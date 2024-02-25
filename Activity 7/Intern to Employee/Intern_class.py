class Intern:
    def __init__(self, intern_id, name, email, skills, performance_rating):
        self.intern_id = intern_id
        self.name = name
        self.email = email
        self.skills = skills
        self.performance_rating = performance_rating
        self.conversion_status = None

    def display_details(self):
        print("Intern ID:", self.intern_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Skills:", self.skills)
        print("Performance Rating:", self.performance_rating)
        print("Conversion Status:", self.conversion_status)

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)

    def evaluate_performance(self):
        if self.performance_rating >= 8:
            self.conversion_status = 'Approved'
        else:
            self.conversion_status = 'Rejected'
    
    def setConversionStatus(self,status):
            self.conversion_status = status
