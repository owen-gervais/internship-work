from onshape_client.client import Client
import json
import sys

# Reads in your personal api-key files
key = ""
secret = ""
with open("api-key", "r") as f: 
        key = f.readline().rstrip()
        secret = f.readline().rstrip()

base_url = 'https://rogers.onshape.com'

# ENTER THE ONSHAPE PARAMETERS BELOW:
did = '5180c826cc8ee318e7669421'
wid = 'dd443cb272828ce48b0bb115'
eid = 'c3d902ec77c01bd9d08f2120'
pid = 'JSD'

# Esatblishing the headers for the request
headers = {'Accept-Encoding': 'applicaton/vnd.onshape.v1+json', 'Content-Type': 'application/json'}

# Creating the Onshape API Client instance
client = Client(configuration ={"base_url": base_url, "access_key": key, "secret_key": secret})

# The RGB values are obtained from the command line prompt in the main.py
red = int(sys.argv[1])
green = int(sys.argv[2])
blue = int(sys.argv[3])

# Opacity is hardcoded below
opac = 255

# Request body is defined below 
body = { "properties":[{ "propertyId": "57f3fb8efa3416c06701d60c","value": {"color": {"red": red,"green": green,"blue": blue},"opacity": opac }}]}

# POST Request is sent with the established url, query, headers, and body
r = client.api_client.request('POST', url = base_url + '/api/metadata/d/'+did+'/w/'+ wid +'/e/'+ eid +'/p/' + pid,query_params={},headers = headers, body=body)
print('COMPLETED, check the updated Part Studio in Onshape')
