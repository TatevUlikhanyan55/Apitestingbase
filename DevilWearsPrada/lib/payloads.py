def create_user_reqres_in(name="Tat", job="QA"):
    create_user_reqrest = {
        "name": f"{name}",
        "job": f"{job}"
    }
    return create_user_reqrest


def update_user_reqres_in(updated_name="Garnik", job="DB_Specialist"):
    update_user_reqrest = {
        "name": f"{updated_name}",
        "job": f"{job}"
    }
    return update_user_reqrest


def get_token():
    token_body = {
        "username": "admin",
        "password": "password123"
    }
    return token_body


def create_user_restful_booker():
    create_user = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return create_user
