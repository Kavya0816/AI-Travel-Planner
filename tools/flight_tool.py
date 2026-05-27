import pandas as pd

# LOAD DATASET

df = pd.read_excel("data/flights.xlsx")


# =====================================================
# FLIGHT SEARCH TOOL
# =====================================================

def flight_search(query):

    query = query.lower()

    results = df[
        df["from"].str.lower().str.contains(query.split("to")[0].strip(), na=False)
    ]

    if "to" in query:

        destination = query.split("to")[1].strip().split(" ")[0]

        results = results[
            results["to"].str.lower().str.contains(destination, na=False)
        ]

    if results.empty:

        return "No matching flights found."

    output = "\nAVAILABLE FLIGHTS:\n"

    for _, row in results.iterrows():

        output += f"""

Flight ID: {row['flight_id']}
Airline: {row['airline']}
From: {row['from']}
To: {row['to']}
Departure Time: {row['departure_time']}
Arrival Time: {row['arrival_time']}
Price: ₹{row['price']}

"""

    return output