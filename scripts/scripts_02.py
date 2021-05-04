# Создать скрипт, который принимает имя фамилию
# и возраст и дописывает их в файл

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first_name', type=str)
parser.add_argument('-ln', '--last_name', type=str)
parser.add_argument('-a', '--age', type=int)
args = parser.parse_args()
args_arr = f"{args.first_name} {args.last_name} {args.age}\n"

with open('text_for_02.txt', 'a') as txtfile:
    txtfile.write(args_arr)
