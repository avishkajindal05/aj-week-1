import statistics

# Sample weather data for last 10 days
# Format: (Temperature, Humidity)
weather_data = [
    (28.5, 62),
    (30.2, 58),
    (29.8, 60),
    (31.1, 55),
    (30.0, 59),
    (28.9, 61),
    (29.2, 60),
    (30.5, 57),
    (29.7, 59),
    (30.1, 58),
]

temperatures = [temp for temp, _ in weather_data]
humidities = [hum for _, hum in weather_data]

def compute_stats(data):
    return {
        "average": round(statistics.mean(data), 2),
        "median": round(statistics.median(data), 2),
    }

# Compute
temp_stats = compute_stats(temperatures)
hum_stats = compute_stats(humidities)

print("Temperature Stats:", temp_stats)
print("Humidity Stats:", hum_stats)