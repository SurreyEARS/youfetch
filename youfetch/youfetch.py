from requests import get

def getpublicip():
    # Use the ifconfig.me service to get the public ip address.
    result = get("https://ifconfig.me").text

    return result
