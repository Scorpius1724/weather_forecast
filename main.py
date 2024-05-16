import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
          help="Select the number of forcasted days")
option = st.selectbox("Select data to view",
             ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates = ["2022-25-4", "2022-26-5"]
    temperatures = [10, 20]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "date", "y": "temperature"})
st.plotly_chart(figure)