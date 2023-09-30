import yaml

from argparse import ArgumentParser

from fish_pond import FishPond

parser = ArgumentParser()
parser.add_argument('--config', '-y', default='config/task_config.yaml', help='task config')
if __name__ == '__main__':
    task_config = parser.parse_args()
    default_config = yaml.load(open(task_config.config, encoding='utf8'), yaml.FullLoader)
    FishPond(default_config).start()

