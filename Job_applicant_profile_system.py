class PersonalInfo:
    def __init__(self, name, dob, contact, email):
        self.name = name
        self.dob = dob
        self.contact = contact
        self.email = email
    
    def display_personal(self):
        print("Name:", self.name)
        print("DOB:", self.dob)
        print("Contact:", self.contact)
        print("Email:", self.email)

class Education(PersonalInfo):
    def __init__(self, name, dob, contact, email, degree, uni, year, cgpa):
        PersonalInfo.__init__(self, name, dob, contact, email)
        self.degree = degree
        self.uni = uni
        self.year = year
        self.cgpa = cgpa

    def display_education(self):
        print("Degree:", self.degree)
        print("University:", self.uni)
        print("Year:", self.year)
        print("CGPA:", self.cgpa)

class CandidateProfile(Education):
    def __init__(self, name, dob, contact, email, degree, uni, year, cgpa, comp, role, exp, skills):
        Education.__init__(self, name, dob, contact, email, degree, uni, year, cgpa)
        self.comp = comp
        self.role = role
        self.exp = exp # Years of experience
        self.skills = skills

    def display_complete(self):
        print("\n CANDIDATE PROFILE")
        self.display_personal()
        self.display_education()
        print("Company:", self.comp)
        print("Role:", self.role)
        print("Experience:", self.exp, "years")
        print("Skills:", self.skills)

    def check_eligibility(self):
        if self.exp > 5:
            print("Eligible for Senior Role")
        else:
            print("Eligible for Junior Role")

# Objects for two candidates
c1 = CandidateProfile("Reshma", "2006", "987654321", "rash@gmail.com", "B.Tech", "ANITS", 2017, 9.5, "Google", "GM", 6, "Python")
c2 = CandidateProfile("Jashu", "2006", "123456789", "jash@gmil.com", "B.Tech", "ANITS", 2024, 9.5, "TCS", "Trainee", 2, "Java")

c1.display_complete()
c1.check_eligibility()
c2.display_complete()
c2.check_eligibility()
