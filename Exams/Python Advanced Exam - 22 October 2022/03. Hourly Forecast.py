def forecast(*cities):
    weather_forecast = {"Sunny": [],  "Cloudy": [], "Rainy": []}

    for location, weather in cities:
        weather_forecast[weather].append(location)

    sorted_weather = {key: sorted(value) for key, value in weather_forecast.items()}
    result = []
    for key, value in sorted_weather.items():
        for v in value:
            result.append(v)
            result.extend([f" - {key}\n"])

    return ''.join(result)

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))