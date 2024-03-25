def main():
    import os
    host_script = os.getcwd()
    container_script = '/path/to/container'
    config = {
        'image': 'python:3.9',
        'name': 'opsariichthys-bidens',
        'ports': {'2518/tcp': 2518},
        'volumes': {
            f'{host_script}': {'bind': container_script, 'mode': 'rw'}
        },
        'detach': True,
        'command': ["sh", "-c", f'cd {container_script} &&'
                                'ls &&'
                                'pip install --root-user-action=ignore requests &&'
                                'pip install -r requirements.txt &&'
                                f'python run.py']
    }
    from easierdocker import EasierDocker
    easier_docker = EasierDocker(config)
    easier_docker.start()


if __name__ == '__main__':
    main()
