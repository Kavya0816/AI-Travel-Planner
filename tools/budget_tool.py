import pandas as pd


# =========================================================
# LOAD DATASETS
# =========================================================

flights_df = pd.read_excel("data/flights.xlsx")
hotels_df = pd.read_excel("data/hotels.xlsx")


# =========================================================
# BUDGET CALCULATOR
# =========================================================


def budget_calculator(flight_price, hotel_price, days=1):

    hotel_total = hotel_price * days

    food_cost = days * 800

    local_transport = days * 500

    total = (
        flight_price
        + hotel_total
        + food_cost
        + local_transport
    )

    return f"""
BUDGET ESTIMATION

Flight Cost: ₹{flight_price}

Hotel Cost ({days} nights): ₹{hotel_total}

Food Cost: ₹{food_cost}

Local Transport: ₹{local_transport}

--------------------------------

TOTAL ESTIMATED COST: ₹{total}
"""