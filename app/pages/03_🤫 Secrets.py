# import streamlit as st
# import requests
# import datetime
# import pandas as pd
# import plotly.express as px

# # spell = st.secrets['spell']
# # key = st.secrets.some_magic_api.key
# # st.write(spell)
# # st.write(key)

# MAPBOX_ACCESS_TOKEN = st.secrets.some_magic_api.mapbox_api_key
# TAXI_FARE_API_URL = "https://taxifare.lewagon.ai/predict"
# MAPBOX_GEOCODE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"


# st.title("NYC Taxi Fare Predictor")

# # Function to get location suggestions
# def get_location_suggestions(query):
#     if query:
#         response = requests.get(f"{MAPBOX_GEOCODE_URL}{query}.json", params={"access_token": MAPBOX_ACCESS_TOKEN})
#         if response.status_code == 200:
#             features = response.json().get("features", [])
#             return [(feature["place_name"], feature["center"]) for feature in features]
#     return []

# col1, col2 = st.columns(2)
# # Pickup location
# pickup_query = col1.text_input("Type Pickup Location and select from the options")
# pickup_suggestions = get_location_suggestions(pickup_query) if pickup_query else []
# pickup_selection = col2.selectbox("Select Pickup Location", [""] + [s[0] for s in pickup_suggestions])

# pickup_lat, pickup_lng = (40.71427, -74.00597)
# if pickup_selection and pickup_selection != "":
#     selected_coords = dict(pickup_suggestions).get(pickup_selection)
#     if selected_coords:
#         pickup_lat, pickup_lng = selected_coords[1], selected_coords[0]

# # Dropoff location
# dropoff_query = col1.text_input("Enter Dropoff Location")
# dropoff_suggestions = get_location_suggestions(dropoff_query) if dropoff_query else []
# dropoff_selection = col2.selectbox("Select Dropoff Location", [""] + [s[0] for s in dropoff_suggestions])

# dropoff_lat, dropoff_lng = (40.802, -73.956)
# if dropoff_selection and dropoff_selection != "":
#     selected_coords = dict(dropoff_suggestions).get(dropoff_selection)
#     if selected_coords:
#         dropoff_lat, dropoff_lng = selected_coords[1], selected_coords[0]

# col4, col5, col6, col7 = st.columns(4)

# passenger_count = col4.number_input("Passenger Count", min_value=1, max_value=6, value=1)
# pickup_datetime = col5.text_input("Pickup Date & Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# if col4.button("Predict Fare"):
#     params = {
#         "pickup_latitude": pickup_lat,
#         "pickup_longitude": pickup_lng,
#         "dropoff_latitude": dropoff_lat,
#         "dropoff_longitude": dropoff_lng,
#         "passenger_count": passenger_count,
#         "pickup_datetime": pickup_datetime
#     }
#     response = requests.get(TAXI_FARE_API_URL, params=params)
#     if response.status_code == 200:
#         fare = response.json().get("fare", "N/A")
#         if pickup_selection is None:
#             st.success(f"You want to go from **{pickup_selection.split(',')[0] + ',' + pickup_selection.split(',')[1]}** to **{dropoff_selection.split(',')[0] + ',' + dropoff_selection.split(',')[1]}**. Predicted Fare: **${round(fare, 2)}**")
#         else:

#             st.success(f"You want to go from **{pickup_selection.split(',')[0] + ',' + pickup_selection.split(',')[1]}** to **{dropoff_selection.split(',')[0] + ',' + dropoff_selection.split(',')[1]}**. Predicted Fare: **${round(fare, 2)}**")

#     else:
#         st.error("Error fetching fare prediction")

# map_data = pd.DataFrame(
#     [[pickup_lng, pickup_lat], [dropoff_lng, dropoff_lat]],
#     columns=["lon", "lat"]
# )
# fig = px.scatter_mapbox(
#     map_data,
#     lat="lat",
#     lon="lon",
#     zoom=9,
#     center={"lat": 40.71427, "lon": -74.00597},
#     # mapbox_style="open-street-map",
# )

# fig.update_traces(marker=dict(size=15, color='purple'))  # Set fixed size and color for markers
# fig.update_layout(mapbox_accesstoken=MAPBOX_ACCESS_TOKEN)
# st.plotly_chart(fig)
