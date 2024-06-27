import sys
sys.path.append('C:\\Users\\Margaret\\Documents\\GitHub\\sicherdet\\sicher\\')

from src.password_manager import register, login, storeAccount, getAccounts
from src.database import initialize_tables

#print('Starting program...')
#initialize_tables()
#print('Databases set!')

#if register():
#  print("Registration sucessful!")
#else:
#  print("Registration failed. Exiting.")
#  exit()

if login():
  print('Login sucessful!')
  storeAccount()
  print(getAccounts())
else:
  print('Login failed. Exiting.')
  exit()



