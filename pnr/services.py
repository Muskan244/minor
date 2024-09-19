import requests

# Service function to check PNR status using external API
def check_pnr_status(pnr_number):
    url = "https://irctc1.p.rapidapi.com/api/v1/checkPNR"
    querystring = {"pnrNumber": pnr_number}

    headers = {
        "X-RapidAPI-Key": settings.RAPIDAPI_KEY,  # Store API key in settings
        "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("pnrStatus", {}).get("isValid", False)  # Adjust based on API response structure
    return False
