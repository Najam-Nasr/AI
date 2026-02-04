
# TASK 2:

class StaffMember:
    def __init__(self, full_name, staff_id):
        self.full_name = full_name
        self.staff_id = staff_id

    def get_salary(self):
        raise NotImplementedError("Salary method not implemented")

    def show_details(self):
        print(f"Name: {self.full_name}")
        print(f"Employee ID: {self.staff_id}")


class PermanentStaff(StaffMember):
    def __init__(self, full_name, staff_id, fixed_salary):
        super().__init__(full_name, staff_id)
        self.fixed_salary = fixed_salary

    def get_salary(self):
        return self.fixed_salary


class HourlyStaff(StaffMember):
    def __init__(self, full_name, staff_id, total_hours, rate_per_hour):
        super().__init__(full_name, staff_id)
        self.total_hours = total_hours
        self.rate_per_hour = rate_per_hour

    def get_salary(self):
        return self.total_hours * self.rate_per_hour


# Full-time employee
emp_one = PermanentStaff("Najam", "N2975", 500000)
emp_one.show_details()
print("Salary:", emp_one.get_salary())

print()

# Part-time employee
emp_two = HourlyStaff("Ahmed", "A8965", 12, 1000)
emp_two.show_details()
print("Salary:", emp_two.get_salary())
