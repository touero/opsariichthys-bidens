<h1 align="center">中国大学的数据信息API搭建</h1>

<p align="center">
<img src="https://img.shields.io/badge/python_-%3E%3D3.8-green" alt=""> <img src="https://img.shields.io/badge/license_-MIT-green" alt=""> <img src="https://img.shields.io/badge/pymysql-blue" alt=""> <img src="https://img.shields.io/badge/dataease-blue" alt="">  <img src="https://img.shields.io/badge/fastapi-blue" alt=""> 
</p>

## 仓库介绍

&emsp;&emsp;本仓库数据来源于我的另一个仓库ScrapySchoolAll, 利用FastAPI构建自定义的API以供任何人在任何地使用, 我个人利用在由飞致云开源的DataEase作图分析.

![img.png](img.png)

本仓库包含以下API：

1. province_count: 各个省份包含大学
2. dual_class_count: 各省份包含双一流数量
3. type_count: 学校类别统计
4. spacial_name_count: 所有专业统计
5. score_province: 招生统计
6. big_data_count: 不同大数据专业统计
7. big_data_province_count: 含大数据专业的省份内大学统计
8. big_data_type_count: 大数据本科专科统计
9. big_data_level2_count: 大数据二级类目统计
10. big_data_level3_count: 大数据一级类目统计
11. big_data_in_dual: 大数据在双一流占比
12. big_data_in_null: 大数据在普通院校占比
13. artificial_intelligence_in_dual: 人工智能在双一流占比
14. artificial_intelligence_in_null: 人工智能在普通院校占比


## 安装

这个项目使用[Python](https://www.python.org/) [Git](https://git-scm.com/) 请确保你本地安装了它们。

```shell
$ git clone https://github.com/weiensong/allSchoolAPI.git
```



## 运行
```sh
$ pip install -r requriements.txt

# local_runner.py中的default_config用以配置任务
$ python3 ./local_runner.py
```


## 相关仓库

- [python](https://github.com/TheAlgorithms/Python) — All Algorithms implemented in Python
- [fastapi](https://github.com/tiangolo/fastapi) — FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [dataease](https://github.com/dataease/dataeasen) — 人人可用的开源数据可视化分析工具
- [ScrapySchoolAll](https://github.com/weiensong/ScrapySchoolAll) — Hadoop,mapreduce分布式爬取掌上高考的所有中国大学数据



## 相关链接

- [fastapi](https://fastapi.tiangolo.com/)
- [飞致云](https://www.fit2cloud.com/)




## 维护者

[@weiensong](https://github.com/weiensong)



## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/weiensong/allSchoolAPI/issues) 或者提交一个 Pull Request。


标准 Python 遵循 [Python PEP-8](https://peps.python.org/pep-0008/) 行为规范。

### 贡献者

感谢参与项目的所有人



## 使用许可

[MIT](LICENSE) © weiensong

