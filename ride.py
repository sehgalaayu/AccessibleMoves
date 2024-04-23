class Ride:
    def __init__(self, user_id, origin, destination, accessibility_preferences):
        self.user_id = user_id
        self.origin = origin
        self.destination = destination
        self.accessibility_preferences = accessibility_preferences
        self.status = "Pending"

    def confirm_ride(self):
        self.status = "Confirmed"
        return "Ride request confirmed."

    def cancel_ride(self):
        self.status = "Cancelled"
        return "Ride request cancelled."
