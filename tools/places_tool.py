import pandas as pd

# LOAD DATASET

df = pd.read_excel("data/places.xlsx")


# =====================================================
# PLACES SEARCH TOOL
# =====================================================

def places_search(query):

    query = query.lower()

    results = df.copy()

    # FILTER CITY

    cities = df["city"].str.lower().unique()

    for city in cities:

        if city in query:

            results = results[
                results["city"].str.lower() == city
            ]

    # FILTER TYPE

    types = df["type"].str.lower().unique()

    matched_type = False

    for t in types:

        if t in query:

            results = results[
                results["type"].str.lower() == t
            ]

            matched_type = True

    # TOP RATED

    results = results.sort_values(by="rating", ascending=False)

    if results.empty:

        return "No matching places found."

    output = "\nTOURIST PLACES:\n"

    for _, row in results.head(5).iterrows():

        output += f"""

Place ID: {row['place_id']}
Place Name: {row['name']}
City: {row['city']}
Type: {row['type']}
Rating: {row['rating']}

"""

    return output