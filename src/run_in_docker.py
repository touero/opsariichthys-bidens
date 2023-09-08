# todo
"""
    From yaml import config and run it in docker
    Please fix it !!
"""
import docker


def run_image(client, command):
    if client is not None:
        image = search_image(client)
        if image is None:
            client.pull('', stream=True)
            image = search_image(client)
        client.containers.run(image, command, ports={'2518/tcp': 2518})


def search_image(client):
    local_images = client.images()
    for local_image in local_images:
        if 'xxx' in local_image:
            return local_image
    return None


if __name__ == '__main__':
    command = 'python -c local_runner.py xxx.yaml'
    client = docker.from_env()
    run_image(client)
