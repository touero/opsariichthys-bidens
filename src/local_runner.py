from master import Master

"""
in_docker: 是否在docker运行
task_type: 任务类型
[0]弃用 [1]API
"""

default_config = {
    "in_docker": 0,
    "task_type": 1,
    "host": "127.0.0.1",
    "port": 2518,
}

if __name__ == '__main__':
    Master(default_config).start()
