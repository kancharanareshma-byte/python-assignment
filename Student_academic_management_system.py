class College:
    def __init__(self, code, name, location, s1, s2, s3):
        self.college_code = code
        self.college_name = name
        self.location = location
        # Directly assigning the 3 student objects
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def display_report(self):
        print("COLLEGE DETAILS")
        print("Name:", self.college_name)
        print("Code:", self.college_code)
        print("Location:", self.location)
        print("STUDENT ACADEMIC REPORT:")       
        self.s1.print_studentdetails()
        self.s2.print_studentdetails()
        self.s3.print_studentdetails()
# --- Execution ---
# 1. Create three objects for Student class
std1 = Student(81, "hasini", 85, 90, 88, 2006, 30000)
std2 = Student(102, "Jashu", 70, 99, 98, 2006, 46000)
std3 = Student(103, "Reshma", 77, 88, 99, 2006, 50000)
# 2. Create one object for College class and pass the 3 students
my_college = College("ANES001", "ANITS", "Visakhapatnam", std1, std2, std3)
# 3. Display report
my_college.display_report()
