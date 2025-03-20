import streamlit as st
import pandas as pd

# Function to load CSV files into dataframes
@st.cache_data
def load_data():
    trips = pd.read_csv("data/trips.csv")
    cars = pd.read_csv("data/cars.csv")
    cities = pd.read_csv("data/cities.csv")

    return trips, cars, cities

# Load data
trips, cars, cities = load_data()

# Merge trips with cars (joining on car_id)
trips_merged = trips.merge(cars, left_on="car_id", right_on="id", suffixes=("", "_car"))
# Merge with cities for car's city (joining on city_id)
trips_merged = trips_merged.merge(cities, left_on="city_id", right_on="city_id", suffixes=("", "_city"))
st.write(trips_merged["pickup_time"].dtype)
# Streamlit UI
st.title("🚗 Trip Data Analysis Dashboard")

# Convert to date time 
trips_merged["pickup_time"] = pd.to_datetime(trips_merged['pickup_time'])
trips_merged["dropoff_time"] = pd.to_datetime(trips_merged['dropoff_time'])
trips_merged['pickup_date'] = trips_merged['pickup_time'].dt.date

# Create a sidebar to filter by car brand
cars_brand = st.sidebar.multiselect("Select the car brand", trips_merged["brand"].unique(),  trips_merged["brand"].unique())
trips_merged = trips_merged[trips_merged["brand"].isin(cars_brand)]

# Compute business performance metrics
total_trips = len(trips_merged)  # Total number of trips
total_distance = trips_merged["distance"].sum()  # Sum of all trip distances
# Car model with the highest revenue
top_car = trips_merged.groupby("model")["revenue"].sum().idxmax()
top_car_revenue = trips_merged.groupby("model")["revenue"].sum().max()

# Display metrics in columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Trips", value=total_trips)
with col2:
    st.metric(label="Top Car Model by Revenue", value=top_car, help=f"Total revenue: ${top_car_revenue:,.2f}")
with col3:
    st.metric(label="Total Distance (km)", value=f"{total_distance:,.2f}")

# Display the merged dataframe
st.write("### Trips Data")
st.dataframe(trips_merged.head())

# **Trips Over Time (Line Chart)**
st.subheader(" Number of Trips Over Time")
trips_per_day = trips_merged.groupby("pickup_date").size()
st.line_chart(trips_per_day)

# **Revenue Per Car Model (Bar Chart)**
st.subheader(" Total Revenue by Car Model")
revenue_per_model = trips_merged.groupby("model")["revenue"].sum()
st.bar_chart(revenue_per_model)

# **Cumulative Revenue Growth Over Time (Area Chart)**
st.subheader(" Cumulative Revenue Growth")
trips_merged["cumulative_revenue"] = trips_merged["revenue"].cumsum()
cumulative_revenue = trips_merged.groupby("pickup_date")["cumulative_revenue"].max()
st.area_chart(cumulative_revenue)


# **Trips Per Car Model (Bar Chart)**
st.subheader(" Number of Trips per Car Model")
trips_per_model = trips_merged["model"].value_counts()
st.bar_chart(trips_per_model)


# **Revenue Distribution by City (Bar Chart)**
st.subheader(" Revenue by City")
revenue_per_city = trips_merged.groupby("city_name")["revenue"].sum()
st.bar_chart(revenue_per_city)

# **Trip Duration Distribution (Bar Chart)**
st.subheader(" Trip Duration Distribution (Avg per City)")
trips_merged["trip_duration"] = (trips_merged["dropoff_time"] - trips_merged["pickup_time"]).dt.total_seconds() / 60  # Convert to minutes
avg_trip_duration_city = trips_merged.groupby("city_name")["trip_duration"].mean()
st.bar_chart(avg_trip_duration_city)



