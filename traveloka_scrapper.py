import json
import requests
from datetime import datetime

url = "https://www.traveloka.com/api/v2/hotel/search/rooms"

date_format = '%d-%m-%Y'
dateIn = "20-02-2025"
dateOut = "21-02-2025"

inputs = {
    "dateIn": dateIn,
    "dateOut": dateOut,
    "nights": (datetime.strptime(dateOut, date_format) - datetime.strptime(dateIn, date_format)).days,
    "rooms": 1,
    "id": 9000001153383,
    "name": "novotel%20hua%20hin%20cha-am%20beach%20resort%20&%20spa",
    "numAdults": 1,
    "numChildren": 0
}

deep_link = f"https://www.traveloka.com/en-th/hotel/detail?spec={inputs['dateIn']}.{inputs['dateOut']}.{inputs['nights']}.{inputs['rooms']}.HOTEL.{inputs['id']}.{inputs['name']}.{inputs['numAdults']+inputs['numChildren']}"

headers = {
    "Host": "www.traveloka.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept": "*/*",
    "Accept-Language": "uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.traveloka.com/en-th/hotel/detail?spec=20-02-2025.21-02-2025.1.1.HOTEL.9000001153383.novotel%20hua%20hin%20cha-am%20beach%20resort%20&%20spa.2",
    "x-domain": "accomRoom",
    "content-type": "application/json",
    "x-route-prefix": "en-th",
    "Origin": "https://www.traveloka.com",
    "Connection": "keep-alive",
    "Cookie": 'tvl=shWhEo3ys9vvqKl8UReriqLuopMThxDyMNrsgk7vc3JPfwuGWqfXwnZzQFLuYY9W8n4/8e807LE3/0jDaeqHSx41J2bM8HlZQcXYxHlL9ebueOYS+JBldjBIzOEBd+XhEvZaeUoayLDR4daFxQe60wP/UYWhpmhovlolXt4IRGVUWyky44a0k+SVp6v9VZLdOReBDLY6p76RosokEdhzyDFEjvVKN64uzwjgYpPlXjRfEbZQA4ddUCyd/Y+qB8MawAevqaAkFiA=~djAy; countryCode=UA; _gcl_au=1.1.829386284.1739301309; amp_1a5adb=2Vih_dJzkjoiPwIFUDHrJJ...1ik0g5gi4.1ik0gdvic.9o.8.a0; amp_f4354c=s6_FA11e_x2OD1D7KhcGhm...1ik0g5gi5.1ik0gdvid.0.8.8; _ga_RSRSMMBH0X=GS1.1.1739478711.21.1.1739478989.3.0.1234583186; _ga=GA1.2.677976467.1739301309; _gid=GA1.2.1335701736.1739301310; cto_bundle=xFqwWF9SJTJCeTg2RlNDZ1RCNkZJM3oxWXdqbG9sYVpjakxnR3VRRVZXJTJGSGlnczZKMzZBeUdxWGpPUEg5Q2JheGQ4akxMRjBqY20yN0k0QUpFcmdNWSUyRnIyOFloYlZycEtkZ3NIZ1ppTU5pRFdtZFJaQXZnbFFLZ0k4TkJyMGNDUUM4OUlCciUyQmFJNU5zcUx0NVR3YyUyRnZuY1JVcEdnJTNEJTNE; _tt_enable_cookie=1; _ttp=NWscD7zniVCdFlha1hNeR82OU5t.tt.1; _cs_ex=1738719462; g_state={"i_p":1740048417195,"i_l":3}; tvs=iLUAhPnm30e1dacnLOSuBJ168NtdaZdtV/fROEjHDUZQOy+e9a26bGqmpv2qjYjPgPh32VaPQSQPiJmM0DxX1iI7blGR0ziKXEDJAs2990kdA4/qx9/6oqiZlfbtVujLgFjoqqnmGj6wFVepEP6WXAKhIltx5ehmE+a1a/acjJdRKJnWSCvfvTtGJwJi6dXtkQyH9EZIYN+uENUEZm1NHSYDIS9ekdeGrLvTTQY5fvfACTsQOLUokJ2owSTGDXA7W7IOXxrZBJSHtCb9AN+nUeER7OFoaCtWbAs=~djAy; tv-repeat-visit=true; tv_user={"authorizationLevel":100,"id":null}; accomSearchbarVariant=newDesign; _dd_s=rum=0&expire=1739479890246&logs=1&id=2ac58e10-d537-428f-a5d2-0d1111087db8&created=1739471486278; _cs_c=1; aws-waf-token=25a802a4-eb85-45f1-9480-a40bf14472c6:DQoAaiKQlOUEAAAA:g/7Eu0EcQAmn8axEZC/st4YjkXatklYd8FUKUt1kfvf7OPKLLDmn2PA1P+xWbu2Pzc/BGZrPaGe3zHC2HCe3GAji7mmL7Uz1+ur5sawtd8PKo+fWmzZptlJaFwhnNz/xatRXwVm7aJlwxgEujpBVCr7ZNkLGHP6B0e9d+rynnpkoWJPrFSxLfOZi7nbmjARRsVk=; _gat_UA-29776811-12=1'
}

