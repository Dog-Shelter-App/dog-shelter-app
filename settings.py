import os

# Google Oauth Credentials
client_id = os.environ.get("client_id")
project_id = os.environ.get("project_id")
auth_uri = os.environ.get("auth_uri")
token_uri = os.environ.get("token_uri")
auth_provider_x509_cert_url = os.environ.get("auth_provider_x509_cert_url")
client_secret = os.environ.get("client_secret")

# Application cookie secret (long random string)
cookie_secret = os.environ.get("cookie_secret")

################################################################################
# https://stackoverflow.com/questions/9554087/setting-an-environment-variable-in-virtualenv OPEN ENVIRONMENT VARIABLES
################################################################################
# run command: $ nano $VIRTUAL_ENV/bin/postactivate
# for each entry in client_secret.json add to postactivate script
# EX: export client_id="<YOUR_CLIENT_IDE>"




################################################################################
################################################################################
################################################################################
# IMPORTANT!
################################################################################
################################################################################
################################################################################
# 1. DO NOT INCLUDE ANY SPACES, OR IT WILL BREAK
# 2. once you've added all variables, run $ deactivate and then reactivate
#    your virtualenv to have access to new variables.
################################################################################
################################################################################
################################################################################
