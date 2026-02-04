# TASK 1:

class RentalVehicle:
    def __init__(self, vid, company, daily_rate):
        self.vid = vid
        self.company = company
        self.daily_rate = daily_rate

    def show_info(self):
        print(f"Vehicle ID: {self.vid}")
        print(f"Brand: {self.company}")
        print(f"Daily Rent: {self.daily_rate}")

    def get_rent_amount(self, duration):
        return self.daily_rate * duration


# First vehicle
vehicle_one = RentalVehicle("BCP-567", "Suzuki", 500)
vehicle_one.show_info()
print(f"Total Rent for {vehicle_one.vid} is {vehicle_one.get_rent_amount(5)}")
print(f"Total Rent for {vehicle_one.vid} is {vehicle_one.get_rent_amount(2)}")

print()

# Second vehicle
vehicle_two = RentalVehicle("U-5678", "Suzuki", 1500)
vehicle_two.show_info()
print(f"Total Rent for {vehicle_two.vid} is {vehicle_two.get_rent_amount(8)}")
print(f"Total Rent for {vehicle_two.vid} is {vehicle_two.get_rent_amount(4)}")
