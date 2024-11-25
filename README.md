# python-IDLE-Tools

## Features

* type ``exit`` for exit python.
* type ``clear`` or ``cls`` to clear python-console.
* use specified imports like all math methods (default).

## Customization
Feel free to add your own imports or commands. \
Open the \_\_init__.py file and add your code.
```python
## CONFIG ##
_CLEAR_ON_START = True  # clear terminal on calling python3

## IMPORTS ##
from math import * #  add your imports here
############
```


## Installation
### 1. Install Packages 
````bash
pip3 install colorama
````
OR
````bash
apt install python3-colorama
````
### 2. Add export to console config

````bash
export PYTHONSTARTUP=<path>/python-IDLE-Tools/__init__.py
````
default: .bashrc file in home folder