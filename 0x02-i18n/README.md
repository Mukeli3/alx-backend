# Project: 0x02. i18n

## Resources

#### Read or watch:

* [Flask-Babel](https://intranet.alxswe.com/rltoken/0m4Qykp52fFH-dPzlWIdkw)
* [Flask i18n tutorial](https://intranet.alxswe.com/rltoken/RtGz7pI7TKnYqrMMG9rWMg)
* [pytz](https://intranet.alxswe.com/rltoken/tw8sQWhB3HJvk3jmR2GBwg)
## Learning Objectives

### General

* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* A <code>README.md</code> file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
* All your <code>*.py</code> files should be executable
* All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
* All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)
* All your functions and methods should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* All your functions and coroutines must be type-annotated.
## Tasks

| Task | File |
| ---- | ---- |
| 0. Basic Flask app | [0-app.py](./0-app.py), [templates/0-index.html](./templates/0-index.html) |
| 1. Basic Babel setup | [1-app.py](./1-app.py), [templates/1-index.html](./templates/1-index.html) |
| 2. Get locale from request | [2-app.py](./2-app.py), [templates/2-index.html](./templates/2-index.html) |
| 3. Parametrize templates | [3-app.py](./3-app.py), [babel.cfg](./babel.cfg), [templates/3-index.html](./templates/3-index.html), [translations/en/LC_MESSAGES/messages.po](./translations/en/LC_MESSAGES/messages.po), [translations/fr/LC_MESSAGES/messages.po](./translations/fr/LC_MESSAGES/messages.po), [translations/en/LC_MESSAGES/messages.mo](./translations/en/LC_MESSAGES/messages.mo), [translations/fr/LC_MESSAGES/messages.mo](./translations/fr/LC_MESSAGES/messages.mo) |
| 4. Force locale with URL parameter | [4-app.py](./4-app.py), [templates/4-index.html](./templates/4-index.html) |
| 5. Mock logging in | [5-app.py](./5-app.py), [templates/5-index.html](./templates/5-index.html) |
| 6. Use user locale | [6-app.py](./6-app.py), [templates/6-index.html](./templates/6-index.html) |
| 7. Infer appropriate time zone | [7-app.py](./7-app.py), [templates/7-index.html](./templates/7-index.html) |

