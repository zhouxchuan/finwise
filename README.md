# FInWise

#### 介绍
一个私人理财管理工具，帮助用户管理个人资产、支出和收入，提供财务分析和建议。

#### 软件架构
软件架构说明


#### 安装教程

1.  创建MySQL数据库
    - 打开MySQL命令行客户端或使用MySQL Workbench等工具。
    - 通过sql/finwise.sql执行以下命令创建数据库和数据表结构：
      ```sql
      source sql/finwise.sql;
      ```
    为user_account创建一个默认用户，用户名和密码均为admin。

2.  配置数据库连接
    - 在utils/msyqldb.py中配置数据库连接信息，包括数据库URL、用户名和密码。

3.  运行项目
    - 确保Python环境已安装，推荐使用Python 3.8及以上版本。
    - 安装项目依赖，执行以下命令：
      ```bash
      pip install -r requirements.txt
      ```
    - 运行项目，执行以下命令：
      ```bash
      python main.py
      ```
    - 或者使用IDE直接运行`main.py`文件。

#### 使用说明

1.  启动项目后，登录管理员账号和密码。
2.  登录后，点击导航栏的“用户管理”，添加普通用户账号。
3.  普通用户登录后，即可管理自己的资产、支出和收入。

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
