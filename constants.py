Readme = r"""

# {name}

## Installation

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

### Build from Source
Clone the repository and checkout to stable commit

```
git clone https://github.com/cannibalcheeseburger/{name}.git
cd {name}
```

### Install Requirements
For pipenv:
```
pipenv install
```
For pip:
```
pip install -r requirements.txt
```

## Usage

Run Script:
```
python main.py
```

### Contact / Social Media

<a href = "https://www.github.com/cannibalcheeseburger/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/github.svg"  width="30" height="30">
</a>
 
<a href = "https://www.twitter.com/cannibalcheese/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/twitter.svg"  width="30" height="30">
</a>

<a href = "https://www.instagram.com/cannibalcheeseburger/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/instagram.svg"  width="30" height="30">
</a>

<a href = "https://www.facebook.com/kashish.srivastava.351/">
    <img src = "https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/facebook.svg"  width="30" height="30">
</a>

Email: kashish.srivastava014@gmail.com
### Developed by

Developer / Author: [Kashish Srivastava](https://github.com/cannibalcheeseburger/)


"""


license = f"""
MIT License

Copyright (c) 2021 Kashish srivastava

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


gitignore = f"""
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# Some files i use

try.*

"""



manifest = f"""
include README.md
include requirements.txt
include LICENSE
"""

setup  = r"""

import os
from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name='environment-setup',
    version='0.0.1',
    description='Easy environment setup',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kashish Srivastava',
    author_email='kashish.srivastava014@gmail.com',
    url='http://github.com/cannibalcheeseburger/environment-setup',

    packages=find_packages(), # provides same list, looks for __init__.py file in dir
    include_package_data=True,
    install_requires=requirements, #external packages as dependencies

    entry_points={
        'console_scripts': ['envpy=environment_setup.
        :main']
    },

    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    license='MIT License',
)

"""