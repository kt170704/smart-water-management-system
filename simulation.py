import numpy as np
import random
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Simulate water level (in cm)
def simulate_water_level():
    return random.randint(5, 50)

# Generate data (for training)
def generate_data(num_samples=100):
    water_levels = [simulate_water_level() for _ in range(num_samples)]
    flow_rates = [np.random.uniform(0, 10) for _ in range(num_samples)]  # Simulate flow rates
    return np.array(water_levels), np.array(flow_rates)

# Train a Linear Regression model
def train_model():
    # Generate data
    water_levels, flow_rates = generate_data(100)
    
    # Prepare features and target
    X = flow_rates.reshape(-1, 1)  # Flow rate as the feature
    y = water_levels  # Water level as the target

    # Train the model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

# Predict future water levels
def predict_water_level(model, flow_rate):
    predicted_level = model.predict([[flow_rate]])
    return predicted_level[0]

# Plot the data and prediction line
def plot_data(water_levels, flow_rates, model):
    plt.scatter(flow_rates, water_levels, color='blue', label='Data')
    
    # Predict values
    predicted_levels = model.predict(flow_rates.reshape(-1, 1))
    plt.plot(flow_rates, predicted_levels, color='red', label='Regression Line')
    
    plt.xlabel('Flow Rate (L/min)')
    plt.ylabel('Water Level (cm)')
    plt.legend()
    plt.show()

# Main function
if __name__ == '__main__':
    # Train the model
    model = train_model()

    # Simulate and predict
    flow_rate = 5  # Example flow rate
    predicted_level = predict_water_level(model, flow_rate)
    print(f"Predicted water level for flow rate {flow_rate} L/min: {predicted_level:.2f} cm")

    # Plotting the data
    water_levels, flow_rates = generate_data(100)
    plot_data(water_levels, flow_rates, model)
