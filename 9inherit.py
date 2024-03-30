class Employee:
    organisation_name = "CDAC Institute"

    def __init__(self, emp_id, name, base_location, deployed_location, designation, salary):
        # Instance variables
        self.emp_id = emp_id
        self.name = name
        self.base_location = base_location
        self.deployed_location = deployed_location
        self.designation = designation
        self.salary = salary

    ###################### Class method
    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name

    ###################### Class method
    @classmethod
    def set_organisation_name(cls, org_name):
        cls.organisation_name = org_name

    ###################### Instance method
    def get_employee_details(self):
        return self.__dict__

########################## Example usage:
emp1 = Employee(1, "Utk Gvt", "Nashik", "Maharashtra", "Q&A Tester", 450000)
emp2 = Employee(2, "Manoj P", "Nandurbar", "Maharashtra", "QA Engineer", 90000)

print("Employee details:")
for emp in (emp1, emp2):
    print(emp.get_employee_details())

print("Organization name: " + Employee.get_organisation_name())
Employee.set_organisation_name("NCL Institute")
print("Organization name: " + Employee.get_organisation_name())