import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
          help="Select the number of forcasted days")
option = st.selectbox("Select data to view",
             ("Temperature", "Sky"))


if place:
    try:
        filtered_data = get_data(place, days)
        st.subheader(f"{option} for the next {days} days in {place}")

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "DATE", "y": "TEMPERATURE (°C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds":"images/clouds.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=110)


    except KeyError:
        st.info("The location that you entered does not exist!")




