import requests

client_id = "y25R7Si0cQFdrTqpwoD"
file_name= "zalando1.csv"

headers = {

    'x-api-key': "GusfAW9hKrR4QEDQ7ck3zIhYgEqTduLi3Ce8kSZi",
    'content-type': "application/csv",
    'cache-control': "no-cache"
    
}

with open('zalando1.csv', 'rb') as f:

    res = requests.put(f"https://merchants-connector-importer.zalandoapis.com/{client_id}/validate".format(client_id=client_id), headers=headers, data=f.read())

    print(res.json())

    if res.status_code == 200:

        print("Success validate")

        res = requests.put(f"https://merchants-connector-importer.zalandoapis.com/{client_id}/{file_name}".format(client_id=client_id), headers=headers, data=f.read())

        if res.status_code == 200:

            print("Success update")

        else:

            print("Failed validate")
            print(res.json())

    else:

        print("Failed validate")