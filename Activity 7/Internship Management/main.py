class Intern:
    def __init__(self, intern_id, name, email, skills):
        self.intern_id = intern_id
        self.name = name
        self.email = email
        self.skills = skills

    def display_details(self):
        print(f"Intern ID: {self.intern_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Skills: {', '.join(self.skills)}")

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)


class Project:
    def __init__(self, project_id, title, description):
        self.project_id = project_id
        self.title = title
        self.description = description
        self.assigned_intern = None

    def display_details(self):
        print(f"Project ID: {self.project_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        if self.assigned_intern:
            print(f"Assigned Intern: {self.assigned_intern.name}")
        else:
            print("Assigned Intern: None")

    def assign_intern(self, intern):
        if not self.assigned_intern:
            self.assigned_intern = intern
            print(f"{intern.name} assigned to project {self.title}")
        else:
            print(f"This project already has an intern assigned.")


class InternshipCoordinator:
    def __init__(self):
        self.interns = []
        self.projects = []

    def add_intern(self, intern):
        self.interns.append(intern)

    def add_project(self, project):
        self.projects.append(project)

    def assign_intern_to_project(self, intern_id, project_id):
        intern = next((i for i in self.interns if i.intern_id == intern_id), None)
        project = next((p for p in self.projects if p.project_id == project_id), None)
        if intern and project:
            project.assign_intern(intern)
        elif not intern:
            print("Intern not found.")
        elif not project:
            print("Project not found.")

    def track_project_progress(self, project_id, progress):
        project = next((p for p in self.projects if p.project_id == project_id), None)
        if project:
            print(f"Updating progress for project {project.title}: {progress}")
        else:
            print("Project not found.")


class InternshipManagementSystem:
    def __init__(self):
        self.coordinator = InternshipCoordinator()

    def onboard_intern(self, intern):
        self.coordinator.add_intern(intern)
        print(f"{intern.name} onboarded successfully.")

    def create_project(self, project):
        self.coordinator.add_project(project)
        print(f"Project '{project.title}' created successfully.")

    def assign_intern_to_project(self, intern_id, project_id):
        self.coordinator.assign_intern_to_project(intern_id, project_id)

    def update_project_progress(self, project_id, progress):
        self.coordinator.track_project_progress(project_id, progress)


# Example usage:
if __name__ == "__main__":
    # Create Intern objects
    intern1 = Intern(1, "Alice", "alice@example.com", ["Python", "Java"])
    intern2 = Intern(2, "Bob", "bob@example.com", ["C++", "JavaScript"])

    # Create Project objects
    project1 = Project(101, "Web Development", "Develop a website using Django.")
    project2 = Project(102, "Mobile App", "Build a mobile app for Android.")

    # Create Internship Management System
    ims = InternshipManagementSystem()

    # Onboard interns
    ims.onboard_intern(intern1)
    ims.onboard_intern(intern2)

    # Create projects
    ims.create_project(project1)
    ims.create_project(project2)

    # Assign interns to projects
    ims.assign_intern_to_project(1, 101)
    ims.assign_intern_to_project(2, 102)

    # Update project progress
    ims.update_project_progress(101, "50% complete")
    ims.update_project_progress(103, "30% complete") 
