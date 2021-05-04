# Создать скрипт. Программа принимает имя папки и имя файла с расширением.
# Создает папку и создает в ней файл. Если расширение файла py
# - записывает в файл следующее:
import os
import argparse

text_for_py = """
def main():
    pass


if __name__ == '__main__':
    main()
"""

parser = argparse.ArgumentParser()
parser.add_argument('-nd', '--new_dir')
parser.add_argument('-nf', '--new_file')
args = parser.parse_args()

if not os.path.isdir(args.new_dir):
    os.mkdir(args.new_dir)
file_path = os.path.join(args.new_dir, args.new_file)
end_name = file_path.split('.')

new_file = open(file_path, 'w')
if end_name[-1] == 'py':
    new_file.write(text_for_py)
new_file.close()
