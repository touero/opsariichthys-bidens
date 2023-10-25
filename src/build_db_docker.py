import os

from src.docker_re import DockerRe


class BuildDb(DockerRe):
    def __init__(self, image_name: str = 'mysql:5.7', container_name: str = 'mysql_5.7'):
        super().__init__(image_name, container_name)

    def config(self):
        host_script = os.path.dirname(os.getcwd())
        return {
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


if __name__ == '__main__':
    build_db = BuildDb()
    build_db.start()
