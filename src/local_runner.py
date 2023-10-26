from fish_pond import FishPond

"""
request_type: 请求类型
[0]弃用 [1] GET [2] POST
"""

default_config = {
    "in_server": 0,
    "request_type": 1,
    "from_local": 1,
    "host": "127.0.0.1",
    "port": 2518,
}


fish_pond = FishPond(default_config)
if __name__ == '__main__':
    fish_pond.run()
