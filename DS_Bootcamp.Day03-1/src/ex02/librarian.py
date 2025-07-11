import sys
import os
import subprocess


if not sys.prefix != sys.base_prefix:
    raise ValueError("you are not in virtual env")

if os.path.basename(sys.prefix) != 'eldissda':
    raise ValueError("you are in wrong virtual env")

try:
    subprocess.check_call([sys.executable, '-m', 'pip',
                          'install', 'beautifulsoup4', 'pytest'])
except subprocess.CalledProcessError as error:
    print(f'there is an error: {error}')

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])

with open('requirements.txt', 'w') as r:
    r.write(reqs.decode('utf-8'))

