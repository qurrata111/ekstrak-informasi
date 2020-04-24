# Extraction Information Application

Algoritma pencocokan string (pattern) Knuth-Morris-Pratt (KMP) dan Algoritma Boyer-Moore
merupakan algoritma yang lebih baik daripada brute force. Aplikasi sederhana ini akan mengekstraksi informasi dengan kedua algoritma tersebut, plus
menggunakan regular expression (regex). Teks yang akan Anda proses adalah teks berita
berbahasa Indonesia dan berbahasa Inggris dengan contoh format (jabar11042020.txt)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
1. Python3
On Windows
- Donwload here https://www.python.org/downloads/
- Install the file by clicking the source file.
On Linux
- Open terminal
- Run these following commands
```sudo apt-get update```
```sudo apt-get install python3.6```
2. Pip3
On Windows
- Download PIP get-pip.py https://bootstrap.pypa.io/get-pip.py on https://bootstrap.pypa.io/get-pip.py
- Open command prompt
- Install pip on windows ```python get-pip.py```

On Linux
- Run this command ```sudo apt-get install python3-pip```
3. Flask 
On Windows
- Install virtual environment e.g.
```\Python27\python.exe Downloads\get-pip.py```
```\Python27\python.exe -m pip install virtualenv```
- Create an environment ```py -3 -m venv venv```, if you need to install virtualvenv try this command ```\Python27\Scripts\virtualenv.exe venv```
- Activate environment ```venv\Scripts\activate```
- Install Flask ```pip3 install Flask```

On Linux
- Install virtual environment ```apt-get install python-virtualenv```
- Create an environment ```python3 -m venv venv```
- Activate environment ```. venv/bin/activate```
- Install Flask ```pip3 install Flask```

## Running the tests

- Open terminal
- Clone or download this project, and run this command (```export FLASK_APP=app```) based on where ```app.py``` is placed 
- Run the app ```flask run```

P.S.: make sure before execute the program you have installed Flask and create environment for this app.

### Thanks to:
https://www.regextester.com/
https://docs.python.org/3/library/re.html
https://flask-doc.readthedocs.io/en/latest/

## Authors

* **Qurrata A'yuni** - *Initial work* - [qurrata111](https://github.com/qurrata111)