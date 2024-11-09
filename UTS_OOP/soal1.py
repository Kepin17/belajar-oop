from abc import ABC, abstractmethod

class Address:
    def __init__(self, street, city, state, postal_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def validate(self):
        return isinstance(self.postal_code, int) and self.postal_code > 0

    def output_as_label(self):
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}"

class Person(ABC):
    def __init__(self, name, phone_number, email_address, address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address  

    def purchase_parking_pass(self):
        print(f"{self.name} has successfully purchased a parking pass.")
    
    @abstractmethod
    def get_details(self):
        pass  

class Student(Person):
    def __init__(self, name, phone_number, email_address, address, student_number, average_mark):
        super().__init__(name, phone_number, email_address, address)
        self.student_number = student_number
        self.average_mark = average_mark

    def is_eligible_to_enroll(self):   
        return self.average_mark >= 70

    def get_seminars_taken(self):
        print(f"{self.name} has taken {self.student_number} seminars.") 

    def get_details(self):
        return f"Student: {self.name}, Average Mark: {self.average_mark}"

class Professor(Person):
    def __init__(self, name, phone_number, email_address, address, salary, staff_number, years_of_service, number_of_classes):
        super().__init__(name, phone_number, email_address, address)
        self.salary = salary
        self.staff_number = staff_number
        self.years_of_service = years_of_service
        self.number_of_classes = number_of_classes

    def get_details(self):
        return f"Professor: {self.name}, Years of Service: {self.years_of_service}"

    def supervises(self):
        return "Supervising students or research projects"

address = Address("jl.Kue Raya", "Bandung", "State", 9920, "Country")
student = Student("Olyzano", "628-123-7890", "olyzano@gmail.com", address, 1001, 85)
professor = Professor("Dr. Charlie", "098-765-4321", "drCharlie@gmail.com", address, 70000, 2001, 10, 3)

print(student.get_details())
print(professor.get_details())
print(student.is_eligible_to_enroll())
print(address.output_as_label())
print(professor.supervises())
