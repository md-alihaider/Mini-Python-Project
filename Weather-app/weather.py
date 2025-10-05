import requests

def weather_in_python():
    # 1. Base URL (The service's main address)
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    # 2. Your API key
    API_KEY = "a60c4574689fa1e8c9a2e27c57537e54"

    # 3. The city we want to check 
    CITY = input("Enter your city: ").capitalize().strip()

    parameters = {
        'q' : CITY,              
        'appid' : API_KEY,
        'units' : 'metric'
    }

    response = requests.get(BASE_URL, params=parameters)

    if response.ok:
        #.json() turn json file into dictionary
        weather_data = response.json()

        # 1. Extract the main data points
        temperature = weather_data['main']['temp']
        # The description is usually in a list under the 'weather' key
        description = weather_data['weather'][0]['description'].capitalize() 
        humidity = weather_data['main']['humidity']

        # 2. Print the results clearly
        print("-" * 40)
        print(f"Current Weather in {CITY}:")
        print("-" * 40)
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity:    {humidity}%")
        print(f"☀️ Condition:   {description}")
        print("-" * 40)
    else:
        status = response.status_code
        if status == 404:
            print("-" * 40)
            print(f"❌ Error: City '{CITY}' not found.")
            print("Please check the spelling.")
            print("-" * 40)
        else:
            print("-" * 40)
            print(f"❌ Error during API call. Status Code: {status}")
            print("Please check your API key or internet connection.")
            print("-" * 40)

weather_in_python()
