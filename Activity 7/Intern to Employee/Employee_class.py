class Employee:
    def __init__(self, employee_id, name, email, skills):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.skills = skills
        self.designation = 'Intern'

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Skills:", self.skills)
        print("Designation:", self.designation)

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)

    def set_designation(self, designation):
        self.designation = designation