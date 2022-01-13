# GitHub repository analyzer

## 1. Installation

1.1 Clone the repository:
```shell
git clone https://github.com/wojciech-pawlik/gh-analyzer.git
```

1.2 Create a virtual environment
```shell
python -m virtualenv venv
```

1.3.1 (linux/mac) Activate venv, install the requirements using [pip](https://pip.pypa.io/en/stable/getting-started/) and set environmental variable FLASK_APP:
```shell
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
```

1.3.2 (windows) Activate venv, install the requirements using [pip](https://pip.pypa.io/en/stable/getting-started/) and set environmental variable FLASK_APP:
```shell
\venv\Scripts\activate.bat
pip install -r requirements.txt
export FLASK_APP=run.py
```

1.4 Run the application by executing the command:
```shell
flask run
```

## 2. Usage

Run the application by executing the command:
```shell
flask run
```

Open the address on which the application is running:

![image](https://i.snipboard.io/jIWN1V.jpg)

Authorize the app by your GitHub account via OAuth:
![image](https://i.snipboard.io/dIcMP1.jpg)

Select a username which repositories you want to list, next click of the buttons:
- List repos: prints all the received repositories of the selected user with a list of used languages
- List languages: prints all languages used in all repositories of the selected user
![image](https://i.snipboard.io/xLNKYz.jpg)

## 3. Todo
- Manage the authentication directly from the app (GitHub REST API works without a token, however, there exists a limit of 60 requests)
- Secure unexpected cases (eg. failed authorization, achieved the limit of requests)
- Create the layout
- Further development: language usage by time, time series charts, forecasting
