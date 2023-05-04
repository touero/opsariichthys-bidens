from master import Master
import os

"""
in_docker: 是否在docker运行
task_type: 任务类型
[0]弃用 [1]API
"""

default_config = {
    "in_server": 0,
    "task_type": 1,
    "host": "127.0.0.1",
    "port": 2518,
    "mysql_info": {
        "host": "",
        "port": 3306
    }
}

if __name__ == '__main__':
    Master(default_config).start()
