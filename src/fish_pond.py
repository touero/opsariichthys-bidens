import json
import traceback
import uvicorn

from constants import RequestType, API, Server
from tools import log


class FishPond:

    def __init__(self, default_config: dict):
        self.task = default_config
        self.request_type = self.task['request_type']
        self.in_server = self.task['in_server']

    def run(self):
        try:
            if RequestType.is_api_task(self.request_type):
                all_api: dict = {}
                port = self.task['port']
                host = Server.get_machine_host()
                base_url = f'http://{host}:{port}/api'
                if self.request_type == RequestType.API_GET.value:
                    for index, item in enumerate(API):
                        all_api[index + 1] = f'{base_url}/{item.value}'
                    log(f"all_api =\n {json.dumps(all_api, sort_keys=True, indent=4, separators=(',', ': '))}")
                elif self.request_type == RequestType.API_POST.value:
                    for index, item in enumerate(API):
                        base_cmd = '''curl -X POST -H "Content-Type: application/json" -d '''
                        curl_cmd = base_cmd + '\'{"item": "'''f'{item.value}"}}\' {base_url}'
                        log(curl_cmd)
                uvicorn.run(app="api:app", host=host, port=port, reload=True)

        except Exception as e:
            log(str(e))
            log(traceback.format_exc())
