import pandas as pd

# LOAD DATASET

df = pd.read_excel("data/hotels.xlsx")


# =====================================================
# HOTEL SEARCH TOOL
# =====================================================

def hotel_search(query):

    query = query.lower()

    city_found = None

    cities = df["city"].str.lower().unique()

    for city in cities:

        if city in query:

            city_found = city
            break

    if city_found:

        results = df[
            df["city"].str.lower() == city_found
        ]

    else:

        results = df

    # BREAKFAST FILTER

    if "breakfast" in query:

        results = results[
            results["amenities"].str.lower().str.contains("breakfast", na=False)
        ]

    # BUDGET FILTER

    if "budget" in query:

        results = results.sort_values(by="price_per_night")

    if results.empty:

        return "No matching hotels found."

    output = "\nAVAILABLE HOTELS:\n"

    for _, row in results.head(5).iterrows():

        output += f"""

Hotel ID: {row['hotel_id']}
Hotel Name: {row['name']}
City: {row['city']}
Stars: {row['stars']}
Price Per Night: ₹{row['price_per_night']}
Amenities: {row['amenities']}

"""

    return output