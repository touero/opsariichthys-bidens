from fish_pond import FishPond

"""
in_docker: 是否在docker运行
task_type: 任务类型
[0]弃用 [1]API
"""

default_config = {
    "in_server": 0,
    "task_type": 1,
    "from_local": 1,
    "host": "127.0.0.1",
    "port": 2518,
}

if __name__ == '__main__':
    FishPond(default_config).start()

