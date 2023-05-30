import requests
import json


def make_post_request(url="", header="", json_body="", status_code=201):
    json.dumps(json_body)
    response = requests.post(url, json=json_body, headers=header)
    assert response.status_code == status_code
    return json.loads(response.text)

def make_post_request_with_auth(url ="", bearer="", json_body="", status_code=200):
    headers = {
                'Accept': 'application/json, text/plain',
                'Accept-Language': 'en-US,en;q=0.9',
                'Content-Type': 'application/json;charset=UTF-8',
                'authorization' : 'Bearer ' + bearer
               }
    json.dumps(json_body)
    response = requests.post(url, headers, json_body)
    assert response.status_code == status_code
    return json.loads(response.text)

