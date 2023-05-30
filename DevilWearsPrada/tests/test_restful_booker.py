from DevilWearsPrada.lib.requests.post_requests import make_post_request, make_post_request_with_auth

from DevilWearsPrada.lib import endpoints
from DevilWearsPrada.lib import payloads
from DevilWearsPrada.lib.requests.put_requests import make_put_request_with_auth

def get_token():
    token = make_post_request(endpoints.create_token_restful_booker,json_body=payloads.get_token(),status_code=200)
    return token

def test_update_user():
    token_dict = get_token()
    token = token_dict['token']
    update_user = make_put_request_with_auth(endpoints.update_user_restful_booker(), json_body=payloads.create_user_restful_booker(),bearer=token)
    updated_user_id = update_user['id']
    print(updated_user_id)
    return updated_user_id




if __name__ == '__main__':
    test_update_user()
