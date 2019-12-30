import requests

def test_request():
    #response = requests.get('http://IP:8080//jira/plugins/servlet/applications/versions-licenses', auth=('admin', 123456))
    response = requests.get('http://IP:8080/jira/rest/api/2/avatar', auth=('admin', 123456))
    return response.content.decode('UTF-8')
print(test_request())
