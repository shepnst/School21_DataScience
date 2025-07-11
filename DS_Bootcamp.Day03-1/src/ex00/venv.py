import os

if os.getenv('VIRTUAL_ENV'):
    print(f"Your current virtual env is {os.getenv('VIRTUAL_ENV')}")
else:
    print("virtual env is not active")
