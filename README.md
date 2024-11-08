# A template for generating an executable written in Python

## Building

The first step is creating an environment for Python and installing
build dependencies. It's recommended to build a virtual Python
environment in the folder `env/`. One might run the following
commands.

```
python3 -m venv env
. env/bin/activate
pip install cx_freeze
```

For now the only build requirement is installing the package `cx_freeze`.

To build the application, one runs `python setup.py build`. The
command `python setup.py --help-commands` show all options for
building an application and distributions. In the file `setup.py`
the variables such as the project name, version, packages,
dependencies and others should be configured.

## Running tests

To run the tests, install `pytest` using pip and run it in the
project's root folder.
