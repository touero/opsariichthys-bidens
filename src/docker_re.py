import json
import docker

from typing import Union
from docker.errors import ImageNotFound
from docker.models.containers import Container
from abc import ABC, abstractmethod

from src.tools import log_t


class DockerRe(ABC):
    def __init__(self, image_name: str, container_name: str):
        self._client = docker.from_env()
        self.image_name = image_name
        self.container_name = container_name

    def _get_image(self):
        log_t(f'Finding {self.image_name} docker image in local')
        try:
            self._client.images.get(self.image_name)
        except ImageNotFound as e:
            log_t(f'ImageNotFound: {str(e)}')
            log_t(f'Waiting docker pull {self.image_name}')
            for event in self._client.api.pull(self.image_name, stream=True):
                event_info = json.loads(event.decode('utf-8'))
                if 'status' in event_info:
                    status = event_info['status']
                    progress = event_info.get('progress', '')
                    log_t(f'Status: {status}, Progress: {progress}')
            log_t(f'Docker pull {self.image_name} finish')
        except Exception as e:
            log_t(str(e))

    def _get_container(self) -> Union[Container, None]:
        log_t(f'find {self.container_name} docker container in local')
        containers = self._client.containers.list(all=True)
        for container in containers:
            if self.container_name == container.name:
                log_t(f'find docker container: {container.id}')
                return container
        log_t(f'ContainerNotFound: {self.container_name}')
        return None

    def _run_container(self):
        try:
            container = self._client.containers.run(**self.config())
            log_t(f'container id: {container.id} is running')
        except docker.errors.APIError as e:
            log_t(f'Error starting container: {e}')
        except Exception as e:
            log_t(f'An error occurred: {e}')

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
