import yaml

from argparse import ArgumentParser

from fish_pond import FishPond

parser = ArgumentParser()
parser.add_argument('--config', '-y', default='config/task_config.yaml', help='task config')
task_config = parser.parse_args()
default_config: dict = yaml.load(open(task_config.config, encoding='utf8'), yaml.FullLoader)
fish_pond = FishPond(default_config['config'])

if __name__ == '__main__':
    fish_pond.run()
