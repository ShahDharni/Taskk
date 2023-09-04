import requests
import json

URL="http://127.0.0.1:8000/studentapi/"
def get_data(id=None):
    data={}
    if id is not None:
      data={id:id}
    json_data=json.dumps(data)  # To convert python data into json data
    r=requests.get(url = URL, data=json_data) # To pass data by using GET method
    data=r.json() # To extract data
    print(data)

get_data()


def post_data():
    data={
        'name':'Jay',
        'roll' :90,
        'city':'Ahmedabad'
    }

    json_data=json.dumps(data)
    r=requests.post(url = URL, data=json_data) # To pass data by using POST method
    data= r.json() #To extract data
    print(data)

#post_data()

def update_data():
    data={
        'id':5,
        'name':'Honey',
        'city':'Ranchi'
    }

    json_data=json.dumps(data)
    r=requests.put(url = URL, data=json_data) # To pass data by using POST method
    data= r.json() #To extract data
    print(data)


#update_data()


def delete_data():
    data={'id':9}

    json_data=json.dumps(data)
    r=requests.delete(url = URL, data=json_data) # To pass data by using POST method
    data= r.json() #To extract data
    print(data)


# delete_data()


