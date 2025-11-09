# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "SK": "South Korea",
    "NK": "North Korea",

}
try:
    print(country_codes["PH"])
except KeyError:
    print("Country not found")

