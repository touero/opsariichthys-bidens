import json
import docker

from typing import Union
from docker.errors import ImageNotFound
from docker.models.containers import Container
from abc import ABC, abstractmethod

from src.tools import log


class DockerRe(ABC):
    def __init__(self, image_name: str, container_name: str):
        self._client = docker.from_env()
        self.image_name = image_name
        self.container_name = container_name

    def _get_image(self):
        log(f'Finding {self.image_name} docker image in local')
        try:
            self._client.images.get(self.image_name)
        except ImageNotFound as e:
            log(f'ImageNotFound: {str(e)}')
            log(f'Waiting docker pull {self.image_name}')
            for event in self._client.api.pull(self.image_name, stream=True):
                event_info = json.loads(event.decode('utf-8'))
                if 'status' in event_info:
                    status = event_info['status']
                    progress = event_info.get('progress', '')
                    log(f'Status: {status}, Progress: {progress}')
            log(f'Docker pull {self.image_name} finish')
        except Exception as e:
            log(str(e))

    def _get_container(self) -> Union[Container, None]:
        log(f'find {self.container_name} docker container in local')
        containers = self._client.containers.list(all=True)
        for container in containers:
            if self.container_name == container.name:
                log(f'find docker container: {container.id}')
                return container
        log(f'ContainerNotFound: {self.container_name}')
        return None

    def _run_container(self):
        try:
            container = self._client.containers.run(**self.config())
            log(f'container id: {container.id} is running')
        except docker.errors.APIError as e:
            log(f'Error starting container: {e}')
        except Exception as e:
            log(f'An error occurred: {e}')

    @abstractmethod
    def config(self) -> dict:
        raise NotImplemented

    def start(self):
        self._get_image()
        container = self._get_container()
        if container:
            container.start()
        else:
            self._run_container()
