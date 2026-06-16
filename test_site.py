import pytest
import requests

URL = "http://localhost:8000"

# def test_local_website_is_up():
#     url = URL
#     response = requests.get(url, timeout=5)

#     assert response.status_code == 200, f"Expected 200, got {response.status_code}"


@pytest.mark.parametrize(
    "path",
    [
        "/",
        "/about",
        "/resources",
        "/privacy",
        "/login.html",
        "/signup.html",
        "/past_papers",
        "/useful_websites",
        "/personal_dashboard",
    ],
)
def test_pages_are_up(path):
    response = requests.get(f"{URL}{path}", timeout=5)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
