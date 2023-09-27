import docker
from docker.errors import ImageNotFound
import os


class FishPond:
    def __init__(self):
        self.client = docker.from_env()
        self.image_name = 'python:3.9'
        self.container_name = 'opsariichthys_bidens'

    def get_image(self):
        try:
            self.client.images.get(self.image_name)
        except ImageNotFound as e:
            print(str(e))
            print(f'waiting docker pull {self.image_name}')
            self.client.images.pull(self.image_name)
            print(f'docker pull {self.image_name} finish')

    def get_container(self):
        containers = self.client.containers.list(all=True)
        for container in containers:
            if self.container_name == container.name:
                return container
        return None

    def run_container(self):
        host_script = os.getcwd()
        container_script = "/path/to/container/test"
        volumes = {
            host_script: {
                "bind": container_script,
                "mode": "rw"
            }
        }
        container = self.client.containers.run(
            self.image_name,
            command=["python", f'{container_script}/local_runner.py'],
            detach=True,
            volumes=volumes,
            name=self.container_name,
            ports={'2518/tcp': 2518}
        )
        container.wait()

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
