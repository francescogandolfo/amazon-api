import sys
import requests
import requests_aws4auth as aws4auth
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from credentials import access_id, access_key, region,zoneid


endpoint = 'https://route53.amazonaws.com/2013-04-01/hostedzone/'

ns = 'https://route53.amazonaws.com/doc/2013-04-01/'


def xml_pprint(xml_string):
    print(minidom.parseString(xml_string).toprettyxml())

def getHostedZoneResponse(url,zoneid,auth):
    urlZoneId = url + '/' + zoneid
    response = requests.get(urlZoneId,auth=auth)
    if response.status_code == 200:
        xml_pprint(response.text)
    else:
        print ("problemi autenticazione")


if __name__ == '__main__':
    # oggetto autenticazione
    authObj = aws4auth.AWS4Auth(access_id, access_key, region, 'route53')
    getHostedZoneResponse(endpoint,zoneid,auth=authObj)
