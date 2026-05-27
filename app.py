import streamlit as st

from agent.travel_agent import generate_travel_plan


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("✈️ AI Travel Planner")

st.markdown("""
Plan smart trips using:
- AI
- LangChain
- OpenAI
- Weather API
- Travel Datasets
""")


# =========================================================
# USER INPUT
# =========================================================

user_input = st.text_area(

    "Enter your travel request:",

    placeholder="""
Example:
Plan a 3 day trip from Hyderabad to Delhi on 2025-01-04 with budget hotel, breakfast, lakes and temples
"""
)


# =========================================================
# BUTTON
# =========================================================

if st.button("Generate Travel Plan"):

    if user_input.strip() == "":

        st.warning("Please enter a travel request.")

    else:

        with st.spinner("Planning your trip..."):

            try:

                result = generate_travel_plan(user_input)

                st.success("Trip Plan Generated Successfully!")

                st.markdown("## 🌍 Your Travel Plan")

                st.write(result)

            except Exception as e:

                st.error(f"Error: {e}")