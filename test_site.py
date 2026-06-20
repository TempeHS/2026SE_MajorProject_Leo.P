import pytest
import requests

URL = "http://localhost:8000"

# def test_local_website_is_up():
#     url = URL
#     response = requests.get(url, timeout=5)

#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"

### sprint 1unit test
# @pytest.mark.parametrize(
#     "path",
#     [
#         "/",
#         "/about",
#         "/resources",
#         "/privacy",
#         "/login.html",
#         "/signup.html",
#         "/past_papers",
#         "/useful_websites",
#         "/personal_dashboard",
#     ],
# )
# def test_pages_are_up(path):
#     response = requests.get(f"{URL}{path}", timeout=5)

#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"


### sprint 2 unit test
# @pytest.mark.parametrize(
#     "path",
#     [
#         "/subject/hsie/business-studies",
#         "/subject/hsie/business-studies/past-papers",
#         "/resources",
#         "/login.html",
#         "/signup.html",
#     ],
# )
# def test_pages_are_up(path):
#     response = requests.get(f"{URL}{path}", timeout=5)

#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"


### sprint 3 test
@pytest.mark.parametrize(
    "path",
    [
        "/subject/hsie/business-studies/notes/operations",
        "/subject/hsie/business-studies/videos/operations",
    ],
)
def test_pages_are_up(path):
    response = requests.get(f"{URL}{path}", timeout=5)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
