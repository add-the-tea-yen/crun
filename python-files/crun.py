import os
import subprocess
import argparse

from click import command

parser = argparse.ArgumentParser(description='Make the cpp file execution process simpler')
parser.add_argument('--n', type=str, required=True)

args = parser.parse_args()

command = "g++ " + args.n

os.system(command)
os.system("a")