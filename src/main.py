import sys
sys.path.append('C:\\Users\\Margaret\\Documents\\GitHub\\sicherdet\\sicher\\')

from src.utils import register, login

if login():
  print('Login sucessful!')
else:
  print('Login unsucessful!')
