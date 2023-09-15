weather_conditions = ["Sunny", "Cloudy", "Rainy", "Snowy"]

num_days = int(input("Please enter the number of days for the weather forecast: "))
current_weather_index = 0

for day in range(1, num_days + 1):
    weather_condition = weather_conditions[current_weather_index]

    print(f"Day {day}: {weather_condition}")
    current_weather_index = (current_weather_index + 1) % len(weather_conditions)
