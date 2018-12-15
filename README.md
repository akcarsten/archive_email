import getEmail
import getpass


# Define parameters:
server = 'imap.MY_HOST.COM'
account = 'MY_EMAIL@MY_HOST.COM'
folder = 'Inbox'
output = './mails'
pwd = getpass.getpass()


# Usage 1:
a = getEmail.Retrieve(server=server,
                      account=account,
                      folder=folder,
                      output=output,
                      pwd=pwd)
a.run()


# Usage 2:
a = getEmail.Retrieve()
a.connect(server)
a.login(account, pwd)
rv, data = a.search_folder(folder)
if rv == 'OK':
    a.download_mails(data)
