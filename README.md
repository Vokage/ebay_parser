# Ebay Parser

> A simple command line interface to retrieve active listings for specified ebay accounts and write the data to excel.

## Prerequisites

- [Python 3](https://www.python.org/downloads/)

### Python Dependencies

See Pipfile

## Installation

```
git clone https://github.com/Vokage/ebay_parser.git
cd ebay_parser
pipenv install
pipenv run
```

## Usage

```
usage: Ebay Parser [-h] -a ACCOUNTS [ACCOUNTS ...] [-fn FILENAME] [-p PATH]

EbayParser is a command line interface to help retrieve active listings for
specified accounts and writing data to an excel file

optional arguments:
  -h, --help            show this help message and exit
  -a ACCOUNTS [ACCOUNTS ...], --accounts ACCOUNTS [ACCOUNTS ...]
                        name of accounts (at least one required)
  -fn FILENAME, --filename FILENAME
                        output excel file name
  -p PATH, --path PATH  file path of destination
  -gsurl GOOGLESHEETS_URL, --googlesheets-url GOOGLESHEETS_URL
                        URL of google sheet
  -gs GOOGLESHEETS, --googlesheets GOOGLESHEETS
                        Use existing google sheets
  -gs-c GOOGLESHEETS_CREDENTIALS, --googlesheets-credentials GOOGLESHEETS_CREDENTIALS
                        Path to google sheets credentials
```

### Examples

```
### Get help
python parse_main.py -h

### Write active listings for single account to excel file in current directory
python parse_main.py -a account_name

### Write active listings for multiple accounts to excel file in current directory
python parse_main.py -a account_name1 account_name 2

### Write active listings for single account to excel file at the specified directory and specified file name
python parse_main.py -a account_name -fn output_file_name -p output_path

### Write active listings to active google sheets (Clears and rewrites file)
python parse_main.py -a account_name -gs True -gsurl [url/to/googlesheet/document] -gs-c [path/to/secrets.json]
```

## Use Cases

- Book keeping for ebay account
- Excel data aggregation
