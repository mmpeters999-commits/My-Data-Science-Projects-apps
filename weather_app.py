import streamlit as st
import pandas as pd
import requests

# Inject custom CSS for theming
st.markdown(
    """
    <style>
        /* Set primary color for highlights and accents */
        :root {
            --primary-color: #e61c06ff;
            --background-color: #010714ff;
            --secondary-background-color: #0652d6ff;
            --text-color: #fafafa;
            --font-family: 'sans-serif';
        }

        /* Apply background color */
        body {
            background-color: var(--background-color);
            font-family: var(--font-family);
            color: var(--text-color);
        }

        /* Style headings */
        h2 {
            color: var(--primary-color);
            font-family: var(--font-family);
        }

        /* Style markdown and other text */
        /* Optional: override other default styles if needed */
        /* Example for markdown text */
        .css-1y0tads {
            color: var(--text-color);
        }

        /* Style buttons */
        div.stButton > button {
            background-color: var(--primary-color);
            color: #fff;
            font-family: var(--font-family);
        }

        /* Style columns or other elements as needed */
        /* Add more custom styles if necessary */
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    ---

    <h2>Hi there,</h2>
    <p>This app tells you the temperature in any locations around the world</p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

API_KEY = "00d2960454349ca4fb8fb1e8c54baead"
city = st.text_input('Enter state, country or region to check weather:').lower()

if st.button('Show weather'):
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            temperature = round(data['main']['temp'], 1)
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            precipitation = 0
            if 'rain' in data and '1h' in data['rain']:
                precipitation = data['rain']['1h']
            elif 'snow' in data and '1h' in data['snow']:
                precipitation = data['snow']['1h']

            previous_temperature = temperature - 2
            temp_delta = round(temperature - previous_temperature, 1)

            st.write(f"Weather details for {city}:")

            col1, col2, col3, col4 = st.columns(4)
            col1.metric(f"Temperature in {city}", f"{temperature}°C", delta=f"{temp_delta}°C")
            col2.metric("Humidity", f"{humidity}%")
            col3.metric("Precipitation (last 1h)", f"{precipitation} mm")
            col4.metric("Wind Speed", f"{wind_speed} m/s")

            st.markdown("---")
            st.markdown(
                f"""
                <div style="border:1px solid #ddd; padding:10px; border-radius:5px; background-color:#111;">
                <strong>Weather Details for {city}:</strong><br><br>
                - Temperature: {temperature}°C<br>
                - Humidity: {humidity}%<br>
                - Precipitation (last 1h): {precipitation} mm<br>
                - Wind Speed: {wind_speed} m/s
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.write("Error fetching data:", response.status_code)
    else:
        st.write('Invalid state, country or region, Please enter the correct values')

st.markdown(
    """
    >**_Built by Micheal Peters_ (Empeetech)**
    """
)



#py -m streamlit run weather_app.py