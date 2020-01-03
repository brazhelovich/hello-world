#https://python-scripts.com/json - не плохой сайт

import requests
import json
def test_request():
    #response = requests.get('http://10.6.211.178:8080//jira/plugins/servlet/applications/versions-licenses', auth=('admin', 123456))
    response = requests.get('http://10.6.211.178:8080/jira/rest/api/2/issue/PAD-1', auth=('admin', 123456))
    #with open("data_file.json", "w") as write_file:
        #json.dump(response, write_file)
    #data = json.dumps(response)
    #data = print(response.json().dumps
    #print(response)
    data = response.content.decode('UTF-8')
    dat = json.loads(data.)['fields']['issuetype']['description']


    #print(data['sandwich'])


    print(dat)
    #return response

test_request()
