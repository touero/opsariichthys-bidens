import os
from argparse import ArgumentParser
from src.docker_re import DockerRe


class DockerRun(DockerRe):
    def __init__(self, yaml_dir: str):
        super().__init__()
        self.yaml_dir = yaml_dir
        self.image_name = 'python:3.9'
        self.container_name = 'opsariichthys-bidens'

    def config(self):
        host_script = os.path.dirname(os.getcwd())
        container_script = '/path/to/container'
        return {
            'image': self.image_name,
            'name': self.container_name,
            'ports': {'2518/tcp': 2518},
            'volumes': {
                f'{host_script}': {'bind': container_script, 'mode': 'rw'}
            },
            'detach': True,
            'command': ["sh", "-c", f'cd {container_script} &&'
                                    'pip install --root-user-action=ignore requests &&'
                                    'pip install -r requirements.txt &&'
                                    'cd src &&'
                                    f'python config_run.py -y {self.yaml_dir}']
        }


parser = ArgumentParser()
parser.add_argument('--config', '-y', default='config/task_config.yaml', help='task config')
if __name__ == '__main__':
    task_config = parser.parse_args()
    config_dir = task_config.config
    docker_run = DockerRun(config_dir)
    docker_run.start()