payload = {
    "fields": [],
    "data": {
        "contexts": {
            "bookingId": None,
            "sourceIdentifier": "HOTEL_DETAIL",
            "shouldDisplayAllRooms": False
        },
        "prevSearchId": "undefined",
        "numInfants": 0,
        "ccGuaranteeOptions": {
            "ccInfoPreferences": ["CC_TOKEN", "CC_FULL_INFO"],
            "ccGuaranteeRequirementOptions": ["CC_GUARANTEE"]
        },
        "rateTypes": ["PAY_NOW", "PAY_AT_PROPERTY"],
        "isJustLogin": False,
        "isReschedule": False,
        "preview": False,
        "monitoringSpec": {
            "lastKeyword": "novotel hua hin cha-am beach resort",
            "referrer": "",
            "isPriceFinderActive": "null",
            "dateIndicator": "null",
            "displayPrice": "null"
        },
        "hotelId": "9000001153383",
        "currency": "THB",
        "labelContext": {},
        "isExtraBedIncluded": True,
        "hasPromoLabel": False,
        "supportedRoomHighlightTypes": ["ROOM"],
        "checkInDate": {"day": dateIn[:2], "month": dateIn[3:5], "year": dateIn[6:]},
        "checkOutDate": {"day": dateOut[:2], "month": dateOut[3:5], "year": dateIn[6:]},
        "numOfNights": inputs["nights"],
        "numAdults": inputs["numAdults"],
        "numRooms": inputs["rooms"],
        "numChildren": inputs["numChildren"],
        "childAges": [],
        "tid": "5a5eb6a6-eab8-4fa9-8490-4a3edc4de80c"
    },
    "clientInterface": "desktop"
}

session = requests.Session()
session.headers.update(headers)

response = session.post(url, json=payload, headers=headers)


if response.status_code == 200:
    try:
        response_content = response.content
        if response.headers.get('Content-Encoding') == 'br':
            response_content = response.content.decode('utf-8')
        else:
            response_content = response.text
    except Exception as e:
        print(f"Error during decompression: {e}")
        response_content = None
else:
    print(f"Failed request: {response.status_code}")

json_data = json.loads(response_content)

### Uncomment to save full json (approx. 250KB)
# with open("hotel_data.json", "w", encoding="utf-8") as f:
#     json.dump(json_data, f, indent=4, ensure_ascii=False)

def parse_hotel_data(json_data, guest_num):
    rates = []
    
    for entry in json_data.get("data", {}).get("recommendedEntries", []):
        room_name = entry.get("name", "Unknown Room")
        
        for inventory in entry.get("hotelRoomInventoryList", []):
            rate_name = inventory.get("inventoryName", "Unknown Rate")
            rate_display = inventory.get("rateDisplay", {})
            final_price = inventory.get("finalPrice", {}).get("totalPriceRateDisplay", {})
            per_room_display = inventory.get("finalPrice", {}).get("perRoomPerNightDisplay", {})
            final_strikethrough = inventory.get("finalStrikethroughPrice", {}).get("perRoomPerNightDisplay", {})
            
            rates.append({
                "room_name": room_name,
                "rate_name": rate_name,
                "shown_currency": rate_display.get("baseFare", {}).get("currency", "Unknown"),
                "shown_price": str(float(rate_display.get("baseFare", {}).get("amount", 0)) / 100.0),
                "net_price": str(float(final_price.get("baseFare", {}).get("amount", 0)) / 100.0),
                "cancellation_policy": inventory.get("roomCancellationPolicy", {}).get("refundable", False),
                "breakfast": inventory.get("isBreakfastIncluded", False),
                "number_of_guests": guest_num,
                "taxes_amount": str(float(rate_display.get("taxes", {}).get("amount", 0)) / 100.0),
                "total_price": str(float(final_price.get("totalFare", {}).get("amount", 0)) / 100.0),
                "original_price": str(float(final_strikethrough.get("baseFare", {}).get("amount", 0)) / 100.0),
                "shown_price_per_stay": str(float(per_room_display.get("baseFare", {}).get("amount", 0)) / 100.0),
                "net_price_per_stay": str(float(per_room_display.get("baseFare", {}).get("amount", 0)) / 100.0),
                "total_price_per_stay": str(float(per_room_display.get("totalFare", {}).get("amount", 0)) / 100.0),
            })
    
    return {"rates": rates}


parsed_data = parse_hotel_data(json_data, inputs["numAdults"] + inputs["numChildren"])

with open("parsed_hotel_rates.json", "w", encoding="utf-8") as output_file:
    json.dump(parsed_data, output_file, indent=4, ensure_ascii=False)

print(deep_link)