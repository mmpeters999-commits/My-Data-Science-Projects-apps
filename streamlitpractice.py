import streamlit as st
import pandas as pd


st.markdown(
    r"""
    ---
    <h2>Hi there, 
    This app tells you the weather in any locations around the world</h2>    
   

""", unsafe_allow_html=True


)

st.markdown("---")


#py -m streamlit run streamlitpractice.py



import requests
import streamlit as st

API_KEY = "00d2960454349ca4fb8fb1e8c54baead"
city = st.text_input('Enter state, country or region to check weather:').lower()

 
if st.button('Show whether'):

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
            <div style="border:1px solid #ddd; padding:10px; border-radius:5px;">
             Weather Details for {city}:<br><br>
            - Temperature: {temperature}°C<br>
            - Humidity: {humidity}%<br>
            - Precipitation (last 1h): {precipitation} mm<br>
            - Wind Speed: {wind_speed} m/s
            </div>
            """, unsafe_allow_html=True)
       else:
        st.write("Error fetching data:", response.status_code)
    else:
        st.write('Invalid state, country or region, Please enter the correct values')
    
    
st.markdown(
    r"""
    
    >**_Built by Micheal Peters_ (Empeetech)**


""", unsafe_allow_html=True
    
)