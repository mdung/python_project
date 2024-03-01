import requests
from datetime import datetime
import folium
from folium import Marker

# Function to get the real-time ISS location using Open Notify API
def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()
    iss_location = (data['iss_position']['latitude'], data['iss_position']['longitude'])
    timestamp = datetime.utcfromtimestamp(data['timestamp']).strftime('%Y-%m-%d %H:%M:%S UTC')
    return iss_location, timestamp

# Function to update the ISS marker on the map
def update_iss_marker(map_obj, iss_marker, iss_location):
    iss_marker.location = iss_location
    map_obj.add_child(iss_marker)

# Main function to create and update the real-time ISS tracker
def main():
    # Create a folium map centered at (0, 0)
    iss_map = folium.Map(location=[0, 0], zoom_start=2)

    # Initialize ISS marker
    iss_marker = Marker(location=[0, 0], popup="ISS", icon=folium.Icon(color='red'))

    # Update the ISS marker and display the map
    update_iss_marker(iss_map, iss_marker, get_iss_location())
    iss_map.save("iss_tracker_map.html")

    while True:
        # Update ISS location every 10 seconds
        iss_location, timestamp = get_iss_location()
        print(f"ISS Location at {timestamp}: Latitude {iss_location[0]}, Longitude {iss_location[1]}")
        update_iss_marker(iss_map, iss_marker, iss_location)

if __name__ == "__main__":
    main()
