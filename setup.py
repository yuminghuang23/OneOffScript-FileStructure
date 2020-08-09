# setup.py

import os, sys, re

# get version info from module without importing it
version_re = re.compile("""__version__[\s]*=[\s]*['|"](.*)['|"]""")

with open('hello_world.py') as f:
    content = f.read()
    match = version_re.search(content)
    version = match.group(1)

readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()

SETUP_ARGS = dict(
    name = 'hello_world',
    version = version,
    description = ('Grabs the "Hellow World" Wikipedia page and prints its title'),
    long_description = long_description,
    url = 'github url to be provided',
    author ='<AUTHOR>',
    author_email ='<EMAIL>',
    license = 'MIT',
    include_package_data = True,
    classifiers = [
        'Development Status :; 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approvied :: MIT License',
        'Operating Syste :: OS Independent',
        'Programming Language :: Python :: 3.7',
        ],
    py_modules = ['hello_world',],
    install_requires = [
        'requests >= 2.22',
        ],
    )

if __name__ == '__main__':
    from setuptools import setup, find_packages
    
    SETUP_ARGS['packages'] = find_packages()
    setup(**SETUP_ARGS)