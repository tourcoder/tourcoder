---
title: "将 Google Cloud Firestore 中的数据导入到 Cloudflare KV 中"
slug: "how-to-make-connection-between-google-cloud-firestore-and-cloudflare-kv"
author: "Bin Hua"
date: 2025-03-04T05:39:08Z
tags: ["googlecloud", "firestore", "cloudflare"]
draft: false
---

做了下尝试，将 Google Cloud 上 Firestore 里的数据导入到 Cloudflare 的 KV 里，主要实现思路是

- Firestore 里每个 collection 作为 Cloudflare 里的一个 KV

- collection 里的每个文档作为 kv 里的一条数据，key 对应文档的 ID，value 为文档的值

废话少说，直接上代码

```
const { Firestore } = require('@google-cloud/firestore');
const ProgressBar = require('progress');

// 配置 Firestore
const firestore = new Firestore({
  projectId: 'GOOGLE_CLOUD_PROJECT_ID', // 替换为你的 Google Cloud 项目 ID
  keyFilename: './service-account.json', // 指向服务账号密钥文件
  databaseId: 'DATABASE_ID', // 如果是 (default) 可不写
});

// 配置 Cloudflare
const accountId = 'YOUR_CLOUDFLARE_ACCOUNT_ID'; // 替换为您的 Cloudflare 账户 ID
const apiToken = 'YOUR_API_TOKEN'; // 替换为您的 API Token

// 获取或创建 KV 命名空间
async function getOrCreateNamespace(collectionId) {
  const listUrl = `https://api.cloudflare.com/client/v4/accounts/${accountId}/storage/kv/namespaces`;
  
  // 获取现有命名空间
  const listResponse = await fetch(listUrl, {
    headers: {
      'Authorization': `Bearer ${apiToken}`,
      'Content-Type': 'application/json',
    },
  });
  const listData = await listResponse.json();
  if (!listResponse.ok) {
    throw new Error(`获取命名空间列表失败: ${listResponse.status} ${listResponse.statusText}`);
  }

  // 检查是否已存在同名命名空间
  const existingNamespace = listData.result.find(ns => ns.title === collectionId);
  if (existingNamespace) {
    console.log(`复用现有命名空间: ${collectionId} (ID: ${existingNamespace.id})`);
    return existingNamespace.id;
  }

  // 创建新命名空间
  const createUrl = listUrl;
  const createResponse = await fetch(createUrl, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiToken}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title: collectionId }),
  });
  const createData = await createResponse.json();
  if (!createResponse.ok) {
    throw new Error(`创建命名空间 ${collectionId} 失败: ${createResponse.status} ${createResponse.statusText}`);
  }

  console.log(`创建新命名空间: ${collectionId} (ID: ${createData.result.id})`);
  return createData.result.id;
}

// 从 Firestore 读取数据并组织为集合
async function fetchFirestoreData() {
  const collectionsData = {};

  try {
    const collections = await firestore.listCollections();
    console.log(`发现 ${collections.length} 个集合`);

    for (const collection of collections) {
      const collectionId = collection.id;
      console.log(`正在处理集合: ${collectionId}`);

      const snapshot = await firestore.collection(collectionId).get();
      collectionsData[collectionId] = {};

      snapshot.forEach(doc => {
        collectionsData[collectionId][doc.id] = JSON.stringify(doc.data());
      });
    }

    return collectionsData;
  } catch (error) {
    console.error('读取 Firestore 数据时出错:', error);
    throw error;
  }
}

// 上传到指定 KV 命名空间
async function uploadToKV(namespaceId, kvData, batchSize = 1000) {
  const totalEntries = Object.entries(kvData).length;
  console.log(`命名空间 ${namespaceId} 总共有 ${totalEntries} 条数据需要上传`);

  const bar = new ProgressBar('上传进度 [:bar] :percent | :current/:total | ETA: :etas', {
    total: totalEntries,
    width: 40,
    complete: '=',
    incomplete: ' ',
  });

  const entries = Object.entries(kvData);
  const batches = [];
  for (let i = 0; i < entries.length; i += batchSize) {
    batches.push(entries.slice(i, i + batchSize));
  }

  for (let batchIndex = 0; batchIndex < batches.length; batchIndex++) {
    const batch = batches[batchIndex];
    const promises = batch.map(async ([key, value]) => {
      try {
        const response = await fetch(
          `https://api.cloudflare.com/client/v4/accounts/${accountId}/storage/kv/namespaces/${namespaceId}/values/${key}`,
          {
            method: 'PUT',
            headers: {
              'Authorization': `Bearer ${apiToken}`,
              'Content-Type': 'application/json',
            },
            body: value,
          }
        );
        if (!response.ok) {
          throw new Error(`上传失败: ${key} - ${response.status} ${response.statusText}`);
        }
        bar.tick();
      } catch (error) {
        console.error(`错误在键 ${key}:`, error.message);
      }
    });

    await Promise.all(promises);
    console.log(`批次 ${batchIndex + 1}/${batches.length} 完成`);
  }

  console.log(`命名空间 ${namespaceId} 所有数据上传完成！`);
}

// 主函数
async function main() {
  try {
    // 从 Firestore 获取数据
    const collectionsData = await fetchFirestoreData();

    // 为每个集合创建或获取命名空间并上传数据
    for (const [collectionId, kvData] of Object.entries(collectionsData)) {
      console.log(`\n处理集合: ${collectionId}`);
      const namespaceId = await getOrCreateNamespace(collectionId);
      await uploadToKV(namespaceId, kvData, 1000);
    }

    console.log('\n所有集合数据已成功导入 Cloudflare KV！');
  } catch (error) {
    console.error('处理过程中发生错误:', error);
  }
}

// 执行
main();
```

如果有问题，欢迎留言 :)