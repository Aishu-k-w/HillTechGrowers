from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import pandas as pd
import requests

app = Flask(__name__)
app.secret_key = 'smart_agriculture_2025_sikkim'

# ------------------ CONFIG ------------------
API_KEY = "a8833213c3647ad53e97b2d30ff7c4ef"  # replace with your OpenWeather key
CITY = "Jorethang"

# Demo user credentials
USERS = {'admin': 'agriculture2025'}

# ------------------ LOAD CROPS DATA ------------------
CROPS_DF = pd.read_csv("cropsnew.csv")

# ------------------ DATA FUNCTIONS ------------------
def get_weather_data():
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return {
            'temperature': round(weather_data["main"]["temp"]),
            'humidity': round(weather_data["main"]["humidity"]),
            'rainfall': round(weather_data.get("rain", {}).get("1h", 0), 1),
            'wind_speed': round(weather_data["wind"]["speed"])
        }
    except Exception as e:
        print("Weather API error:", e)
        # fallback static values
        return {'temperature': 22, 'humidity': 70, 'rainfall': 0, 'wind_speed': 5}

def get_soil_data():
    return {'ph': 6.5, 'moisture': 60, 'temperature': 22, 'nutrients': 'Optimal'}

def get_irrigation_data():
    return {'schedule': 'Active', 'next_watering': '14:30', 'duration': 25, 'pressure': 2.8}

def get_tank_level():
    return 100

def get_crops_from_csv(weather, soil):
    try:
        # Filter by temperature
        suitable = CROPS_DF[
            (CROPS_DF["Min Temp"] <= weather["temperature"]) &
            (CROPS_DF["Max temp"] >= weather["temperature"])
        ]

        # Categorize soil moisture
        if soil["moisture"] < 40:
            soil_condition = "Low"
        elif 40 <= soil["moisture"] <= 70:
            soil_condition = "Medium"
        else:
            soil_condition = "High"

        # Filter based on Soil Moisture column
        suitable = suitable[suitable["Soil Moisture"].str.contains(soil_condition, case=False, na=False)]

        # Convert to list of dicts
        crops_list = suitable.to_dict(orient="records")
        return crops_list
    except Exception as e:
        print("Error in crop filter:", e)
        return []

# ------------------ ROUTES ------------------
@app.route('/')
def login():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if username in USERS and USERS[username] == password:
        session['user'] = username
        return redirect(url_for('dashboard'))
    return render_template('login.html', error='Invalid credentials. Use admin/agriculture2025')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))

    soil = get_soil_data()
    weather = get_weather_data()
    recommended_crops = get_crops_from_csv(weather, soil)

    data = {
        'soil': soil,
        'weather': weather,
        'irrigation': get_irrigation_data(),
        'tank_level': get_tank_level(),
        'current_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'crops': recommended_crops,
        'soil_category': "Medium"  # added for dashboard.html display
    }
    return render_template('dashboard.html', data=data)

@app.route('/crops')
def crops():
    if 'user' not in session:
        return redirect(url_for('login'))

    soil = get_soil_data()
    weather = get_weather_data()
    recommended_crops = get_crops_from_csv(weather, soil)

    return render_template(
        'crops.html',
        soil=soil,
        weather=weather,
        crops=recommended_crops,
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )


@app.route("/crop_recommendation", methods=["GET", "POST"])
def crop_recommendation():
    # Soil categories exactly as you listed
    soil_types = ["Clayey", "Well-drained", "Loamy", "Sandy", "Medium fertility", "High organic", "Alluvial"]

    selected_soil = None
    filtered_crops = []

    # Get current weather and soil data
    weather = get_weather_data()
    soil_data = get_soil_data()

    if request.method == "POST":
        selected_soil = request.form.get("soil_type")
        if selected_soil:
            # Filter crops by selected soil type
            suitable = CROPS_DF[
                (CROPS_DF["Soil Type"].str.strip().str.lower() == selected_soil.lower()) &
                (CROPS_DF["Min Temp"] <= weather["temperature"]) &
                (CROPS_DF["Max temp"] >= weather["temperature"])
                ]

            # Filter by soil moisture category
            if soil_data["moisture"] < 40:
                soil_condition = "Low"
            elif 40 <= soil_data["moisture"] <= 70:
                soil_condition = "Medium"
            else:
                soil_condition = "High"

            suitable = suitable[suitable["Soil Moisture"].str.contains(soil_condition, case=False, na=False)]
            filtered_crops = suitable.to_dict(orient="records")

    return render_template(
        "crops.html",
        soil_types=soil_types,  # Dropdown categories
        selected_soil=selected_soil,  # Selected option remains selected
        crops=filtered_crops,
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# Placeholder routes
@app.route('/graphs')
def graphs():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('graphs.html')

@app.route('/alerts')
def alerts():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('alerts.html')

@app.route('/api/water_control', methods=['POST'])
def water_control():
    action = request.json.get('action')
    return jsonify({'status': 'success', 'action': action})

# ------------------ MAIN ------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
