import requests


def apiRequest(url):
    try:
        return requests.get(url)
    except requests.exceptions.HTTPError as errh:
        return ("Http Error")
    except requests.exceptions.ConnectionError as errc:
        return ("Error Connecting")
    except requests.exceptions.Timeout as errt:
        return ("Timeout Error")
    except requests.exceptions.RequestException as err:
        return ("OOps: Something Else")
