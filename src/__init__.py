# src/__init__.py

# Importing submodules to make them available when `src` is imported
from .password_manager import register, login, storeAccount, queryAccounts
from .database import add_account, retrieve_accounts
