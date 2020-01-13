import requests
import json
import sys

#from easygui import passwordbox


def get_exp_date(expire):
    message = []
    for link in expire:

        url_exp = 'http://10.6.211.178' + link + '/license'
        #print(url_exp)
        response = requests.get(url_exp, auth=('admin', 123456), verify=False)

        dec = response.content.decode('UTF-8')
        parsed_string = json.loads(dec)
        result = json.dumps(parsed_string, indent=4)
        message.append('Name of plugin: ' + str(parsed_string['pluginKey']).split('.')[-1] + '\n' 'Expire date: ' + parsed_string['expiryDateString'] + '\n')
        print('Name of plugin: ' + str(parsed_string['pluginKey']).split('.')[-1] + '\n' 'Expire date: ' + parsed_string['expiryDateString'] + '\n')
    #print('\n'.join(message))
    print('Return code: ' + str(response.status_code) + '\n')

    notify('\n'.join(message))
    slack_notify('\n'.join(message))

def slack_notify(probe):

    #probe = 'Check'
    data = {'text': probe}
    response = requests.post('https://hooks.slack.com/services/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', json=data)

def notify(message):
    # !/usr/bin/env python

    #message = sys.argv[1]

    requests.post("https://api.telegram.org/bot902068419:AAFWBpfk-S8f-Ts7XA1wQqEw3TLTMst8nNg/sendMessage",
                  data={'chat_id': -284395075, 'text': message})
#514530890
def get_paid_plugins():
    list_plugins = []
    list_index = []
    exp_urls =[]
    n = 0
    #url = 'http://10.6.211.178/jira/rest/plugins/1.0/com.onresolve.jira.groovy.groovyrunner-key/license'
    url = 'http://10.6.211.178/jira/rest/plugins/1.0/'
    #data = {'body': 'Это здорово'}
    response = requests.get(url, auth=('admin', 123456))
    print('Return code: ' + str(response.status_code) + '\n')
    dec = response.content.decode('UTF-8')
    parsed_string = json.loads(dec)
    parsed = json.dumps(parsed_string, indent=4)
    #print(parsed)
    count = len(parsed_string['plugins'])

    if count == 0:
        print('No plugins')

    else:
        for n in range(count):
            if parsed_string['plugins'][n]['usesLicensing'] == True:
                list_index.append(n)
                n +=1

        for i in list_index:

            exp_urls.append(parsed_string['plugins'][i]['links']['delete'])
    #print(exp_urls)
    get_exp_date(exp_urls)



get_paid_plugins()



