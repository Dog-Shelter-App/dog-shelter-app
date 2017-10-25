import os

# Google Oauth Credentials
client_id = "845583204100-mdr5iv0bgkurj3a1ibu6r9k0e4fj8jnh.apps.googleusercontent.com"
project_id = os.environ.get("project_id")
auth_uri = os.environ.get("auth_uri")
token_uri = os.environ.get("token_uri")
auth_provider_x509_cert_url = os.environ.get("auth_provider_x509_cert_url")
client_secret = "HQINf3qMplZ9_5bpEKfI_0w-"

# Application cookie secret (long random string)
cookie_secret = "sdflkjweghwoegjwoekfjwoekfjweogkhwoekjwoeihrgowehfwjhglkdjdksjbvdfjksdahofdjkhdfjkhsdfbdf"

################################################################################
# https://stackoverflow.com/questions/9554087/setting-an-environment-variable-in-virtualenv OPEN ENVIRONMENT VARIABLES
################################################################################
# run command: $ nano $VIRTUAL_ENV/bin/postactivate
# for each entry in client_secret.json add to postactivate script
# EX: export client_id="<YOUR_CLIENT_IDE>"

aws_s3_access_key = "AKIAIKSEMI7ILS6MSJJQ,psW5yhtCR2XWGP1xujYpxQhM5DmIUNmQbAdPwnNK"
aws_s3_secret_access_key = "psW5yhtCR2XWGP1xujYpxQhM5DmIUNmQbAdPwnNK"

mongo_url = "mongodb://dog-shelter-app:123456dogs!@cluster0-shard-00-00-kfusm.mongodb.net:27017,cluster0-shard-00-01-kfusm.mongodb.net:27017,cluster0-shard-00-02-kfusm.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"


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
