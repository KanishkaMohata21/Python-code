import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID=""

pixela_endpoint = "https://pixe.la/v1/users"
pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id":GRAPH_ID,
    "name": "Coding graph",
    "unit": "hrs",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today=datetime.now()

pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many hours did you code today??\n")
}

# response=requests.post(url=pixel_creation_endpoint,json=pixel_params,headers=headers)
# print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20231112"
new_pixel_data={
    "quantity":"10"
}

# response=requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
# print(response.text)

# delete_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20231111"
# requests.delete(url=delete_endpoint,headers=headers)