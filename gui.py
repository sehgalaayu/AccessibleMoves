from user import User
import speech_recognition as sr
import subprocess

def run_gui():
    print("AccessibleMoves GUI is running.")
    
    def speak(text):
        subprocess.call(['say', text])

    user = None

    while True:
        print("1. Request Ride")
        print("2. Update Phone Number")
        print("3. Start Navigation")
        print("4. Get Navigation Directions")
        print("5. Request Emergency Assistance")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            origin = input("Enter Origin: ")
            destination = input("Enter Destination: ")
            accessibility_preferences = input("Enter Accessibility Preferences: ")

            user = User(user_id, name, phone_number)
            ride = user.request_ride(origin, destination, accessibility_preferences)
            print(f"Ride requested: {ride.status}")

        elif choice == "2":
            if user:
                new_phone_number = input("Enter New Phone Number: ")
                user.update_phone_number(new_phone_number)
                print(f"Phone number updated for {user.name}")
            else:
                print("Please request a ride first.")

        elif choice == "3":
            if user:
                destination = input("Enter Destination: ")
                user.start_navigation(destination)
                print(f"Navigation started to {destination}")
            else:
                print("Please request a ride first.")

        elif choice == "4":
            if user:
                directions = user.get_navigation_direction()
                print(directions)
                speak(directions)
                user.update_navigation()
            else:
                print("Please start navigation first.")

        elif choice == "5":
            if user:
                assistance = user.request_assistance()
                print(assistance)
                speak(assistance)
            else:
                print("Please start navigation first.")

        elif choice == "6":
            break
