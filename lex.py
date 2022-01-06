import requests
import urllib3
from pprint import pprint
import json
import random
import geopy
from geopy.geocoders import Nominatim
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

key = 'AIzaSyARWvZu2Mlus1TEE-noRIoCqY9sU8fLY0U'

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

#resultJSON = verifyPassword('xpfizmahxciipjcbms@bptfp.net', True, 'letsgooooo123')
#idToken = resultJSON['idToken']

def createUser(birthdate, firstName, pronoun, latitude, longitude, enableNotificationsMessages, enableNotificationsPostLikes, enableNotificationsNewPostNearby, username, idToken):
    body = {
            'birthdate': f'{birthdate}T05:00:00.000Z',
            'fcmToken': 'drac5f3hU0_Dl1BXPjXc-p:APA91bE2lYoDeHKd_fTEaCqkEGsRkUXrPwfjRqfsVGTfDVzl14DGTajTmlDeWQkdLgKVNbtBLT5s3yGbfX0q4HqX61qLUk22S2hBQGfdf_w0tD0Q7c1eGVheZlTqGn14RTU179faz1_Z',
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

def loopChicago():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 41.85003, -87.65005, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'hello!', 'personal', idToken)

def loopVancouver():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 49.246292, -123.116226, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopToronto():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 43.651070, -79.347015, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopNewYork():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 40.730610, -73.935242, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopLondon():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 51.509865, -0.118092, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopSanFran():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 37.773972, -122.431297, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopLA():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 34.05223, -118.24368, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopBoston():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 42.361145, -71.057083, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopPortland():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 45.523064, -122.676483, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopSeattle():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 47.608013, -122.335167, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopAtlanta():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 33.753746, -84.386330, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopAustin():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 30.266666, -97.733330, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopPhilly():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 39.952583, -75.165222, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)

def loopCharlotte():
    signupJSON = signupNewUser(f'{random.randint(100, 6000)}@zwoho.com', True, 'peachesareyummy321')
    print(signupJSON)
    idToken = signupJSON['idToken']
    createUser('1990-10-11', 'jane', 'She/Her', 35.227085, -80.843124, True, True, True, str(random.randint(100, 6000)), idToken)
    createPost('read this', 'https://files.cargocollective.com/c523136/01_Post-Trans_Booklet_EN.pdf', 'personal', idToken)


#newJSON = createUser('2001-09-11', 'amber', 'She/Her', 41.8781, 87.6298, True, True, True, 'marina23', idToken)
#newJSON = createPost('i love u all', 'stay safe', 'personal', idToken)
#print(newJSON)
#resultJSON = signupNewUser('xpfizmahxciipjcbms@bptfp.net', True, 'letsgooooo123')
#localId = resultJSON['localId']
#print(resultJSON)
#getOobConfirmationCode(idToken, 'VERIFY_EMAIL')
