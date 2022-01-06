import requests
import urllib3
from pprint import pprint
import json
import random
import geopy
from geopy.geocoders import Nominatim
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

key = 'KEY'

def signupNewUser(email, returnSecureToken, password):
    body = {'email': email, 'returnSecureToken': returnSecureToken,'password': password}
    body = json.dumps(body)
    r = requests.post(f'https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key={key}', headers={'Host': 'www.googleapis.com', 'User-Agent': 'FirebaseAuth.iOS/7.11.0 us.personals/1.38 iPhone/14.6 hw/iPhone10_4','Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive', 'X-Client-Version': 'iOS/FirebaseSDK/7.11.0/FirebaseCore-iOS', 'Content-Length': '104', 'Origin': 'https://www.googleapis.com'}, data=body, verify=False)
    resultJSON = r.json()
    return resultJSON

def verifyPassword(email, returnSecureToken, password):
    body = {'email': email, 'returnSecureToken': returnSecureToken,'password': password}
    body = json.dumps(body)
    r = requests.post(f'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={key}', headers={'Host': 'www.googleapis.com', 'User-Agent': 'FirebaseAuth.iOS/7.11.0 us.personals/1.38 iPhone/14.6 hw/iPhone10_4','Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive', 'X-Client-Version': 'iOS/FirebaseSDK/7.11.0/FirebaseCore-iOS', 'Content-Length': '104', 'Origin': 'https://www.googleapis.com'}, data=body, verify=False)
    resultJSON = r.json()
    return resultJSON

def getOobConfirmationCode(idToken, requestType):
    body = {'idToken': idToken, 'requestType': requestType}
    body = json.dumps(body)
    r = requests.post(f'https://www.googleapis.com/identitytoolkit/v3/relyingparty/getOobConfirmationCode?key={key}', headers={'Host': 'www.googleapis.com', 'User-Agent': 'FirebaseAuth.iOS/7.11.0 us.personals/1.38 iPhone/14.6 hw/iPhone10_4','Accept-Encoding': 'gzip, deflate, br', 'Connection': 'keep-alive', 'X-Client-Version': 'iOS/FirebaseSDK/7.11.0/FirebaseCore-iOS', 'Content-Length': '104', 'Origin': 'https://www.googleapis.com'}, data=body, verify=False)
    resultJSON = r.json()
    return resultJSON

def createUser(birthdate, firstName, pronoun, latitude, longitude, enableNotificationsMessages, enableNotificationsPostLikes, enableNotificationsNewPostNearby, username, idToken):
    body = {
            'birthdate': f'{birthdate}T05:00:00.000Z',
            'fcmToken': 'TOKEN',
            'firstName': firstName,
            'pronoun': pronoun,
            'location': {
                'latitude': latitude,
                'longitude': longitude
            },
            'settings': {
                'enableNotificationsMessages': enableNotificationsMessages,
                'enableNotificationsPostLikes': enableNotificationsPostLikes,
                'enableNotificationsNewPostNearby': enableNotificationsNewPostNearby
            },
            'username': username
        }
    body = json.dumps(body)
    r = requests.post('https://us-central1-personals-personals.cloudfunctions.net/createUser', headers={'Host': 'us-central1-personals-personals.cloudfunctions.net', 'User-Agent': 'Lex/56 CFNetwork/1240.0.4 Darwin/20.5.0', 'Accept': 'application/json', 'Accept-Language': 'en-us', 'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/json', 'Connection': 'keep-alive', 'x-clientversion': '1.38.1', 'x-lex-device-id': 'xxxxxx', 'Authorization': f'Bearer {idToken}', 'Content-Length': '0', 'Upgrade-Insecure-Requests': '1'}, data=body, verify=False)
    resultJSON = r.json()
    return resultJSON

def createPost(title, content, type, idToken):
    body = {'title': title, 'content': content, 'type': type}
    body = json.dumps(body)
    r = requests.post('https://us-central1-personals-personals.cloudfunctions.net/createPost', headers={'Host': 'us-central1-personals-personals.cloudfunctions.net', 'User-Agent': 'Lex/56 CFNetwork/1240.0.4 Darwin/20.5.0', 'Accept': 'application/json', 'Accept-Language': 'en-us', 'Accept-Encoding': 'gzip, deflate, br', 'Content-Type': 'application/json', 'Connection': 'keep-alive', 'x-clientversion': '1.38.1', 'x-lex-device-id': 'xxxxxx', 'Authorization': f'Bearer {idToken}', 'Content-Length': '0', 'Upgrade-Insecure-Requests': '1'}, data=body, verify=False)
    resultJSON = r.json()
    return resultJSON

