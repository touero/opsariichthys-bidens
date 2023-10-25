import os
import yaml

from argparse import ArgumentParser

from src.docker_re import DockerRe


class DockerRun(DockerRe):
    def __init__(self, container_name: str, config_dir: str, image_name: str = 'python:3.9'):
        super().__init__(image_name, container_name)
        self.config_dir = config_dir

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
                                    f'python config_run.py -y {self.config_dir}']
        }


parser = ArgumentParser()
parser.add_argument('--config', '-y', default='config/task_config.yaml', help='task config')
if __name__ == '__main__':
    task_config = parser.parse_args()
    yaml_dir = task_config.config
    default_config = yaml.load(open(task_config.config, encoding='utf8'), yaml.FullLoader)
    docker_run = DockerRun(container_name=default_config['docker']['name'], config_dir=yaml_dir)
    docker_run.start()
