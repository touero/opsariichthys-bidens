import json
import traceback
import uvicorn

from constants import TaskType, API, Server
from tools import log_t


class FishPond:

    def __init__(self, default_config):
        self.task = default_config
        self.task_type = self.task['task_type']
        self.in_server = self.task['in_server']

    def start(self):
        try:
            if self.task_type == TaskType.API.value:
                all_api = {}
                port = self.task['port']
                host = Server.get_machine_type()
                for index, item in enumerate(API):
                    all_api[index + 1] = f'http://{host}:{port}/api/{item.value}'
                log_t(f"all_api =\n {json.dumps(all_api, sort_keys=True, indent=4, separators=(',', ': '))}")
                uvicorn.run(app="api:app", host=host, port=port, reload=True)

        except Exception as e:
            log_t(str(e))
            log_t(traceback.print_exc())
