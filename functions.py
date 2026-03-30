students = {}

def register ( name , age , ID ,course, state):
    
    name = input("Enter the student's name: ")
    
    try:
        age = int(input("Enter the student's age: "))
        ID = int(input("Enter the ID the studen't: "))
    except:
        print("Errors: Please enter your age and ID again")
        
    course = (input("Enter the student's course: "))
    state = input("Enter the studen't active/inactive: ")
            
    return 
        
register("name", "age","ID","course","state")

students = { 1:{"name":"name",
            "age" : "age",
            "ID": "ID"}}           
            

def consul (students ):
   search = input("Enter one of these options to search for the student 1.name, 2. age, 3.ID: ")
   
   for find,travel  in search(students):
        if travel == students:
            return find

consul("students")



def update(students, keys , update_student):
    current = input("select what you want to update 1.name, 2. age: ")
    print()
    
    students[keys] = update_student
    return students

update("students", "keys","update_student")
    
    
    
def delete (students , keys):
    eliminating = input("select which one you want to delete  1.name , 2.age ,3.ID: ")
    del name 
    return students.pop(keys, None)
    
    

            
            
    
    
    


