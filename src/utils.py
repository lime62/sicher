import re
import hashlib
import os

from src.database import add_user, getUsername, getMasterPassword, getSalt

userPattern = "^[a-zA-Z0-9_-]{4,15}$"
passPattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{16,}$"

# Registration and Login
def register():
  flag = False

  while(flag != True):
    username = input("Enter your username: ")
    if(getUsername(username)):
      print("Username is already taken.")
    else:
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
      salt = os.urandom(32)
      password_bytes = salt + password.encode('utf-8')
      hash_obj = hashlib.sha256(password_bytes)
      pass_hash = hash_obj.hexdigest()
      print("Saving user to the database.")
      add_user(username, pass_hash, salt)
      print(username, "is now registered.")
      flag = True
    else:
      print("Password must be at least 16 characters, include one uppercase letter and one special character.")

def login():
  username = input("Enter your username: ")
  if(getUsername(username)):
    if(re.match(userPattern, username)):
      password = input("Enter your password: ")
      if(re.match(passPattern, password)):
        salted_pass = getSalt(username) + password.encode('utf-8')
        hashed_obj = hashlib.sha256(salted_pass)
        pass_hash = hashed_obj.hexdigest()
        return pass_hash == getMasterPassword(username)
      else:
          print('Password is not in the correct format.')
    else:
      print('Username is not in the correct format.')
  else:
    print('Username does not exist.')
          