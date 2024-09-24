import requests

url = "https://irctc1.p.rapidapi.com/api/v3/getPNRStatus"

def check_pnr_status(pnr_number):

    querystring = {"pnrNumber":pnr_number}

    headers = {
        "x-rapidapi-key": "fc538a48eemshb0c33dfbc9e41b4p1f97a2jsndc77183af7da",
        "x-rapidapi-host": "irctc1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        print("Response Data:", data)

        # Check if critical fields exist to determine PNR validity
        pnr_data = data.get("data", {})
        pnr_number_in_response = pnr_data.get("Pnr")
        train_no = pnr_data.get("TrainNo")
        passenger_status = pnr_data.get("PassengerStatus", [])

        if pnr_number_in_response and train_no and passenger_status:
            # PNR exists and contains passenger status information
            print(f"PNR {pnr_number} is valid.")
            return True
        else:
            # Critical data is missing; assume PNR is invalid
            print(f"PNR {pnr_number} is invalid.")
            return False
    else:
        print("Failed to retrieve PNR status:", response.status_code, response.text)
        return False