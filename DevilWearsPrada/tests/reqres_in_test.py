from DevilWearsPrada.lib.requests.delete_requests import make_delete_request
from DevilWearsPrada.lib.requests.post_requests import make_post_request
from DevilWearsPrada.lib.requests.get_requests import make_get_request
from DevilWearsPrada.lib import endpoints
from DevilWearsPrada.lib import payloads
from DevilWearsPrada.lib.requests.put_requests import make_put_request


def test_create_user():
    created_user = make_post_request(endpoints.create_user_reqres_in, json_body=payloads.create_user_reqres_in())
    created_user_id = created_user['id']
    print(created_user_id)
    return created_user_id

def test_get_created_user_and_check_name(expected_user_name="George"):
    user_id = 1
    user_credentials = make_get_request(endpoints.get_user_reqres_in(user_id))
    print(user_credentials)
    user_name = user_credentials['data']['first_name']
    print(user_name)
    assert user_name == expected_user_name

def test_update_created_user_name_and_check_it(expected_user_name="Garnik"):
    user_id = 2
    user_credentials = make_put_request(endpoints.get_user_reqres_in(user_id), json_body=payloads.update_user_reqres_in())
    user_name = user_credentials['name']
    print(user_name)
    assert user_name == expected_user_name

def test_delete_user_and_check_it():
    user_id = 2
    user_credentials = make_delete_request(endpoints.get_user_reqres_in(user_id))
    print(user_credentials)
    assert user_credentials == ""


if __name__ == '__main__':
    test_create_user()
    test_get_created_user_and_check_name(expected_user_name="George")
    test_update_created_user_name_and_check_it(expected_user_name="Garnik")
    test_delete_user_and_check_it()

