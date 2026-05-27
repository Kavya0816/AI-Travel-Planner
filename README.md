# ✈️ AI Travel Planner

An AI-powered travel planning system built using LangChain, OpenAI, Streamlit, and travel datasets.

This application generates intelligent travel plans by analyzing:

* Flights
* Hotels
* Tourist attractions
* Weather forecasts
* Estimated travel budget

The project uses LangChain agents and multiple custom tools to create personalized trip recommendations.

---

# 🚀 Features

* AI-powered travel itinerary generation
* Flight recommendation system
* Hotel recommendation system
* Tourist attraction suggestions
* Live weather forecasting using Open-Meteo API
* Budget estimation
* Streamlit interactive dashboard
* LangChain agent-based architecture
* Dataset-driven recommendations

---

# 🛠️ Technologies Used

* Python
* LangChain
* OpenAI API
* Streamlit
* Pandas
* Open-Meteo API
* Excel datasets

---

# 📂 Project Structure

```bash
AI_Travel_Planner/
│
├── agent/
│   └── travel_agent.py
│
├── tools/
│   ├── flight_tool.py
│   ├── hotel_tool.py
│   ├── places_tool.py
│   ├── weather_tool.py
│   └── budget_tool.py
│
├── datasets/
│   ├── flights.xlsx
│   ├── hotels.xlsx
│   └── places.xlsx
│
├── screenshots/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/AI-Travel-Planner.git
```

---

## 2. Open Project

```bash
cd AI-Travel-Planner
```

---

## 3. Create Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Add OpenAI API Key

Create `.env`

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧠 Example Prompt

```text
Plan a 3 day trip from Hyderabad to Delhi on 2025-01-04 with budget hotel, breakfast, lakes and temples
```

---

# 📸 Screenshots

## Homepage

Add screenshot here.

## Generated Travel Plan

Add screenshot here.

---

# 🔮 Future Improvements

* Google Maps integration
* Hotel image support
* Real-time flight APIs
* PDF itinerary export
* User authentication
* Voice-based travel assistant
* Multi-city trip planning

---

# 👨‍💻 Author

Kavya Taneja
IIT Madras
Manufacturing Engineering Student | AI & Data Science Enthusiast
