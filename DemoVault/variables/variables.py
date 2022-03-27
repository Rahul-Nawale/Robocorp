import secrets
from RPA.Robocloud.Secrets import Secrets
secrets = Secrets()
USER_NAME = secrets.get_secret("DemoVault")["USER_NAME"]
PASSWORD = secrets.get_secret("DemoVault")["PASSWORD"]