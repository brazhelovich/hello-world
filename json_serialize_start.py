# Process JSON data returned from a server

# TODO: user the JSON module
import json

def main():
    # define a string of JSON code
    pythonData = {'sandwich': 'Reuben', 'toasted': 'true', 'toppings': ['Thousend Island Dressing', 'Sauerkraut', 'Pickeles'], 'price': 8.99}
    #TODO: srialize to JSON using dumps
    jsonString = json.dumps(pythonData, indent=4)


    # TODO: print the resulting dumps
    print(type(jsonString))
    print('JSON Data: ----------')
    print(jsonString)



main()
