import os
import yaml

from argparse import ArgumentParser
from easierdocker import EasierDocker


def main():
    host_script = os.path.dirname(os.getcwd())
    container_script = '/path/to/container'
    config = {
        'image': 'python:3.9',
        'name': name,
        'ports': {'2518/tcp': 2518},
        'volumes': {
            f'{host_script}': {'bind': container_script, 'mode': 'rw'}
        },
        'detach': True,
        'command': ["sh", "-c", f'cd {container_script} &&'
                                'pip install --root-user-action=ignore requests &&'
                                'pip install -r requirements.txt &&'
                                'cd src &&'
                                f'python configure_run.py -y {yaml_dir}']
    }
    easier_docker = EasierDocker(config)
    easier_docker.start()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--config', '-y', default='config/task_config.yaml', help='task config')
    task_config = parser.parse_args()
    yaml_dir = task_config.config
    default_config: dict = yaml.load(open(task_config.config, encoding='utf8'), yaml.FullLoader)
    if default_config.get('docker', None) is not None:
        name = default_config['docker']['name']
    else:
        name = 'opsariichthys-bidens'
    main()
