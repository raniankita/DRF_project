# this is a third party application which have no connection with the api project
# we are creating this to get the data from the api. in our case this is in python or it can be in any language.
import requests
# putting the url of our application here to which we have to sent the request
URL = "http://127.0.0.1:8000/studentinfo/"
# sending get request to the URL and also we get the response from it and we store it in r
r = requests.get(url = URL)
print('###########',r)
# here we are extractiong the data in the json format and store it in the data
data = r.json()
print(data)