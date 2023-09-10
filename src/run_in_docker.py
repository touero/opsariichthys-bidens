# todo
"""
    From yaml import config and run it in docker
    Please fix it !!
"""
import docker


class FishPond:
    def __init__(self):
        self.client = docker.from_env()
        self.run_command = 'python -c local_runner.py xxx.yaml'

    def run_image(self):
        if self.client is not None:
            image = self.search_image
            if image is None:
                self.client.pull('', stream=True)
                image = self.search_image
            self.client.containers.run(image, self.run_command, ports={'2518/tcp': 2518})

    @property
    def search_image(self):
        local_images = self.client.images()
        for local_image in local_images:
            if 'xxx' in local_image:
                return local_image
        return None


if __name__ == '__main__':
    fish_pond = FishPond()
    fish_pond.run_image()
