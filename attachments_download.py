import requests
import json
import os



def download(list, folder):
        path = 'C:/Users/Andrei_Brazhalovich/PycharmProjects/EPAM/venv/'
        fol = path + folder
        #print(list)
        try:
                papka = str(os.makedirs(fol, exist_ok=True))

                for i in list:
                        sp = i.split('/')
                        print(sp[7])
                        get = requests.get(i, auth=('admin', 123456), verify=False)
                        with open(fol+'/'+sp[7], 'wb') as f:
                                f.write(get.content)
                                f.close()
        except FileExistsError:
                print('Cannot create a folder when that file already exists')
        else:
                print('The folder was created successfully')

                        #print('Done ' + n + ' ' + i)
                #print(url)
        #get = requests.get(url, auth=('admin', 123456), verify=False)
        #for i in list:

#https://10.6.211.178/jira/secure/attachment/10100/avatar.JPG

def get_issuetype():
        n = 0
        #open('Attachments/project_attach/')
        list_content = []
        list_file_name = []
        url = 'http://10.6.211.178:8080/jira/rest/api/2/issue/'
        issue_key = 'za-2'
        #response = requests.get('http://10.6.211.178:8080/jira/rest/api/2/issuetype/10002', auth=('admin', 123456))
        response = requests.get(url+issue_key, auth=('admin', 123456))
        #response = requests.get(url, auth=('admin', 123456))
        probe = response.content.decode('UTF-8')
        res = json.loads(probe)
        result = json.dumps(res, indent=4)
        print('Return code: '+str(response.status_code)+'\n')


        count = len(res['fields']['attachment'])
        if count == 0:
                print('No attachments')

        else:
                while n < count:
                        print('Have ' + str(count) + ' attachment(s)')
                        list_content.append(res['fields']['attachment'][n]['content'])
                        #list_file_name.append(res['fields']['attachment'][n]['filename'])
                        n +=1
        #print(list_file_name)
        #print(list_content)

                download(list_content, issue_key)
        #print(res['issueTypes'][1]['self'])
        #print(res['fields']['attachment'][0]['content'])
        #content = res['fields']['attachment'][1]['content']

        #for attach in

        #print(result)
get_issuetype()