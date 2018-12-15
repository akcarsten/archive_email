import imaplib
import os


class Retrieve(object):

    def __init__(self, server=None, account=None, folder=None, output=None, pwd=None):

        self.imap_server = server
        self.email_account = account
        self.email_folder = folder
        self.output = output
        self.email_pwd = pwd

        self.M = []

    def connect(self, server=None):
        if self.imap_server is None:
            self.imap_server = server

        self.M = imaplib.IMAP4_SSL(self.imap_server)

    def login(self, account=None, pwd=None):
        if self.email_account is None:
            self.email_account = account
        if self.email_pwd is None:
            self.email_pwd = pwd

        self.M.login(self.email_account, self.email_pwd)

    def search_folder(self, folder='Inbox'):
        if self.email_folder is None:
            self.email_folder = folder

        rv, data = self.M.select(self.email_folder)
        if rv == 'OK':
            # Search folder
            rv, data = self.M.search(None, "ALL")
            return rv, data

    def download_mails(self, data, output='./mails2'):
        if self.output is None:
            self.output = output

        # Check if output folder exists
        if os.path.isdir(self.output) is False:
            os.mkdir(self.output)

        # Download mails to folder
        for mail in data[0].split():
            mail_rv, mail_data = self.M.fetch(mail, '(RFC822)')
            if mail_rv == 'OK':
                print('Writing data to folder')
                f = open('{}/{}.eml'.format(self.output, mail), 'wb')
                f.write(mail_data[0][1])
                f.close()
            else:
                print('Cannot write file')

    def run(self):
        print('Downloading mail')

        # Connect to IMAP server
        self.connect()

        # Log into account
        self.login()

        # Select and search folder to download
        rv, data = self.search_folder()

        # Download mails
        if rv == 'OK':
            self.download_mails(data)
        else:
            print('Folder not found')
