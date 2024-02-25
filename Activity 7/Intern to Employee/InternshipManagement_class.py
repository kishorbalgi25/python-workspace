from Conversion_Management_class import ConversionManager
from Intern_class import Intern
from Employee_class import Employee

class InternshipManagementSystem:
    def __init__(self):
        self.interns = []
        self.employees = []

    def add_intern(self, intern):
        self.interns.append(intern)

    def display_interns(self):
        print("Interns:")
        for intern in self.interns:
            intern.display_details()
            print()

    def display_employees(self):
        print("Employees:")
        for employee in self.employees:
            employee.display_details()
            print()

    def simulate_conversion_process(self):
        for intern in self.interns:
            try:
                ConversionManager.evaluate_performance(intern)
                employee = ConversionManager.convert_to_employee(intern)
                self.employees.append(employee)
            except ValueError as e:
                print("Conversion Error:", e)
                
if __name__ == "__main__":
    intern1 = Intern(1, "John Doe", "john@example.com", ["Python", "Java"], 9)
    intern2 = Intern(2, "Jane Smith", "jane@example.com", ["C++", "JavaScript"], 7)

    internship_system = InternshipManagementSystem()
    internship_system.add_intern(intern1)
    internship_system.add_intern(intern2)

    internship_system.display_interns()

    internship_system.simulate_conversion_process()

    internship_system.display_employees()