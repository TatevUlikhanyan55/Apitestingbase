base_url="https://www.prada.com/"
view_all_women_bags = base_url + "ww/en/women/bags.glb.getProductGridFilter.json?category=3074457345616749193&facets=&withOutLifeCycle=true"
reqres_base = "https://reqres.in/"
create_user_reqres_in = reqres_base + "api/users"

def get_user_reqres_in(user_id):
    get_user_reqres_in = reqres_base + "api/users/" +f"{user_id}"
    return get_user_reqres_in