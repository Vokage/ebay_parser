import argparse
from pathlib import Path
from ExcelWriter import ExcelWriter
from EbayParser import EbayParser
"""
Parse all active listings for specific accounts and put into an excel worksheet for inventory
Excel workbook will be in the current directory
Script Usage:
    1. Ensure all dependencies have been installed. See README.md
    2. Use command line interface to interact with program and possible options
"""

# Command line interface
ap = argparse.ArgumentParser(prog="Ebay Parser",
                             description="EbayParser is a command line interface to" +
                             " help retrieve active listings for specified accounts" +
                             " and writing data to an excel file")

# accounts argument (required)
ap.add_argument("-a", "--accounts", nargs="+", required=True, help="name of accounts (at least one required)")

# output file name (optional)
default_file_name = "ebay_inventory.xlsx"
ap.add_argument("-fn", "--filename", required=False, default=default_file_name, help="output excel file name")

# file path (optional)
default_file_path = ""
ap.add_argument("-p", "--path", required=False, default=default_file_path, help="file path of destination")

# Parse all arguments
args = ap.parse_args()
account_names = args.accounts
file_name = ExcelWriter.append_excel_extension(args.filename)
file_path = args.path
new_file_path = str((Path(file_path) / file_name).absolute())  # absolute path of new file


# Retrieve all the search results for all the accounts
search_result_list = EbayParser.retrieve_multiple_accounts_active_listings(account_names)
data = EbayParser.search_result_list_to_data(search_result_list)
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
ExcelWriter.write_to_excel_file(new_file_path, headers, data)












# excel_options = {
#     'data': data,
#     'columns': [{'header': 'User Name'},
#                 {'header': 'Listing Id'},
#                 {'header': 'Item Description'},
#                 {'header': 'Price'}],
#     'style': 'Table Style Light 9'
#
#     }
