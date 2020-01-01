import pytest
import requests

url = "http://127.0.0.1:8000/"

def test1():
    res = requests.request(url+"post_location/?lat=68.1&lng=68.1&pincode=IN/600010&address=lalpat ganj&city=delhi")
    js = {
        'id' : 110001
        'key' : "IN/600010",
        'place_name' : "lalpat ganj",
        'admin_name1' : 'delhi',
        'latitude' : 68.1,
        'longitude' : 68.1,
        'accuracy' : '',
    }

    if js == res:
        print("Data is saved")
    else:
        print("data is not save or response problem")
    

def test2():
    res = requests.request(url+"get_location/?lat=68.1&lng=68.1")
    js = {
        'id' : 110001
        'key' : "IN/600010",
        'place_name' : "lalpat ganj",
        'admin_name1' : 'delhi',
        'latitude' : 68.1,
        'longitude' : 68.1,
        'accuracy' : '',
    }

    if js == res:
        print("we get right data")
    else:
        print("not geting right data response")

def test3():
    res1 = requests.request(url+"get_using_postgres/?lat=68.1&lng=68&radius=50")
    res2 = requests.request(url+"get_using_self/?lat=68.1&lng=68&radius=50")
    

    if res1 == res2:
        print("Both are returning save json data")
    else:
        print("they are not returning same data")
        

test1()
test2()
test3()
