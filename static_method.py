class Emp():
    emp_name="Prince"
    emp_age=21

    @staticmethod
    def get_details():
        print(f"My name is {Emp.emp_name} and my age is {Emp.emp_age}")



Emp.get_details()
obj1=Emp()
obj1.get_details()
