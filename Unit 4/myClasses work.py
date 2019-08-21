import myClasses

def main():
    person = myClasses.Person("Mr.Rao", 21)
    
    person.explainTerm()
    
    person.introduceSelf()
    
    name, age = person.getName(), person.getAge()
    print("This person's name is" + name)
    print("They are" , age ," years old")
    
    person.setName("Steve")
    person.setAge(45)
    name, age = person.getName(), person.getAge()
    print("The new person's name is" + name)
    print("They are" , age ," years old")    
    
    student = myClasses.Student("Jason", 12)
    student.setStudentId("333444333") 
    
    name, age = student.getName(), student.getAge()
    print("This person's name is " + name)
    print("They are" , age ," years old")
    print("Their student ID is: ", student.getStudentId())
    
    student.setName("Steve")
    student.setAge(45)
    name, age = person.getName(), person.getAge()
    print("The new person's name is " + name)
    print("They are" , age ," years old")
    print(student.introduceSelf())
    student.setStudentId("444333444")
    
    
main()