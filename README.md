# File Hash Calculator

Rainbow Table Generator is a tool allowing you to calculate the hash values of all files in a given folder and save them to the database

**Current Version:** v.1.0.0

**Author**: Louis Nguyen

## Requirements

Python 3.8 and above

## Install

```bash
apt-get -y install git
git clone https://github.com/ngvlz/hash_calculator.git
cd ./hash_calculator
```

## Use

**Command**: `python3 hash_calc.py`

### Example

Terminal output would look like this:

```bash
user@localhost:~$ python3 hash_calc.py

Enter the specific path to the desired directory: ./your_folder_path
-----------------------------------------------------
| File Name               | File Hash               |
-----------------------------------------------------
| file1.txt               | ...[md5]...             |
-----------------------------------------------------
| file2.doc               | ...[md5]...             |
-----------------------------------------------------
| file1.exe               | ...[md5]...             |
-----------------------------------------------------
| file1.xls               | ...[md5]...             |
-----------------------------------------------------
| file1.pdf               | ...[md5]...             |
-----------------------------------------------------
```
