from DevilWearsPrada.pages import Bags_page
from DevilWearsPrada.lib import helpers
from DevilWearsPrada.testdata import test_data


def test_check_shoulder_bags_total_for_women():
    # helpers.go_to_page(test_data.prada_bags_page_url)
    # Bags_page.navigate_to_women_shoulder_bags_and_check_total()
    Bags_page.navigate_to_women_shoulder_bags_and_check_total_via_api()


if __name__ == '__main__':
    test_check_shoulder_bags_total_for_women()
