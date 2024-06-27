# src/__init__.py

# Importing submodules to make them available when `src` is imported
from .utils import register
from .encryption import encrypt, decrypt
from .database import add_account, retrieve_accounts
