# Создать скрипт, который принимает имя папки и создает ее рядом со скриптом

import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-md', '--name_dir')
args = parser.parse_args()

dir_path = os.path.dirname(__file__)

os.mkdir(os.path.join(dir_path, args.name_dir))
