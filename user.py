import json
from ride import Ride
from navigation import Navigation
class User:
    def __init__(self, user_id, name, phone_number):
        self.user_id = user_id
        self.name = name
        self.phone_number = phone_number
        self.rides = []
        self.navigation = None

    @staticmethod
    def load_users():
        with open("data/users.json", "r") as file:
            return json.load(file)

    @staticmethod
    def save_users(users):
        with open("data/users.json", "w") as file:
            json.dump(users, file)

    def request_ride(self, origin, destination, accessibility_preferences):
        new_ride = Ride(self.user_id, origin, destination, accessibility_preferences)
        self.rides.append(new_ride)
        users = User.load_users()
        users.append(self.__dict__)
        User.save_users(users)
        return new_ride

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def start_navigation(self, destination):
        self.navigation = Navigation("Current Location", destination)

    def get_navigation_direction(self):
        if self.navigation:
            return self.navigation.get_directions()
        else:
            return "No active navigation."

    def update_navigation(self):
        if self.navigation:
            self.navigation.update_route()

    def request_assistance(self):
        if self.navigation:
            return self.navigation.emergency_assistance()
        else:
            return "No active navigation."
