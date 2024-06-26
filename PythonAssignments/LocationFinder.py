# 4.Write a program to find the distance between two locations when their latitude and longitudes are given.
# Hint:Use the math module.

# Import module
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="nominatim.openstreetmap.org")
location = geolocator.geocode("175 5th Avenue NYC")
print('location address is : ',location.address)
print((location.latitude, location.longitude))
print(location.raw)
# Assign Latitude & Longitude
# Latitude = "25.594095"
# Longitude = "85.137566"

Latitude = "34.138332"
Longitude = "-118.660835"

# Displaying Latitude and Longitude
print("Latitude: ", Latitude)
print("Longitude: ", Longitude)

# Get location with geocode
location = geolocator.geocode(Latitude + "," + Longitude)

# Display location
print("\nLocation of the given Latitude and Longitude:")
print(location)