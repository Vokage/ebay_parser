# Ebay Parser
> A simple command line interface to retrieve active listings for specified ebay accounts and write the data to excel.

## Prerequisites
- [Python 3](https://www.python.org/downloads/)

### Python Dependencies
- [xlsx writer](https://xlsxwriter.readthedocs.io/)
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [urllib](https://docs.python.org/3/library/urllib.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [pipenv](https://docs.pipenv.org/en/latest/)
## Installation
```
git clone https://github.com/Vokage/ebay_parser.git
cd ebay_parser
pipenv install
```
## Usage
```
usage: Ebay Parser [-h] -a ACCOUNTS [ACCOUNTS ...] [-fn FILENAME] [-p PATH]

EbayParser is a command line interface to help retrieve active listings for
specified accounts and writing data to an excel file

optional arguments:
  -h, --help                                                       show this help message and exit
  -a ACCOUNTS [ACCOUNTS ...], --accounts ACCOUNTS [ACCOUNTS ...]   name of accounts (at least one required)
  -fn FILENAME, --filename FILENAME                                output excel file name
  -p PATH, --path PATH                                             file path of destination

```

### Examples
```
### Get help
pipenv run parse_main.py -h

### Write active listings for single account to excel file in current directory
pipenv run parse_main.py -a account_name

### Write active listings for multiple accounts to excel file in current directory
pipenv run parse_main.py -a account_name1 account_name 2

### Write active listings for single account to excel file at the specified directory and specified file name
pipenv run parse_main.py -a account_name -fn output_file_name -p output_path
```

## Use Cases
- Book keeping for ebay account
- Excel data aggregation
