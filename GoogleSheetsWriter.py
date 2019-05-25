import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsWriter:
    def __init__(self, json_credentials_file_name):
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(json_credentials_file_name, self.scope)
        try:
            self.gc = gspread.authorize(self.credentials)
        except:
            print("Invalid credentials file\n"
                  "\tSee https://gspread.readthedocs.io/en/latest/oauth2.html"
                  "\n for creating Credentials File")

    def create_file(self, file_name, email):
        # Create a file and share with
        try:
            self.sh = self.gc.create(file_name)
            self.sh.share(email, perm_type='user', role='writer')
        except gspread.exceptions.APIError as e:
            print("Creating file failed: ")
            print(e)

    def open_file_by_url(self, url):
        self.sh = self.gc.open_by_url(url)

    def open_file_by_key(self, key):
        self.sh = self.gc.open_by_key(key)

    def write_data(self, headers, data):
        if self.sh is None:
            raise Exception("Error: No file to work with. Please create one or open one")
        # print(self.sh.worksheets())
        sheet = self.sh.sheet1
        sheet.clear()
        header_names = []
        for header in headers:
            header_names.append(header['name'])

        data.insert(0, header_names)
        self.sh.values_update(
            'Sheet1!A1',
            params={'valueInputOption': 'RAW'},
            body={'values': data}
        )
