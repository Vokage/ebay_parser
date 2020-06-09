import argparse
from pathlib import Path
from ExcelWriter import ExcelWriter
from EbayParser import EbayParser
from GoogleSheetsWriter import GoogleSheetsWriter
"""
Parse all active listings for specific accounts and put into an excel worksheet for inventory
Excel workbook will be in the current directory
Script Usage:
    1. Ensure all dependencies have been installed. See README.md
    2. Use command line interface to interact with program and possible options
"""

ap = argparse.ArgumentParser(prog="Ebay Parser",
                             description="EbayParser is a command line interface to" +
                             " help retrieve active listings for specified accounts" +
                             " and writing data to an excel file")
ap.add_argument("-a", "--accounts", nargs="+", required=True, help="name of accounts (at least one required)")
default_file_name = "ebay_inventory.xlsx"
ap.add_argument("-fn", "--filename", required=False, default=default_file_name, help="output excel file name")
ap.add_argument("-p", "--path", required=False, default="", help="file path of destination")
ap.add_argument("-gsurl", "--googlesheets-url", required=False, default="", help="URL of google sheet")
ap.add_argument("-gs", "--googlesheets", required=False, default="", help="Use existing google sheets")
ap.add_argument("-gs-c", "--googlesheets-credentials", required=False, default="", help="Path to google sheets credentials")

args = ap.parse_args()
account_names = args.accounts
file_name = ExcelWriter.append_excel_extension(args.filename)
file_path = args.path
new_file_path = str((Path(file_path) / file_name).absolute())


# Retrieve all the search results for all the accounts
ebay_parser = EbayParser()
normalized_data = []
for account_name in account_names:
    account = ebay_parser.account(account_name)
    search_results = account.retrieve_active_listings()
    data = map(lambda sr:
               [account_name, sr.id(), sr.title(), sr.price()], search_results)
    normalized_data.extend(data)

# Headers for the excel file
headers = [{'name': "User Name",
            'format_options': {}},

           {'name': "Listing Id",
            'format_options':
                {'num_format': 1}},

           {'name': "Item Description",
            'format_options': {}},

           # TODO: Make this so it doesnt round
           {'name': "Price",
            'format_options':
                {'num_format': 5}}]

# Write the results to the excel file
ExcelWriter.write_to_excel_file(new_file_path, headers, normalized_data)

if args.googlesheets:
    gc = GoogleSheetsWriter(args.googlesheets_credentials)
    gc.open_file_by_url(args.googlesheets_url)
    gc.write_data(headers, normalized_data)
