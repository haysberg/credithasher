import requests
import json

from cchashlib import stringToIntegerArray

def checkVendor(ccNumber):
    """This function call the binlist API to retrieve information about a card number given in input and prints it on the screen.
    
    Arguments:
        ccNumber {string} -- The card number that the user wants to verify
    """
    if getVendorAPI(ccNumber) != False :
        infos = json.loads(getVendorAPI(ccNumber))
        if 'scheme' in infos:
            print("The vendor of the card is " + infos["scheme"])
        if 'country' in infos:
            print("This card has been issued in : " + infos["country"]["alpha2"])
        if infos["brand"] != None:
            print("This card is a " + infos["brand"] + " card")
    else:
        raise ValueError('The number provided did not link to any vendor.')

def getVendorAPI(ccNumber):
    """This function handles the API call to binlist. This is not in the checkVendor function so that we can reuse it anywhere.
    
    Arguments:
        ccNumber {string} -- The card number we want to verify
    
    Returns:
        json -- The json response that we get from the API
    """

    request = requests.get(url = "https://lookup.binlist.net/" + ccNumber[:8])
    if request.status_code != 200 :
        print('The number provided did not link to any vendor.')
        return False
    return json.dumps(request.json())