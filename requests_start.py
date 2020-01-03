import requests

def main():
    # TODO: Use requests to issue a atandart HTTP GET request
    url = 'http://httpbin.org/xml'
    result = requests.post(url)
   # printResults(result)

    # TODO: Send some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding
    url = 'http://httpbin.org/post'
    dataValues = {
        'key1': 'value1',
        'key2': 'value2'
    }
    result = requests.post(url, data=dataValues)
    #printResults(result)

    # TODO: Pass custom header to the server
    url = 'http://httpbin.org/get'
    headerValues = {
        'User-Agent': 'Andrei Brazhalovich App / 1.1.1'
    }

    result = requests.get(url, headers=headerValues)
    printResults(result)


def printResults(resData):
    print('Result code: {0}'.format(resData.status_code))
    print('\n')

    print('Headers: ------------------------------------')
    print(resData.headers)
    print('\n')

    print('Returned data: --------------------------------------')
    print(resData.text)

main()
