# using urllib to request data

# TODO: import the urllib request class
import urllib.request
import urllib.parse

def main():
# the URL to retrieve our sample data from
    url = 'http://httpbin.org/get'



    # TODO: create some data to pass to the GET request
    args = {
        'name': 'Andrei Brazhalovich',
        'is_author': True}


    # TODO: the data needs to be url-encoded before passing as arguments
    data = urllib.parse.urlencode(args)
    # TODO: issue the request with the data params as part of the URL
    #result = urllib.request.urlopen(url + '?' +  data)
    # TODO: issue the request with the data parameter to use POST
    url = 'http://httpbin.org/post'
    data = data.encode()
    result = urllib.request.urlopen(url, data=data)


    print('Result code:{0}'.format(result.status))
    print('Returned data: -----------------------')
    print(result.read().decode('utf-8'))

if __name__ == '__name__':
    main()
main()
