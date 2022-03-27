"""Template robot with Python."""
import webbrowser
import RPA.Robocorp.Vault
from variables import *
from variables.variables import PASSWORD, USER_NAME

username = USER_NAME
password = PASSWORD
def minimal_task():
    link = "https://"+username+":"+password+"@the-internet.herokuapp.com/basic_auth"
    webbrowser.open(link, new= 2)
    print("Done.")


if __name__ == "__main__":
    minimal_task()