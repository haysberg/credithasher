import requests
import json

from cchashlib import stringToIntegerArray

def checkVendor(ccNumber):
    """This function call the binlist API to retrieve information about a card number given in input and prints it on the screen.
    
    Arguments:
        ccNumber {string} -- The card number that the user wants to verify
    """

    #If we get a response from the API
    if getVendorAPI(ccNumber) != False :
        #We parse the JSON that we got previously.
        infos = json.loads(getVendorAPI(ccNumber))

        #All those if statements will tell us if we have the data we need or not.
        #On some occasions, we can retrieve the vendor of the card (for example Visa or Mastercard)
        #But we can't get what country it was issued in.
        if 'scheme' in infos:
            print("The vendor of the card is " + infos["scheme"])
        if 'country' in infos:
            print("This card has been issued in : " + infos["country"]["alpha2"])
        try:
            if 'brand' in infos :
                print("This card is a " + infos["brand"] + " card")
        except:
            print('We could not find any brand for the card.')


def getVendorAPI(ccNumber):
    """This function handles the API call to binlist. This is not in the checkVendor function so that we can reuse it anywhere.
    
    Arguments:
        ccNumber {string} -- The card number we want to verify
    
    Returns:
        array -- The json response that we get from the API, transformed into a format Python can use
    """

    #We make an HTTP GET request to the binlist API giving the first 8 numbers of the credit card given, no need for more.
    request = requests.get(url = "https://lookup.binlist.net/" + ccNumber[:8])

    #If we do not get a valid response from the server...
    if request.status_code != 200 :
        #We print that we didn't get any response from the server...
        print('The number provided did not link to any vendor.')
        #And return false, so that the checkVendor function knows that the request failed.
        return False

    #If the request works, we send the json to the checkVendor function, that will parse the JSON to get infos from it.
    return json.dumps(request.json())