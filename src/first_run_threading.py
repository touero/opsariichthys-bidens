import threading
import time
import yaml

from argparse import ArgumentParser

from db_in_docker import BuildDb
from src.flexible_run import DockerRun


class MyThread(threading.Thread):
    def __init__(self, name, instance, method_name):
        super().__init__(name=name)
        self.instance = instance
        self.method_name = method_name

    def run(self):
        print(f'Starting {self.name}')
        method = getattr(self.instance, self.method_name)
        method()
        print(f'Exiting {self.name}')


def main():
    build_db = BuildDb()

    task_config = parser.parse_args()
    yaml_dir = task_config.config
    default_config: dict = yaml.load(open(task_config.config, encoding='utf8'), yaml.FullLoader)
    if default_config.get('docker', None) is not None:
        name = default_config['docker']['name']
    else:
        name = 'opsariichthys-bidens'
    docker_run = DockerRun(container_name=name, config_dir=yaml_dir)
    docker_run.start()

    thread1 = MyThread(name='Thread 1: build db in docker', instance=build_db, method_name='start')
    thread2 = MyThread(name='Thread 2: docker run the api', instance=docker_run, method_name='start')

    thread1.start()
    thread2.start()

    while True:
        if not thread1.is_alive() and not thread2.is_alive():
            print('Both threads have finished their work')
            break
        else:
            print('Waiting for threads to finish...')
            time.sleep(1)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--config', '-y', default='config/task_config.yaml', help='task config')
    main()
