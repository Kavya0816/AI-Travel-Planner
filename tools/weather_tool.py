import requests


# =====================================================
# CITY COORDINATES
# =====================================================

city_coordinates = {

    "goa": {
        "latitude": 15.2993,
        "longitude": 74.1240
    },

    "delhi": {
        "latitude": 28.6139,
        "longitude": 77.2090
    },

    "mumbai": {
        "latitude": 19.0760,
        "longitude": 72.8777
    },

    "hyderabad": {
        "latitude": 17.3850,
        "longitude": 78.4867
    },

    "bangalore": {
        "latitude": 12.9716,
        "longitude": 77.5946
    },

    "chennai": {
        "latitude": 13.0827,
        "longitude": 80.2707
    },

    "kolkata": {
        "latitude": 22.5726,
        "longitude": 88.3639
    }
}


# =====================================================
# WEATHER TOOL
# =====================================================

def weather_tool(city):

    try:

        city = city.lower().strip()

        # CHECK CITY

        if city not in city_coordinates:

            return f"No weather data available for {city}"


        latitude = city_coordinates[city]["latitude"]

        longitude = city_coordinates[city]["longitude"]


        # =====================================================
        # OPEN METEO API
        # =====================================================

        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}"
            f"&longitude={longitude}"
            f"&daily=temperature_2m_max,"
            f"temperature_2m_min,"
            f"precipitation_sum"
            f"&timezone=auto"
        )


        # API REQUEST

        response = requests.get(url)

        data = response.json()


        daily = data["daily"]


        # =====================================================
        # FORMAT OUTPUT
        # =====================================================

        output = f"\nWEATHER FORECAST FOR {city.upper()}\n"


        for i in range(3):

            output += f"""

Day {i + 1}

Maximum Temperature:
{daily['temperature_2m_max'][i]} °C

Minimum Temperature:
{daily['temperature_2m_min'][i]} °C

Rainfall:
{daily['precipitation_sum'][i]} mm

"""


        return output


    except Exception as e:

        return f"Weather Tool Error: {e}"


# =====================================================
# TESTING
# =====================================================

if __name__ == "__main__":

    print(weather_tool("Delhi"))