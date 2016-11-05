# Code2040 Technical Assessment 


## Step 1
import requests

data = {'token':'d50c95fd0c9f433de94c78b5f6001375', 'github':'https://github.com/galani3/api-registration.git'}
response = requests.post("http://challenge.code2040.org/api/register", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))



## Step 2
import requests

data = {'token':'d50c95fd0c9f433de94c78b5f6001375'}
response = requests.post("http://challenge.code2040.org/api/reverse", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))

reverse_string = (response.text)[::-1]
data['string'] = reverse_string

response = requests.post("http://challenge.code2040.org/api/reverse/validate", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))



## Step 3
import requests

data = {'token':'d50c95fd0c9f433de94c78b5f6001375'}
response = requests.post("http://challenge.code2040.org/api/haystack", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))

apiHaystack = response.json()
needleString = apiHaystack["needle"]
for index, word in enumerate(apiHaystack["haystack"]):
    if needleString == word:
        data['needle'] = index

response = requests.post("http://challenge.code2040.org/api/haystack/validate", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))


## Step 4
import requests

data = {'token':'d50c95fd0c9f433de94c78b5f6001375'}
response = requests.post("http://challenge.code2040.org/api/prefix", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))

apiResponse = response.json()
prefix = apiResponse["prefix"]
prefixLength = len(prefix)
arrayforPrefix = []
for word in apiResponse["array"]:
    if prefix != word[0:prefixLength]:
        arrayforPrefix.append(word)

data['array'] = arrayforPrefix
response = requests.post("http://challenge.code2040.org/api/prefix/validate", json = data)
if response.status_code == 400:
    print('Data was not passed, status code: ' + format(response.status_code))

else:
    print('Posted data successfully with status code ' + format(response.status_code))
    

## Step 5
import requests

import dateutil.parser
import datetime

data = {'token':'d50c95fd0c9f433de94c78b5f6001375'}
response = requests.post("http://challenge.code2040.org/api/dating", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))

dateStamp = dateutil.parser.parse((response.json())['datestamp'])
interval = (response.json())['interval']
newDate = dateStamp + datetime.timedelta(seconds = interval)
data['datestamp'] = str(newDate.date())  + 'T' + str(newDate.time()) + 'Z'

response = requests.post("http://challenge.code2040.org/api/dating/validate", json = data)
if response.status_code == 400:
    print('Data was not passed')
else:
    print('Posted data successfully with status code ' + format(response.status_code))


