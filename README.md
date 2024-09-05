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
    <img src=.public/opsariichthys-bidens.png height="200" width="200" alt="">
</p>

## Repository Introduction


The data in this repository comes from my other repository--[ctenopharyngodon-idella](https://github.com/weiensong/ctenopharyngodon-idella), which uses the Fast API to build custom APIs for anyone to use anywhere. Support for _GET_ and _POST_ requests. I personally use Data Ease, which is open source by Feizhi Cloud, for graphical analysis.  

<a><img src=.public/preview.png alt=""></a>

This repository contains：
| **number** | **item name** | **details** |
| :---- | :---- | :---- |
| **1** | **province** | **Each province contains a university** |
| **2** | **dual_class** | **Each province contains the number of double first-class** |
| **3** | **type** | **School category statistics** |
| **4** | **spacial_name** | **All majors statistics** |
| **5** | **score_province** | **Admissions Statistics** |
| **6** | **big_data** | **Statistics of different big data majors** |
| **7** | **big_data_province** | **Statistics of provincial universities including Big data majors** |
| **8** | **big_data_type** | **Statistics of universities in provinces with big data majors** |
| **9** | **big_data_level2** | **Big data secondary category statistics** |
| **10** | **big_data_level3** | **Big data primary category statistics** |
| **11** | **big_data_in_dual** | **Proportion of Big Data in 211/985** |
| **12** | **big_data_in_null** | **The proportion of big data in ordinary colleges and universities** |
| **13** | **artificial_intelligence_in_dual** | **The proportion of artificial intelligence in 211/985** |
| **14** | **artificial_intelligence_in_null** | **The proportion of artificial intelligence in ordinary universities** |


## Frontend

[AnabasTestudineus](https://github.com/touero/AnabasTestudineus)

## Install

This project uses [python](https://www.python.org/) [git](https://git-scm.com/). Go check them out if you don't have them locally installed.
```shell
git clone https://github.com/weiensong/opsariichthys-bidens.git
```

Creating the virtual environment and activating it.
```shell
python -m venv venv && source ./venv/bin/activate
```

Installing dependencies.
```shell
pip install -r requriements.txt
```

## Usage

Running in local machine:
```shell
python run.py
```

If you want to run it in docker
```shell
python docker_run.py
```

If you want to build image by yourself.
```shell
sudo docker build -t opsariichthys_bidens:lastest .
```

```shell
docker run -d -v "$(pwd):/app" -p 2518:2518 --name opsariichthys_bidens opsariichthys_bidens:lastest
```


If you want to use curl to access:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"key": "item"}' http://127.0.0.1:2518/api
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

[@touero](https://github.com/touero)



## Contributing


Feel free to dive in! [Open an issue](https://github.com/weiensong/opsariichthys-bidens/issues) or submit PRs.

Standard Python follows the [Python PEP-8](https://peps.python.org/pep-0008/) Code of Conduct.


### Contributors

This project exists thanks to all the people who contribute.



## License

[GNU General Public License v3.0](https://github.com/weiensong/opsariichthys-bidens/blob/master/LICENSE) © weiensong

