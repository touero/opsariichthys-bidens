
def main():
    from easierdocker import EasierDocker
    import os
    host_script = os.path.dirname(os.getcwd())
    container_config = {
        'image': 'mysql:5.7',
        'name': 'mysql_5.7',
        'environment': {
            'MYSQL_ROOT_PASSWORD': '223366',
            'MYSQL_DATABASE': 'AllSchoolAPI'
        },
        'ports': {'3306': 3306},
        'volumes': {
            f'{host_script}/database/conf.d': {'bind': '/etc/mysql/conf.d', 'mode': 'ro'},
            f'{host_script}/database/mysql': {'bind': '/var/lib/mysql', 'mode': 'rw'},
            f'{host_script}/database': {'bind': '/docker-entrypoint-initdb.d', 'mode': 'ro'}
        },
        'detach': True
    }
    network_config = {
        'driver': 'host',
    }
    easy_docker = EasierDocker(container_config, network_config)
    easy_docker.start()


if __name__ == '__main__':
    main()
