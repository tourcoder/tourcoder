---
title: ".net 文章分页"
slug: "pages-in-dotnet"
author: "Bin Hua"
date: 2009-01-22 05:12:51
tags: ["dotnet"]
draft: false
---

.net 文章分页，主要是通过文章页面字符的个数进行分页的，这里需要注意的是

- 去HTML，不然会出现超级搞笑的代码现象哦

- 如果是纯文本，建议使用，如果不是纯文本的，强烈不建议使用，如果是文本的，请使用字符分页方式。 

    ```
    public string OutputBySize(string p_strContent)//分页函数
        {
            string m_strRet = "";
            int m_intPageSize = 1000;//文章每页大小
            int m_intCurrentPage = 1;//设置第一页为初始页
            int m_intTotalPage = 0;
            int m_intArticlelength = p_strContent.Length;//文章长度
            if (m_intPageSize < m_intArticlelength)
            {//如果每页大小大于文章长度时就不用分页了
                if (m_intArticlelength % m_intPageSize == 0)
                {//set total pages count
                    m_intTotalPage = m_intArticlelength / m_intPageSize;
                }
                else
                {//if the totalsize
                    m_intTotalPage = m_intArticlelength / m_intPageSize + 1;
                }
                if (Request.QueryString["ps"] != null)
                {//set Current page number
                    try
                    {//处理不正常的地址栏的值
                        m_intCurrentPage = Convert.ToInt32(Request.QueryString["ps"]);
                        if (m_intCurrentPage > m_intTotalPage)
                            m_intCurrentPage = m_intTotalPage;
    
                    }
                    catch
                    {
                        //m_intCurrentPage = m_intCurrentPage;
                    }
                }
                //set the page content 设置获取当前页的大小
                if (m_intCurrentPage < m_intTotalPage)
                {
                    m_intPageSize = m_intCurrentPage < m_intTotalPage ? m_intPageSize : (m_intArticlelength - m_intPageSize * (m_intCurrentPage - 1));
                    m_strRet += p_strContent.Substring(m_intPageSize * (m_intCurrentPage - 1), m_intPageSize);
                }
                else if (m_intCurrentPage == m_intTotalPage)
                {
                    int mm_intPageSize = m_intArticlelength - m_intPageSize * (m_intCurrentPage - 1);
                    m_strRet += p_strContent.Substring(m_intArticlelength - mm_intPageSize);
                }

                string m_strPageInfo = "";
                for (int i = 1; i <= m_intTotalPage; i++)
                {
                    if (i == m_intCurrentPage)
                        m_strPageInfo += "[" + i + "]";
                    else
                        m_strPageInfo += " < a href="?id="</span"> + Id + "&ps=" + i + ">[" + i + "] ;

                }
                if (m_intCurrentPage > 1)
                    m_strPageInfo = "  "< a href="?id="</span"> + Id + "&ps=" + (m_intCurrentPage - 1) + ">上一页  + m_strPageInfo;
                if (m_intCurrentPage < m_intTotalPage)
                    m_strPageInfo += " "< a href="?id="</span"> + Id + "&ps=" + (m_intCurrentPage + 1) + ">下一页 ;
                //输出显示各个页码
                this.ShowPageNumber.Text = " " + m_strPageInfo;
            }
            else
            {
                m_strRet += p_strContent;
            }
            return m_strRet;
        } "
        ```

**update@20090922:PagedDataSource分页方式**

.NET分页的方式很多，网上也有很多的分页的控件，这里和大家分享一个简单的分页方式 PagedDataSource 分页。

我们先来了解下它的相关属性

PagedDataSource 类的部分公共属性：

AllowCustomPaging 获取或设置指示是否启用自定义分页的值。

AllowPaging 获取或设置指示是否启用分页的值。

Count 获取要从数据源使用的项数。

CurrentPageIndex 获取或设置当前页的索引。

DataSource 获取或设置数据源。

DataSourceCount 获取数据源中的项数。

FirstIndexInPage 获取页中的第一个索引。

IsCustomPagingEnabled 获取一个值，该值指示是否启用自定义分页。

IsFirstPage 获取一个值，该值指示当前页是否是首页。

IsLastPage 获取一个值，该值指示当前页是否是最后一页。

IsPagingEnabled 获取一个值，该值指示是否启用分页。

IsReadOnly 获取一个值，该值指示数据源是否是只读的。

IsSynchronized 获取一个值，该值指示是否同步对数据源的访问（线程安全）。

PageCount 获取显示数据源中的所有项所需要的总页数。

PageSize 获取或设置要在单页上显示的项数。

VirtualCount 获取或设置在使用自定义分页时数据源中的实际项数。

实例代码:

```
string strsql = “这里是你的SQL语句”;
SqlConnection objConnection = new SqlConnection(ConfigurationSettings.AppSettings["dns"]);
objConnection.Open();
SqlDataAdapter da = new SqlDataAdapter(strsql, objConnection);
DataSet ds = new DataSet();
da.Fill(ds, “tc”);//这里可写成da.Fill(ds);
objConnection.Close();
//对PagedDataSource 对象的相关属性赋值
PagedDataSource ps = new PagedDataSource();
ps.DataSource = ds.Tables["tourcoder"].DefaultView;//对应上面ds.Tables[0].DefaultView;
ps.AllowPaging = true;
ps.PageSize = 20;

int CurPage;
if (Request.QueryString["Page"] != null)
CurPage = Convert.ToInt32(Request.QueryString["Page"]);
else CurPage = 1;
ps.CurrentPageIndex = CurPage – 1;
lblCurrentPage.Text = “当前在第” + CurPage.ToString() + “/” + ps.PageCount.ToString() + “页”;
if (!ps.IsFirstPage) lnkPrev.NavigateUrl = “所在页面名字”?Page=” + Convert.ToString(CurPage – 1);
if (!ps.IsLastPage) lnkNext.NavigateUrl = “所在页面名字”?Page=” + Convert.ToString(CurPage + 1);
fenye.DataSource = ps;
fenye.DataBind();
```