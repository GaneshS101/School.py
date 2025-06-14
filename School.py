Students = {
    "Alice": {"grade": "A", "school_grade": "10"},
    "Bob": {"grade": "B", "school_grade": "11"},
    "Charlie": {"grade": "C", "school_grade": "9"}
}

while True:
    choice = input("Hi! Do you want to Add, Take, View a student's details? Enter 'q' to quit: ").strip().capitalize()

    #Add Student
    if choice == 'Add':
        name = input("What is the student's name? ")

        valid_grades = ['A', 'B', 'C', 'D', 'F']
        grade = input("What is the student's grade? A, B, C, D, F: ").strip().upper()
        while grade not in valid_grades:
            print("Please enter a valid grade (A, B, C, D, F).")
            grade = input("What is the student's grade? A, B, C, D, F: ").strip().upper()

        school_grade = int(input("What is the student's school grade? 1-12 "))
        while school_grade not in range(1,13):
            print("Please enter a valid school grade 1-12. ")
            school_grade = input("What is the student's school grade? 1-12 ").strip()
        
        Students[name] = {"grade": grade, "school_grade": school_grade}

    #Remove Student
    elif choice == 'Take':
        print(Students)
        name = input("What is the student's name? ")
        Relation = input("What is your relation to the child? ")
        Relation = Relation.lower()
        Relations = {
            "mom": ["mom", "mother", "mama", "mommy", "mum", "ma"],
            "dad": ["dad", "father", "papa", "daddy", "pa"],
            "brother": ["brother", "bro", "sib"],
            "sister": ["sister", "sis", "sib"],
            "grandma": ["grandma", "grandmother", "granny", "nana", "grammy"],
            "grandpa": ["grandpa", "grandfather", "granddad", "pop", "pops"],
            "aunt": ["aunt", "auntie", "aunty"],
            "uncle": ["uncle", "unc"],
            "cousin": ["cousin", "cuz", "cous"]
            }
        if Relation not in Relations:
            print("Sorry I can't give you the child for safety purposes please leave ")
        if Relation in Relations:
            if name in Students:
                Students.pop(name)
                print("Student removed. Have a nice day! ")
            else:
                print("That student is not in this school. ")

    #View Students
    elif choice == 'View':
        print("Here are all the students and their details:")
        for student, details in Students.items():
            print(f"\n{student}: Grade = {details['grade']}, School Grade = {details['school_grade']}\n")

    #Quit
    elif choice == 'Q':
        break
    #Invalid Choice
    else:
        print("Invalid choice. Please enter Add, Take, View, or q to quit.")
