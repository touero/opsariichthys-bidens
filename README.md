<h1 align="center">opsariichthys-bidens</h1>

<p align="center">
    <img src="https://img.shields.io/badge/python_-%3E%3D3.8-blue" alt=""> 
    <img src="https://img.shields.io/badge/license_-MIT-blue" alt=""> 
    <a href="https://www.mysql.com/"><img src="https://img.shields.io/badge/-mysql-grey?style=plastic&logo=mysql" alt=""/></a>
    <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/fastapi-grey?style=plastic&logo=fastapi" alt=""></a>
    <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/docker-grey?style=plastic&logo=docker" alt=""></a>
    <a href="https://dataease.io/"><img src="https://img.shields.io/badge/dataease-grey" alt=""></a>
</p>

<p align="center">
    <img src=img/opsariichthys-bidens.png height="200" width="200" alt="">
</p>

## Repository Introduction

The data in this repository comes from my other repository--[ctenopharyngodon-idella](https://github.com/weiensong/ctenopharyngodon-idella), which uses the Fast API to build custom APIs for anyone to use anywhere. I personally use Data Ease, which is open source by Feizhi Cloud, for graphical analysis.

This repository contains：

1. province_count: Each province contains a university.
2. dual_class_count: Each province contains the number of double first-class.
3. type_count: School category statistics.
4. spacial_name_count: All majors statistics.
5. score_province: Admissions Statistics.
6. big_data_count: Statistics of different big data majors.
7. big_data_province_count: Statistics of provincial universities including Big data majors.
8. big_data_type_count: Statistics of universities in provinces with big data majors.
9. big_data_level2_count: Big data secondary category statistics.
10. big_data_level3_count: Big data primary category statistics.
11. big_data_in_dual: Proportion of Big Data in 211/985.
12. big_data_in_null: The proportion of big data in ordinary colleges and universities.
13. artificial_intelligence_in_dual: The proportion of artificial intelligence in 211/985.
14. artificial_intelligence_in_null: The proportion of artificial intelligence in ordinary universities.


<table>
    <tr>
        <td><img src=img/terminal.gif alt=""></td>
        <td><img src=img/img_1.png alt=""></td>
    </tr>
    <tr>
        <td><img src=img/docker.png  alt=""></td>
        <td><img src=img/docker_log.png  alt=""></td>
    </tr>
</table>
<table>
    <tr>
        <td><img src=img/province.PNG width="50%" alt=""></td>
        <td><img src=img/major.PNG width="50%" alt=""></td>
    </tr>
</table>



## Install

This project uses [python](https://www.python.org/) [git](https://git-scm.com/) [ngrok](https://ngrok.com/). Go check them out if you don't have them locally installed.

```shell
$ git clone https://github.com/weiensong/opsariichthys-bidens.git
```



## Usage
Create virtual environment installation dependencies

```shell
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install -r requriements.txt
$ cd src
```
Data preparing: a mysql image of version 5.7 build a container in docker and executing file of .withDb/AllSchoolAPI.sql.  
Please waiting info score and major table insert finish. 
```shell
$ python build_db_docker.py
```
Debugging running
```shell
# default_config is used to configure tasks in local_runner.py
$ python local_runner.py
```
If you want to run it in docker
```shell
$ python docker_run.py -y your_config.yaml
```
Even if internal network penetration does not need to be enabled, the service can be started, providing penetration examples.  
Please install ngrok before doing so.  
Connect your ngrok account

```shell
$ ngrok config add-authtoken your_key
```
Setting static IP in https://dashboard.ngrok.com/cloud-edge/domains and run it later.

```shell
$ ngroks/ngrok http --domain=exciting-physically-escargot.ngrok-free.app 2518
```

## Related Repository

- [python](https://github.com/TheAlgorithms/Python) — All Algorithms implemented in Python
- [fastapi](https://github.com/tiangolo/fastapi) — FastAPI framework, high performance, easy to learn, fast to code, ready for production
- [dataease](https://github.com/dataease/dataeasen) — 人人可用的开源数据可视化分析工具
- [ctenopharyngodon-idella](https://github.com/weiensong/ctenopharyngodon-idella) — Hadoop, MapReduce distributed crawling of all Chinese university data for the handheld college entrance examination. (Hadoop,mapreduce分布式爬取掌上高考的所有中国大学数据)


## Related Efforts

- [fastapi](https://fastapi.tiangolo.com/)
- [飞致云](https://www.fit2cloud.com/)
- [ngrok](https://ngrok.com/) 



## Maintainers

[@weiensong](https://github.com/weiensong)



## Contributing


Feel free to dive in! [Open an issue](https://github.com/weiensong/opsariichthys-bidens/issues) or submit PRs.

Standard Python follows the [Python PEP-8](https://peps.python.org/pep-0008/) Code of Conduct.


### Contributors

This project exists thanks to all the people who contribute.



## License

[GNU General Public License v3.0](https://github.com/weiensong/opsariichthys-bidens/blob/master/LICENSE) © weiensong

