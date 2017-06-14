# Url Generator #
****

1. [General information](#markdown-header-general-information)
2. [Dependencies](#markdown-header-dependencies)
3. [Installation](#markdown-header-installation)
4. [Development](#markdown-header-development)
    - [Activate environment for project](#markdown-header-activate-environment-for-project)
    - [Run local server](#markdown-header-run-local-server)
    - [Testing](#markdown-header-testing)
    - [Deactivate environment for project](#markdown-header-deactivate-environment-for-project)
5. [To do's](#markdown-header-to-do's)

## General information ##
Url Generator is a simple Django based app to generate urls from a browser Address Bar.

****
## Dependencies ##

- [Python 3.6](https://www.python.org);
- [pip](https://pypi.python.org/pypi/pip);
- [virtualenv](http://python-guide.readthedocs.org/en/latest/dev/virtualenvs/#virtualenv);
- [Django](https://www.djangoproject.com/);

- for other dependencies see *requirements.txt*;

****
## Installation ##
To complete installation successfully do not forget to install Python 3.6, pip and virtualenv first, then:

```sh
$ make install

```

or if you want run the server at that moment:

```
$ make install_and_run
```

****
## Development ##
### Activate environment for the project ###
```sh
$ source .env/bin/activate
```
****
### Run local server ###
```sh
$ make run
```
*local link*: '127.0.0.1:8000/' or 'localhost:8000/'

****
## Testing ##
### Test server side ###
```sh
$ make test # run all the tests
```

****
### Deactivate environment for project ###
```sh
$ deactivate
```

*Note:* An alternative solution is to use Docker setup with nginx, postgres to achieve a necessary result with party generated url, but it can be a bit overhead for this task.
