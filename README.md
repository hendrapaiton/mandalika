# MANDALIKA

Python Flask Restful JWT Authentication with MongoDB


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development 
and testing purposes.

### Prerequisites
Before you can run this project you need a install python first on your operating system.
You can download python [here](https://www.python.org/downloads/) and choose according to your operating system.

### Installing

First, clone this project from github using git command or git gui application like [fork](https://git-fork.com/).
```
$ git clone https://github.com/hendrapaiton/mandalika.git
```

Making environment for project to isolation python installing libraries for this project only.
```
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Installing all libraries needed by this project using [pip](https://pypi.org/project/pip/)
```
$ pip install -r requirements.txt
```

Setting the environment for this project.
```
$ export FLASK_APP=app.py
$ export ENV_FILE_LOCATION=./.env
``` 

Running the project.
```
flask run
```

## Authors

**Hendra Dwi Saputra** - *Initial work* - [hendrapaiton](https://github.com/hendrapaiton)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details