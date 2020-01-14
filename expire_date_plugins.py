import requests
import json
import sys
from datetime import timedelta
from datetime import datetime
#from easygui import passwordbox


def get_exp_date(expire):
    message = []
    now = (datetime.now())

    for link in expire:

        url_exp = 'http://10.6.211.178' + link + '/license'
        #print(url_exp)
        response = requests.get(url_exp, auth=('admin', 123456), verify=False)

        dec = response.content.decode('UTF-8')
        parsed_string = json.loads(dec)
        result = json.dumps(parsed_string, indent=4)
        form = datetime.strptime(str(parsed_string['expiryDateString']), '%d/%b/%y')
        count_days = form - now

        expired = 'Name of plugin: ' + str(parsed_string['pluginKey']).split('.')[-1] + '\nExpire date: ' + \
                  parsed_string['expiryDateString'] + '\nExpired: ' + str(abs(count_days.days)) + \
                  ' days\n===================='

        remaind = 'Name of plugin: ' + str(parsed_string['pluginKey']).split('.')[-1] + '\nExpire date: ' + \
                  parsed_string['expiryDateString'] + '\nRemained: ' + str(count_days.days) +\
                  ' days\n===================='

        #printparsed_string['expiryDateString']


        if count_days.days < 0:
            print(expired)
            message.append(expired)

        elif count_days.days < 8:
            print(remaind)
            message.append(remaind)
            #else:
            #print('No problem with licenses')

    print('\nReturn code: ' + str(response.status_code) + '\n')

    notify_telegram('\n'.join(message))
    slack_notify('\n'.join(message))



def slack_notify(probe):
    data = {'text': probe}
    response = requests.post('https://hooks.slack.com/services/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', json=data)
    print('Message sent to Slack')



def notify_telegram(message):
    # !/usr/bin/env python
    requests.post("https://api.telegram.org/bot902068419:AAFWBpfk-S8f-Ts7XA1wQqEw3TLTMst8nNg/sendMessage",
                  data={'chat_id': -284395075, 'text': message})
    print('Message sent to Telegram')
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



