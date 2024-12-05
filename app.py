import time
import numpy as np
from flask import Flask, render_template, jsonify
from threading import Thread
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import random

# Flask setup
app = Flask(__name__)

# Simulate water level and flow rate
def simulate_water_level():
    return random.randint(5, 50)

def simulate_flow_rate():
    return np.random.uniform(0, 10)

# Data storage for plotting
water_levels = []
flow_rates = []

# Function to simulate data periodically
def simulate_data():
    while True:
        water_levels.append(simulate_water_level())
        flow_rates.append(simulate_flow_rate())
        if len(water_levels) > 100:
            water_levels.pop(0)
            flow_rates.pop(0)
        time.sleep(1)

# Route to serve the dashboard
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route to fetch simulated data for the dashboard
@app.route('/data')
def data():
    return jsonify({
        'water_levels': water_levels,
        'flow_rates': flow_rates
    })

# Route to generate the water level chart
@app.route('/chart')
def chart():
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot water levels
    ax.plot(water_levels, label='Water Level (cm)', color='blue')
    ax.set_title('Water Level Over Time')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Water Level (cm)')
    ax.legend()

    # Save to BytesIO and encode as base64
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close(fig)

    return f'<img src="data:image/png;base64,{img_base64}"/>'

if __name__ == "__main__":
    # Start the data simulation in a separate thread
    thread = Thread(target=simulate_data)
    thread.daemon = True
    thread.start()

    app.run(debug=True)
