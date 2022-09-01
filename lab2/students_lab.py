from dataclasses import dataclass


# Creates the Student dataclass, has a name, school_id, and gpa field.  No longer needs the __str__ or __init__ calls as they are built in, one can use the 
# __str__ to modify the output if one so desires!
@dataclass
class Student:
        name: str
        school_id: str
        gpa: float

# Main function, this is used to test the Student class!
def main():
    alex = Student('Alex', 'asdf', 3.5)
    print(alex)

    jam = Student('Jam', 'JAM1223', 0.2)
    print(jam)
    jam.gpa = 3.2
    print(jam.gpa)
main()