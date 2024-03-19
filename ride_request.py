

class RideRequest:
    def __init__(self, user_id, origin, destination, accessibility_preferences):
        self.user_id = user_id
        self.origin = origin
        self.destination = destination
        self.accessibility_preferences = accessibility_preferences
        self.status = "Pending"

    def confirm_ride(self):
        self.status = "Confirmed"
        print("Ride request confirmed.")

    def cancel_ride(self):
        self.status = "Cancelled"
        print("Ride request cancelled.")

# File: main.py

from ride_request import RideRequest

def main():
    user_id = 12345
    origin = "123 Main St"
    destination = "456 Oak Ave"
    accessibility_preferences = ["Wheelchair accessible vehicle", "Audio instructions"]

    ride_request = RideRequest(user_id, origin, destination, accessibility_preferences)
    ride_request.confirm_ride()

if __name__ == "__main__":
    main()
