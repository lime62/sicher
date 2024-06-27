import re
import hashlib

from src.database import add_user

# Registration and Login
def register():
  userPattern = "^[a-zA-Z0-9_-]{4,15}$"
  passPattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{16,}$"

  flag = False

  while(flag != True):
    username = input("Enter your username: ")
    if(re.match(userPattern, username)):
      flag = True
      print("Valid username.")
    else:
      print("Username must be between 4 and 15 characters")

  flag = False
  while(flag != True):
    password = input("Enter your master password: ")
    if(re.match(passPattern, password)):
      print("Valid password.")
      password_bytes = password.encode('utf-8')
      hash_obj = hashlib.sha256(password_bytes)
      pass_hash = hash_obj.hexdigest()
      print("Saving user to the database.")
      add_user(username, pass_hash)
      print(username, "is now registered.")
      flag = True
    else:
      print("Password must be at least 16 characters, include one uppercase letter and one special character.")
