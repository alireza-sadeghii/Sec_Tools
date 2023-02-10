# @Author : Alireza
# CS50 Project
# Sec Tools : Ip Check


import json
import requests

# declare API key for abuseIpDB
API_KEY = "42e4f799187a8e763bffd01667b074785a5d23db4db2fee5007792a460c45749bd1721dac4f0d912"

# check ip provided by user
def check_ip(ip):
    output = []
    abuse_url = "https://api.abuseipdb.com/api/v2/check"
    header = {
        'Accept' : 'application/json',
        'Key' : API_KEY
    }
    param = {
        'ipAddress' : ip
    }
    try:
        result = requests.request(method='GET', url=abuse_url, headers=header, params=param)
    except:
        output.append("Can't Reach AbuseIpDb !")
        return output

    if result.status_code == 429:
        output.append("Got Error 429 !")
        output.append("Error : Rate Limiting Reached")
        return output
    result = json.loads(result.text)
    try:
        if result["errors"]:
            output.append("AbuseIPDB Error :: " + ip)
            output.append(result['errors'][0]['detail'])
    except:
        config_check_output(result, output)
    return output

# configure result of ip check
def config_check_output(result, out):
    out.append("Ip : " + result['data']['ipAddress'])
    out.append("Public : " + ("[+]" if result['data']['isPublic'] else "[-]"))
    out.append("Ip Version : " + str(result['data']['ipVersion']))
    out.append("Whitelisted : " + ("[+]" if result['data']['isWhitelisted'] else "[-]"))
    out.append("Confidence Score : " + str(result['data']['abuseConfidenceScore']))
    out.append("Country : " + result['data']['countryCode'])
    out.append("Domain : " + result['data']['domain'])
    out.append("-" * 20)
    out.append("Total Reports : " + str(result['data']['totalReports']) + "\n")
