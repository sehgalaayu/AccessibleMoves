import random

class Navigation:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.route = self.plan_route()

    def plan_route(self):
        # Placeholder for actual route planning logic
        return [f"Step {i+1}: Go straight" for i in range(5)]

    def get_directions(self):
        return self.route.pop(0) if self.route else "You've reached your destination."

    def update_route(self):
        self.route = self.plan_route()

    def emergency_assistance(self):
        return "Emergency assistance requested."
