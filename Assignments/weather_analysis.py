import statistics

# Sample weather data for last 10 days
# Format: (Temperature °C, Humidity %, AQI)
weather_data = [
    (28.5, 62, 110),
    (30.2, 58, 125),
    (29.8, 60, 118),
    (31.1, 55, 135),
    (30.0, 59, 121),
    (28.9, 61, 115),
    (29.2, 60, 119),
    (30.5, 57, 130),
    (29.7, 59, 122),
    (30.1, 58, 117),
]

temperatures = [temp for temp, _, _ in weather_data]
humidities = [hum for _, hum, _ in weather_data]
aqi_values = [aqi for _, _, aqi in weather_data]

def compute_stats(data):
    return {
        "average": round(statistics.mean(data), 2),
        "median": round(statistics.median(data), 2),
    }

temp_stats = compute_stats(temperatures)
hum_stats = compute_stats(humidities)
aqi_stats = compute_stats(aqi_values)

print("Temperature Stats:", temp_stats)
print("Humidity Stats:", hum_stats)
print("AQI Stats:", aqi_stats)

# Save results to a file
with open("analysis_results.txt", "w") as f:
    f.write("Weather Analysis for Gandhinagar (Last 10 Days)\n\n")
    f.write(f"Temperature -> {temp_stats}\n")
    f.write(f"Humidity -> {hum_stats}\n")
    f.write(f"AQI -> {aqi_stats}\n")
