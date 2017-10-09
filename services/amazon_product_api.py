# os imports
import os

# timestamp
import time
import datetime

# open url
import webbrowser

# encryption
import hmac
import hashlib
import base64
from Crypto.Hash import SHA256 as sha256

###################################
# 1. Define Constants and audibles#
###################################

service = "AWSECommerceService"
AWS_ACCESS_KEY_ID= "AKIAIJIKZZ7QKYQ56KEQ"
AWS_SECRET_KEY= "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"
ASSOCIATE_TAG = "4dconsulting-20"
AWS_SECRET_KEY= "1234567890"
operation = "ItemSearch"
brand = "Coleman"
# MY VERSION response = "Images%2CItemAttributes%2COffers"
response = "Images%2CItemAttributes%2COffers"
version = "2013-08-01"
service = "AWSECommerceService"

# base url
base_url = "webservices.amazon.com/onca/xml?"

# Prepare for encoding parameter string
http_prefix = "http://"
comma ="%2C"
colon= "%3A"

# generate time stamp, format utc iso... YOU HAVE 20 MICROSECONDS TO GET THIS THING GOING
time_stamp = datetime.datetime.utcnow().isoformat()

##########################
# 2. Build our parameters#
##########################

# # # # ORDER OF THINGS
# 1. AWS_ACCESS_KEY_ID
# 2. AssociateTag
# 3. IdType=ASIN
# 4. ItemId=B071V82JJG
# 5. Operation=ItemLookup
# 6. ResponseGroup=
# 7. Service=AWSECommerceService
# 8. Timestamp=2017-10-06T02%3A42%3A53.000Z
# 9. Signature=EfLYYlVHWqxaZZjC0HX%2FFraOB4bHKYjk8%2FkJXi1IESM%3D

key_param = "AWS_ACCESS_KEY_ID={}".format(AWS_ACCESS_KEY_ID)
associate_param = "AssociateTag={}".format(ASSOCIATE_TAG)
brand_param = "Brand={}".format(brand)
operation_param = "Operation={}".format(operation)
response_param = "ResponseGroup={}".format(response)
service_param = "Service={}".format(service)
time_stamp_param = "Timestamp={}".format(time_stamp)
version_param = "Version={}".format(version)

#################################
# 3. Assemble/Format our Request#
#################################

# Format parameter string
params = [key_param, associate_param, brand_param, operation_param, response_param, service_param, time_stamp_param, version_param]
params_string = "&".join(params)

# Build GET REQUEST
url = base_url + params_string

# Encode commas and colons
encoded_commas = url.replace(",", comma)
encoded_colons = encoded_commas.replace(":", colon)

# Stage GET request for encryption
dig_string = "GET\nwebservices.amazon.com\n/onca/xml\n" + "AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&ItemId=0679722769&Operation=ItemLookup&ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews&Service=AWSECommerceService&Timestamp=2014-08-18T12%3A00%3A00Z&Version=2013-08-01"

# Encode request
dig_string_encoded = dig_string.encode('utf-8')

# Encrypt request
dig = hmac.new(b'+DwXFtp4/KFpAFe/2FeGfMv0Rn4kim4/vNzawe36', msg=dig_string_encoded, digestmod=hashlib.sha256).digest()

signature = quote(
    b64encode(hmac.new(AWS_SECRET_KEY, dig_string, sha256).digest()))

print(signature)


# This doesn't work unless I decode it,,, but I just encoded it.. wtf
hash_string = base64.b64encode(dig).decode()

# Stage for hash encoding
plus = "%2B"
equal_sign = "%3D"

# Encode Hash
hash_string_plus = hash_string.replace("+", plus)
hash_string = hash_string_plus.replace("=", equal_sign)

# Stage final URL
final_url = http_prefix + encoded_colons + "&Signature=" + hash_string

# Check your work
print(final_url)
# Send your request
webbrowser.open(final_url)
