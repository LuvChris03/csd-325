import re
import requests

# Function to validate the zip code using RegEx (US format)
def is_valid_zip(zip_code):
    # Regular expression for validating US zip codes (5 digits)
    pattern = r"^\d{5}$"
    return re.match(pattern, zip_code) is not None

# Function to fetch weather data from OpenWeather API
def get_weather_data(zip_code):
    api_key = "906b6939735602a519447e37a839d229"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Construct the complete URL to access the weather data
    url = f"{base_url}?zip={zip_code},us&appid={api_key}&units=imperial"  # Using imperial units for Fahrenheit

    try:
        response = requests.get(url)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            # Extract the relevant information
            main = data.get('main', {})
            weather = data.get('weather', [{}])[0]
            temp = main.get('temp')
            description = weather.get('description')
            humidity = main.get('humidity')
            pressure = main.get('pressure')

            # Return weather information
            return (f"Temperature: {temp}°F\n"
                    f"Weather: {description.capitalize()}\n"
                    f"Humidity: {humidity}%\n"
                    f"Pressure: {pressure} hPa")
        else:
            return "Error: Invalid zip code or unable to fetch data from OpenWeather."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Main function to run the program
def main():
    while True:
        # Ask the user for their zip code
        zip_code = input("Enter your zip code (5 digits): ")

        # Validate the zip code
        if not is_valid_zip(zip_code):
            print("Invalid zip code. Please enter a valid 5-digit zip code.")
            continue

        # Fetch and display weather data
        weather_info = get_weather_data(zip_code)
        print(weather_info)

        # Ask if the user wants to run the program again
        again = input("\nDo you want to check another zip code? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

