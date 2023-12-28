---
title: "C-Sharp调用存储过程简单完整例子"
slug: "stored-procedure-in-csharp"
author: "Bin Hua"
date: 2009-08-31 05:49:10
tags: ["dotnet"]
draft: false
---

```
CREATE PROC P_TEST
@Name VARCHAR(20),
@Rowcount INT OUTPUT
AS
BEGIN
SELECT * FROM T_Customer WHERE NAME=@Name
SET  @Rowcount=@@ROWCOUNT
END
GO
```

存储过程调用如下:

```
DECLARE @i INT
EXEC P_TEST ‘A’,@i OUTPUT
SELECT @i
```

结果

```
/*
Name       Address    Tel
———- ———- ——————–
A          Address    Telphone

（所影响的行数为 1 行）
———–
1

（所影响的行数为 1 行）
*/
```

```
—————————————————————————————-
–DotNet 部分(C#)
–WebConfig 文件:
—————————————————————————————-
……
</system.web>

<!– 数据库连接字符串
–>
<appSettings>
<add key=”ConnectString” value=”server=(local);User ID=sa;Password=;database=Test” />
</appSettings>

</configuration>
—————————————————————————————-
–C#代码:(用到两个测试控件,DataGrid1(用于显示绑定结果集合),Lable(用于显示存储过程返回单值)
—————————————————————————————-
//添加数据库引用
using System.Data.SqlClient;
……
private void Page_Load(object sender, System.EventArgs e)
{
// 在此处放置用户代码以初始化页面
String DBConnStr;
DataSet MyDataSet=new DataSet();
System.Data.SqlClient.SqlDataAdapter DataAdapter=new System.Data.SqlClient.SqlDataAdapter();
DBConnStr=System.Configuration.ConfigurationSettings.

AppSettings["ConnectString"];
System.Data.SqlClient.SqlConnection myConnection = new System.Data.SqlClient.SqlConnection(DBConnStr);
if (myConnection.State!=ConnectionState.Open)
{
myConnection.Open();
}
System.Data.SqlClient.SqlCommand myCommand = new System.Data.SqlClient.SqlCommand(”P_Test”,myConnection);
myCommand.CommandType=CommandType.StoredProcedure;
//添加输入查询参数、赋予值
myCommand.Parameters.Add(”@Name”,SqlDbType.VarChar);
myCommand.Parameters["@Name"].Value =”A”;

//添加输出参数
myCommand.Parameters.Add(”@Rowcount”,SqlDbType.Int);
myCommand.Parameters["@Rowcount"].Direction=ParameterDirection.Output;
myCommand.ExecuteNonQuery();
DataAdapter.SelectCommand = myCommand;

if (MyDataSet!=null)
{
DataAdapter.Fill(MyDataSet,”table”);
}

DataGrid1.DataSource=MyDataSet;
DataGrid1.DataBind();
//得到存储过程输出参数
Label1.Text=myCommand.Parameters["@Rowcount"].Value.ToString();

if (myConnection.State == ConnectionState.Open)
{
myConnection.Close();
}

}
```

运行以上代码即可(返回记录集合和存储过程返回值)

**又一.NET调用存储过程的实例**

```
/供前台页面调用的方法，这个方法必须是protected或者public
protected void ShowData()
{
//实例化Connection对象
SqlConnection connection = new SqlConnection(”Data Source=(local);Initial Catalog=AspNetStudy;Persist Security Info=True;User ID=sa;Password=sa”);
//实例化Command对象
SqlCommand command = new SqlCommand(”GetAllUsers”, connection); //GetAllUsers是存储过程名字
command.CommandType=CommandType.StoredProcedure;//表示执行的是存储过程
SqlDataAdapter adapter = new SqlDataAdapter(command);
/*
下面的被注释掉的代码与上面的代码是等效的
SqlDataAdapter adapter = new SqlDataAdapter(”select * from UserInfo where sex=0″, connection);
*/
DataTable data = new DataTable();
adapter.Fill(data);
/* 下面的被注释掉语句与上面填充DataTable的效果是一样的，我更倾向于没有注释掉的部分
DataSet ds = new DataSet();//实例化DataSet
adapter.Fill(ds, “UserInfo”);//填充ds中的”UserInfo”表
DataTable data = ds.Tables["UserInfo"];
*/
for (int i = 0; i < data.Rows.Count; i++)
{
Response.Write(”
” + data.Rows[i]["UserId"].ToString() + ”

“);
Response.Write(” ” + data.Rows[i]["UserName"].ToString() + ”

“);
Response.Write(” ” + data.Rows[i]["RealName"].ToString() + ”

“);
Response.Write(” ” + data.Rows[i]["Age"].ToString() + ”

“);
//下面是按照列顺序直接读取值，并且根据值来判断最终显示结果
Response.Write(” ” + (bool.Parse(data.Rows[i]["Sex"].ToString()) == true ? “男” : “女″) + ”

“);
//根据列顺序读，列的值需要做相应转换
Response.Write(” ” + data.Rows[i]["Mobile"].ToString() + ”

“);
//根据列名来读取，列的值需要做相应转换
Response.Write(” ” + data.Rows[i]["Phone"].ToString() + ”

“);
Response.Write(” ” + data.Rows[i]["Email"].ToString() + ”

\n”);
}
}
}
```