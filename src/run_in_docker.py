import docker
from docker.errors import ImageNotFound
import os

from src.tools import log_t


class FishPond:
    def __init__(self):
        self.client = docker.from_env()
        self.image_name = 'python:3.9'
        self.container_name = 'opsariichthys_bidens'

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
        container_script = "/path/to/container"
        log_t(host_script, container_script)
        volumes = {
            host_script: {
                "bind": container_script,
                "mode": "rw"
            }
        }
        container = self.client.containers.run(
            self.image_name,
            command=["sh", "-c", f'cd {container_script} && '
                                 f'./docker.sh'],
            detach=True,
            volumes=volumes,
            name=self.container_name,
            ports={'2518/tcp': 2518}
        )
        log_t(f'container id: {container.id} is running')

    def start(self):
        self.get_image()
        container = self.get_container()
        if container:
            container.start()
        else:
            self.run_container()


if __name__ == '__main__':
    fish_pond = FishPond()
    fish_pond.start()
