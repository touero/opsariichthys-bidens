import json
import traceback
import uvicorn
from constants import RequestType, API, Server
from tools import log_t


class FishPond:

    def __init__(self, default_config):
        self.task = default_config
        self.request_type = self.task['request_type']
        self.in_server = self.task['in_server']

    def start(self):
        try:
            if self.request_type in RequestType.api_task():
                all_api: dict = {}
                port = self.task['port']
                host = Server.get_machine_host()
                for index, item in enumerate(API):
                    all_api[index + 1] = f'http://{host}:{port}/api/{item.value}'
                log_t(f"all_api =\n {json.dumps(all_api, sort_keys=True, indent=4, separators=(',', ': '))}")
                if self.request_type == RequestType.API_GET.value:
                    uvicorn.run(app="api_get:app", host=host, port=port, reload=True)
                elif self.request_type == RequestType.API_POST.value:
                    uvicorn.run(app="api_post:app", host=host, port=port, reload=True)

        except Exception as e:
            log_t(str(e))
            log_t(traceback.print_exc())
