import requests

def get_weather(city):
    api_key = '6c18d4b780df57a1cc1a183b7aaa8805'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_url = base_url + 'q=' + city + '&appid=' + api_key + '&units=metric'
    
    try:
        response = requests.get(complete_url)
        data = response.json()

        # Check if the city was found
        if data['cod'] == 200:  # 200 means successful request
            main = data['main']
            weather = data['weather'][0]
            temperature = main['temp']
            pressure = main['pressure']
            humidity = main['humidity']
            description = weather['description']

            # Print weather details
            print(f"Temperature: {temperature}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Weather description: {description}")
        else:
            print("City not found.")
    except KeyError as e:
        print(f"KeyError: {e} - Something went wrong while retrieving the data.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e} - There was a problem with the request.")

if __name__ == "__main__":
    city = input("Enter city name:  ")
    get_weather(city)
