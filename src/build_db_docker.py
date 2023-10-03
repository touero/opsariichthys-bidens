import os

import docker
from docker.errors import ImageNotFound

from src.tools import log_t


class BuildDb:
    def __init__(self):
        self.client = docker.from_env()
        self.image_name = 'mysql:5.7'
        self.container_name = 'mysql'

    def get_image(self):
        try:
            self.client.images.get(self.image_name)
        except ImageNotFound as e:
            log_t(f'ImageNotFound: {str(e)}')
            log_t(f'waiting docker pull {self.image_name}')
            self.client.images.pull(self.image_name)
            log_t(f'docker pull {self.image_name} finish')
        except Exception as e:
            log_t(str(e))

    def get_container(self):
        containers = self.client.containers.list(all=True)
        for container in containers:
            if self.container_name == container.name:
                log_t(f'docker find container: {container.id}')
                return container
        return None

    def run_container(self):
        host_script = os.path.dirname(os.getcwd())
        mysql_config = {
            'image': self.image_name,
            'name': self.container_name,
            'environment': {
                'MYSQL_ROOT_PASSWORD': '223366',
                'MYSQL_DATABASE': 'AllSchoolAPI'
            },
            'ports': {'3306/tcp': 3306},
            'volumes': {
                f'{host_script}/.withDb/conf.d': {'bind': '/etc/mysql/conf.d', 'mode': 'ro'},
                f'{host_script}/.withDb/mysql': {'bind': '/var/lib/mysql', 'mode': 'rw'},
                f'{host_script}/.withDb': {'bind': '/docker-entrypoint-initdb.d', 'mode': 'ro'}
            },
            'detach': True
        }
        container = self.client.containers.run(**mysql_config)
        log_t(f'container id: {container.id} is running')

    def start(self):
        self.get_image()
        container = self.get_container()
        if container:
            container.start()
        else:
            self.run_container()


if __name__ == '__main__':
    build_db = BuildDb()
    build_db.start()

