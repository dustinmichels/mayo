import requests
from bs4 import BeautifulSoup


def extract_divs(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    # Print response details for debugging
    print(f"Status Code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(
        f"Response Text (First 500 chars): {response.text[:500]}"
    )  # Print only first 500 characters

    response.raise_for_status()  # Raise an error for bad responses

    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", class_="ch-search-result")

    for div in divs:
        print(div.get_text(strip=True))


# Example usage
url = "https://connect.mayoclinic.org/search/?search=vonoprazan"
extract_divs(url)
