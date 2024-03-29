import os

from automizor import vault

os.environ["AUTOMIZOR_API_HOST"] = "marius.automizor.io"
os.environ["AUTOMIZOR_API_TOKEN"] = "9a912ba276209f5bf54cb6d0590971baeb783657"

secret = vault.get_secret("Airbnb")
print("debug me")
