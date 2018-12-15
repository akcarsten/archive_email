# What is getEmail
getEmail is a simple tool that lets you download emails from your email account (IMAP server). Each mail will be stored as an .eml file which can be read with various email programs. It can be helpfull if you want to quickly backup your email account.

# Installation
To install getEmail on your computer just clone the repository, open a terminal, go to the repo folder and run:

```Python
$ python setup.py install
```

# Example usage
Below you can find two examples on how to use the getEmail functionality. In the first example all input parameters are set right away. With the entire email folder can be copied to your HDD in just two lines of code.

In the second example each method is called separately.

```Python
import getEmail
import getpass

# Define parameters:
server = 'imap.MY_HOST.COM' # IMAP address of your email provider
account = 'MY_EMAIL@MY_HOST.COM' # Your email address
folder = 'Inbox' # Can be any folder in your email account
output = './mails' # Folder where email will be stored
pwd = getpass.getpass() # Allows you to enter your password
```

### Usage 1:
```Python
mail = getEmail.Retrieve(server=server,
                      account=account,
                      folder=folder,
                      output=output,
                      pwd=pwd)
mail.run()
```

### Usage 2:
```Python
mail = getEmail.Retrieve()
mail.connect(server)
mail.login(account, pwd)
rv, data = mail.search_folder(folder)
if rv == 'OK':
    mail.download_mails(data)
```
