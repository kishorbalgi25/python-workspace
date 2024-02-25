from Employee_class import Employee

class ConversionManager:
    @staticmethod
    def evaluate_performance(intern):
        if intern.performance_rating >= 8:
            intern.setConversionStatus('Approved')
        else:
            intern.setConversionStatus('Rejected')
            raise ValueError("Intern's performance is below the threshold for conversion.")

    @staticmethod
    def convert_to_employee(intern):
        if intern.conversion_status == 'Approved':
            employee = Employee(intern.intern_id, intern.name, intern.email, intern.skills)
            employee.set_designation('Full-time Employee')
            return employee
        else:
            raise ValueError("Conversion decision cannot be made.")
