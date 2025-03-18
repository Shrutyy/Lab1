import csv
import time
import copy

class Student:
    def __init__(self):
        self.student_details_dict = dict()

    def display_records_all(self): #displays all the details of student
        print("Student_Id\tFirst_Name\tLast_Name\tEmail_Address\tCourse_Id\tGrades\tMarks\n")
        for student_id, entry in self.student_details_dict.items():
            course_grade_marks_dict = entry['courses_taken']
            for course_id, course_entry in course_grade_marks_dict.items():
                print(str(student_id) + "," + str(entry['first_name']) + "," + str(entry['last_name']) + "," + str(entry['email_address'])
                    + "," + str(course_id) + "," + str(course_entry[0]) + "," + str(course_entry[1]))
    
    def display_records_sorted_by_email_address(self): #sortig done by email address by using lambda function
        
        start = time.time()
        sorted_dict_by_email_address = dict(sorted(self.student_details_dict.items(), key=lambda item: item[1]['email_address']))
        end = time.time()
        print("It took " + str(end-start) + " seconds to sort the student records by email_address.")
        print("Email_Address\tStudent_Id\tFirst_Name\tLast_Name\tCourse_Id\tGrades\tMarks\n")
        for student_id, student_record in sorted_dict_by_email_address.items():
            course_grade_marks_dict = student_record['courses_taken']
            for course_id, course_entry in course_grade_marks_dict.items():
                print(str(student_record['email_address']) + "," + str(student_id) + "," + str(student_record['first_name']) + "," + str(student_record['last_name']) 
                    + "," + str(course_id) + "," + str(course_entry[0]) + "," + str(course_entry[1]))
    
    def display_records(self, student_id): #displays the time in which we get the output
        start = time.time()
        student_record = self.student_details_dict[student_id]
        end = time.time() - start
        print("It took " + str(end-start) + " seconds to get the student record for student id: " + str(student_id))
        print("Student_Id\tFirst_Name\tLast_Name\tEmail_Address\tCourse_Id\tGrades\tMarks\n")
        course_grade_marks_dict = student_record['courses_taken']
        for course_id, course_entry in course_grade_marks_dict.items():
            print(str(student_id) + "," + str(student_record['first_name']) + "," + str(student_record['last_name']) + "," + str(student_record['email_address']) + "," 
                + "," + str(course_id) + "," + str(course_entry[0]) + "," + str(course_entry[1]))
    
    def add_new_student(self, student_id, first_name, last_name, email_address, course_id, grades, marks): #function to add a new student
        if student_id is None or str(student_id)=="":
            print("It is mandatory to enter a non empty integeer non null student id!! Please try again.")
            return
        if student_id in self.student_details_dict.keys():
            student_record = self.student_details_dict[student_id]
            student_record['first_name'] = first_name
            student_record['last_name'] = last_name
            student_record['email_address'] = email_address
            course_dict = student_record['courses_taken']
            course_dict[course_id] = [grades, marks]
            student_record['courses_taken'] = course_dict
        else:
            student_record = dict()
            student_record['first_name'] = first_name
            student_record['last_name'] = last_name
            student_record['email_address'] = email_address
            course_dict = dict()
            course_dict[course_id] = [grades, marks]
            student_record['courses_taken'] = course_dict
            self.student_details_dict[student_id] = student_record
        print("Student record added\n")
    
    def delete_student(self, student_id): #function to delete a studnet
        del self.student_details_dict[student_id]
        print("Student record deleted successfully")
    
    def check_my_grades(self, student_id): #function to check the grades
        course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
        print("Grades for student " + str(student_id) + " are:\n")
        print("Course_Name\tGrade:\n")
        for course_id, entry in course_grade_marks_dict.items():
            print(str(course_id)+ "," + str(entry[0]))
            
        
    def update_student_record(self, student_id): #function to updatae any data of the student
        detail_to_be_updated = input("Please enter which detail you wish to be update.\n Choices are: FirstName, LastName, EmailAddress, CourseId, Grades, Marks.\n")
        if detail_to_be_updated.lower() == "firstname":
            first_name = input("Please enter new FirstName:\n")
            self.student_details_dict[student_id]['first_name'] = first_name
        elif detail_to_be_updated.lower() == "lastname":
            last_name = input("Please enter new LastName:\n")
            self.student_details_dict[student_id]['last_name'] = last_name
        elif detail_to_be_updated.lower() == "emailaddress":
            email_address = input("Please enter new EmailAddress:\n")
            self.student_details_dict[student_id]['email_address'] = email_address
        elif detail_to_be_updated.lower() == "courseid" or detail_to_be_updated.lower() == "grades" or detail_to_be_updated.lower() == "marks":
            course_id = input("Please enter the course id you want to update for:\n")
            grade = input("Please enter grades for this course:\n")
            marks = input("Please enter marks for this course:\n")
            course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
            course_grade_marks_dict[course_id] = [grade, marks]
            self.student_details_dict[student_id]['courses_taken'] = course_grade_marks_dict
            
        print("Student details are updated\n")

    def check_my_marks(self, student_id):#to check the marks obtained
        course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
        print("Grades for student " + str(student_id) + " are:\n")
        print("Course_Name\tMarks:\n")
        for course_id, entry in course_grade_marks_dict.items():
            print(str(course_id)+ "," + str(entry[1]))

    def display_sum_of_all_scores_for_a_student_id(self, student_id): 
        course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
        sum=0
        for course_id, entry in course_grade_marks_dict.items():
            sum = sum + int(entry[1])
        print("Sum of all coureses scored by student is:\n")
        print(sum)

    def display_average_score_for_all_students_for_a_course_id(self, course_id):
        no_of_students_taking_the_course = 0
        sum_of_scores_for_this_course = 0
        for student_id, student_record in self.student_details_dict.items():
            course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
            if course_id in course_grade_marks_dict.keys():
                course_record = course_grade_marks_dict[course_id]
                sum_of_scores_for_this_course = sum_of_scores_for_this_course + int(course_record[1])
                no_of_students_taking_the_course+=1
        
        print("Average score of students for course " + course_id + " is:\n")
        print(float(sum_of_scores_for_this_course/no_of_students_taking_the_course))


class Course:

    def __init__(self):
        self.course_dict = dict()
    
    def display_courses_all(self): #display the course details
        print("Courses are as follows:\n")
        print("COurse_Id\tCredits\tCourse_name")

        for key, entry in self.course_dict.items():
            print(str(key)+","+str(entry[0])+","+str(entry[1]))
    
    def display_courses(self, course_id): #disoplay the time to run
        start = time.time()
        course_record = self.course_dict[course_id]
        end = time.time() - start
        print("It took " + str(end-start) + " seconds to get the course record for course id: " + str(course_id))
        
        print("Course is as follows:\n")
        print("COurse_Id\tCredits\tCourse_name")
        print(str(course_id)+","+str(course_record[0])+","+str(course_record[1]))

    def display_records_sorted_by_course_name(self): #function for sorting the records
        start = time.time()
        sorted_dict_by_course_name = dict(sorted(self.course_dict.items(), key=lambda item: item[1][1]))
        end = time.time()
        print("It took " + str(end-start) + " seconds to sort the course records by course name.")
        print("Courses are as follows:\n")
        print("CourseName\tCourse_Id\tCredits")

        for course_id, course_record in sorted_dict_by_course_name.items():
            print(str(course_record[1]) + "," + str(course_id)+","+str(course_record[0]))
            
    
    def add_new_course(self, course_id, credits, course_name): #to add a new course to the curriculum
        if course_id is None or str(course_id)=="":
            print("It is mandatory to enter a non empty and non null course id!! Please try again.")
            return
        self.course_dict[course_id] = [credits, course_name]
        print("Course details are added.")
    
    def delete_course(self, course_id): #to delete a new course from the curriculum
        del self.course_dict[course_id]


class Professor:
    def __init__(self):
        self.professor_details_dict = dict()

    def display_professor_details_all(self): #displays the details of the professor
        print("Professor_ID\tName\tEmail_Address\tRank\tCourse_Id\tCourseName\n")
        for professor_id, entry in self.professor_details_dict.items():
            course__dict = entry['courses_taught']
            for course_id, course_name in course__dict.items():
                print(str(professor_id) + "," + str(entry['name']) + "," + str(entry['email_address']) + "," + str(entry['rank']) 
                    + "," + str(course_id) + "," + str(course_name))
    
    def display_records_sorted_by_email_address(self):
        
        start = time.time()
        sorted_dict_by_email_address = dict(sorted(self.professor_details_dict.items(), key=lambda item: item[1]['email_address']))
        end = time.time()
        print("It took " + str(end-start) + " seconds to sort the professor records by email_address.")
        print("Email_Address\tProfessor_ID\tName\tRank\tCourse_Id\tCourseName\n")
        for professor_id, professor_record in sorted_dict_by_email_address.items():
            course__dict = professor_record['courses_taught']
            for course_id, course_name in course__dict.items():
                print(str(professor_record['email_address']) + "," + str(professor_id) + "," + str(professor_record['name']) + "," + str(professor_record['rank']) 
                        + "," + str(course_id) + "," + str(course_name))
    
    def display_professor_details(self, professor_id): #time taken to display professor records
        start = time.time()
        professor_record = self.professor_details_dict[professor_id]
        end = time.time() - start
        print("It took " + str(end-start) + " seconds to get the professor record for professor id: " + str(professor_id))

        print("Professor_ID\tName\tEmail_Address\tRank\tCourse_Id\tCourseName\n")
        course__dict = professor_record['courses_taught']
        for course_id, course_name in course__dict.items():
            print(str(professor_id) + "," + str(professor_record['name']) + "," + str(professor_record['email_address']) + "," + str(professor_record['rank']) 
                    + "," + str(course_id) + "," + str(course_name))
    
    def add_new_professor(self, professor_id, name, email_address, rank, course_id, course_name): #adds a new professor
        if professor_id is None or str(professor_id)=="":
            print("It is mandatory to enter a non empty integeer non null professor id!! Please try again.")
            return
        if professor_id in self.professor_details_dict:
            professor_record = self.professor_details_dict[professor_id]
            professor_record['name'] = name
            professor_record['email_address'] = email_address
            professor_record['rank'] = rank
            course_dict = professor_record['courses_taught']
            course_dict[course_id] = course_name
            professor_record['courses_taught'] = course_dict
        else:
            professor_record = dict()
            professor_record['name'] = name
            professor_record['email_address'] = email_address
            professor_record['rank'] = rank
            course_dict = dict()
            course_dict[course_id] = course_name
            professor_record['courses_taught'] = course_dict
            self.professor_details_dict[professor_id] = professor_record
        print("Professor record added\n")
    
    def delete_professor(self, professor_id): #fucntion to delete the professor
        del self.professor_details_dict[professor_id]
        print("Professor record deleted successfully")
            
        
    def modify_professor_details(self, professor_id):
        detail_to_be_updated = input("Please enter which detail you wish to be update.\n Choices are: Name, EmailAddress, Rank, CourseId, CourseName.\n")
        if detail_to_be_updated.lower() == "name":
            name = input("Please enter new Name:\n")
            self.professor_details_dict[professor_id]['name'] = name
        elif detail_to_be_updated.lower() == "rank":
            rank = input("Please enter new Rank:\n")
            self.professor_details_dict[professor_id]['rank'] = rank
        elif detail_to_be_updated.lower() == "emailaddress":
            email_address = input("Please enter new EmailAddress:\n")
            self.professor_details_dict[professor_id]['email_address'] = email_address

        elif detail_to_be_updated.lower() == "courseid" or detail_to_be_updated.lower() == "coursename":
            course_id = input("Please enter the course id you want to update for:\n")
            coursename = input("Please enter course name for this course:\n")
            courses_dict = self.professor_details_dict[professor_id]['courses_taught']
            courses_dict[course_id] = course_name
            self.professor_details_dict[professor_id]['courses_taught'] = courses_dict
            
        print("Professor details are updated\n")

    def show_course_details_by_professor(self, professor_id):#course details taken by the professor
        courses_dict = self.professor_details_dict[professor_id]['caourses_taught']
        print("Courses Taught by Professor  " + str(professor_id) + " are:\n")
        print("Course_Id\tCourse_Name:\n")
        for course_id, course_name in courses_dict.items():
            print(str(course_id)+ "," + str(course_name))
    

class LoginUser():
    def __init__(self, shift=4) :
        self.login_db = dict()
        self.shifter=shift
        self.s=self.shifter%26
    
    def _convert(self, text,s): 
        
        result=""
        for i,ch in enumerate(text):
            if (ch.isupper()):
                result += chr((ord(ch) + s-65) % 26 + 65)
            else:
                result += chr((ord(ch) + s-97) % 26 + 97)
        return result

    def encrypt_password(self, text): #to encrypt the password
        """return encrypted string."""
        return self._convert(text,self.shifter)
    
    def decrypt(self, text): #to decrypt the password
        """return encrypted string."""
        return self._convert(text,26-self.s)

    def registed_user(self,user_id,email_address,password): 
        if user_id is None or str(user_id)=="":
            print("It is mandatory to enter a non empty integeer non null user id(student_id or prof_id)!! Please try again.")
            return
        password = self.encrypt_password(password)
        print("Encrypted the password before storing in db\n")
        print("Encrypted password is: " + str(password) + "\n")
        print(type(email_address))
        self.login_db[email_address] = [user_id, password]
        print("User registered successfully.\n") 

    def login(self, email_address, password):
        if email_address in self.login_db.keys():
            value=self.login_db[email_address]
            print("Decrypting password stored in Login records to match with input pwd\n")
            decrypted_pwd = self.decrypt(value[1])
            if password == decrypted_pwd:
                return True,value
        else:
            return False,[None for i in range(0,2)]
        
    def logout(self):
        return "loggedout"
    
    def change_password(self, email_address): #to change the password
        print("Changing Password")
        if email_address in self.login_db.keys():
            print("User found")
            new_password = input("Please enter new password")
            self.login_db[email_address][1] = new_password
            print("Password Updated!!")
        else:
            print("User not found!!")
    
    
login_user = LoginUser()   
student = Student()
professor = Professor()
course = Course()

with open('student_records.csv') as file_obj: 

    
    
      
    #skips the heading using next() method 
    heading = next(file_obj) 
      
    #create reader object by passing the file object to reader method 
    reader_obj = csv.reader(file_obj) 
      
    #iterate over each row in the csv file  
    # using reader object 
    courses = set()
    for row in reader_obj:

        login_user.registed_user(row[0], row[3], row[4])
        student.add_new_student(row[0],row[1],row[2],row[3],row[5],row[6],row[7])


with open('course_records.csv') as file_obj: 

    
     
    heading = next(file_obj)       
   
    reader_obj = csv.reader(file_obj)       
   
    for row in reader_obj:
        course.add_new_course(row[0],row[2],row[1])

with open('professor_records.csv') as file_obj: 

    
      
    
    heading = next(file_obj) 
      
   
    reader_obj = csv.reader(file_obj) 
      
   
    for row in reader_obj:

        login_user.registed_user(row[0], row[2], row[3])
        professor.add_new_professor(row[0],row[1],row[2],row[4],row[5],row[6])


print("Sucess")


while True:
    print("Following are actions you can choose from:\n")
    print("1. Print data for all studentsy:\n")
    print("2. Print data for all professors:\n")
    print("3. Print data for all courses:\n")
    print("4. Add new student data:\n")
    print("5. Add new professor data:\n")
    print("6. Add new course data:\n")
    print("7. Delete student data:\n")
    print("8. Delete professor data:\n")
    print("9. Delete course data:\n")
    print("10. Retrieve details of a student using a student id:\n")
    print("11. Retrieve details of a professor using a professor id:\n")
    print("12. Retrieve details of a course using a course id:\n")
    print("13. Show details of all students in sorted order of email_address and display time taken to show records in sorted fashion.\n")
    print("14. Show details of all professor in sorted order of email_address and display time taken to show records in sorted fashion.\n")
    print("15. Show details of all courses in sorted order of course_name and display time taken to show records in sorted fashion.\n")
    print("16. Display sum of all courses for a student id")
    print("17. Display average score for all students for a given course id")
    print("18. Exit program\n")
    action_id = int(input("PLease enter below number for action you want:\n"))
    if action_id==1:
        student.display_records_all()
    elif action_id==2:
        professor.display_professor_details_all()
    elif action_id==3:
        course.display_courses_all()
    elif action_id==4:
        student_id = input("Please enter valid student_id:\n")
        email_address = input("Please enter student email address:\n")
        password = input("Please enter password:\n")
        login_user.registed_user(student_id, email_address, password)
        first_name = input("Please enter first name of the student:\n")
        last_name = input("Please enter last name of the student:\n")
        course_id = input("Please enter course id:\n")
        grades = input("Please enter grades:\n")
        marks = input("Please enter marks:\n")
        student.add_new_student(student_id, first_name, last_name, email_address, course_id, grades, marks)
        
        header = ["student_id", "first_name", "last_name", "email_address", "password", "course_id", "grades", "marks"]
        input_list = [header]
        for student_id, record in student.student_details_dict.items():
            email_address = record['email_address']
            temp_pwd = login_user.login_db[str(email_address)][1]
            course_grade_marks_dict = record['courses_taken']
            for course_id, course_record in course_grade_marks_dict.items():
                input_list.append([student_id, record['first_name'], record['last_name'], record['email_address'], temp_pwd, course_id, course_record[0], course_record[1]])
        with open("student_records.csv",mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(input_list)
        
            
            
    elif action_id==5:
        professor_id = input("Please enter valid professor_id:\n")
        email_address = input("Please enter professor email address:\n")
        password = input("Please enter password:\n")
        login_user.registed_user(professor_id, email_address, password)
        name = input("Please enter name of the professor:\n")
        rank = input("Please enter designation of the professor:\n")
        course_id = input("Please enter course id taught by professor:\n")
        course_name = input("Please enter course for the course_id entered:\n")
        professor.add_new_professor(professor_id, name, email_address, rank, course_id, course_name)
        header = ["professor_id","name","email_address","password","rank,course_id","course_name"]
        input_list = [header]
        for professor_id, record in professor.professor_details_dict.items():
            email_address = record['email_address']
            temp_pwd = login_user.login_db[str(email_address)][1]
            course_grade_marks_dict = record['courses_taught']
            for course_id, course_name in course_grade_marks_dict.items():
                input_list.append([professor_id,record['name'],record['email_address'],temp_pwd,record['rank'],course_id,course_name])
        with open("professor_records.csv",mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(input_list)

    elif action_id==6:
        course_id = input("Please enter course id of new course:\n")
        credits = input("Please enter creditse for new course:\n")
        course_name = input("Please enter course name of the new course")
        course.add_new_course(course_id, credits, course_name)
        header = ["course_id","course_name","credits"]
        input_list = [header]
        for course_id, course_record in course.course_dict.items():
            input_list.append([course_id, course_record[1],course_record[0]])
        with open("course_records.csv",mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(input_list)
    elif action_id==7:
        student_id = input("Please enter which student_id you wish to delete.\n")
        student.delete_student(student_id)

    elif action_id==8:
        professor_id = input("Please enter which Professor ID you want to delete")
        professor.delete_professor(professor_id)
    
    elif action_id==9:
        course_id = input("Please enter course id you want to delete")
        course.delete_course(course_id)

    elif action_id==10:
        student_id = input("Please enter student_id you want details about:\n")
        student.display_records(student_id)
    elif action_id==11:
        professor_id = input("Please enter professor_id you want details about:\n")
        professor.display_professor_details(professor_id)
    elif action_id==12:
        course_id = input("Please enter course_id you want details about:\n")
        course.display_courses(course_id)
    elif action_id==13:
        student.display_records_sorted_by_email_address()
    elif action_id==14:
        professor.display_records_sorted_by_email_address()
    elif action_id==15:
        course.display_records_sorted_by_course_name()
    elif action_id==16:
        student_id = input("Please enter student_id for which you want to see total score:\n")
        student.display_sum_of_all_scores_for_a_student_id(student_id)
    elif action_id==17:
        course_id = input("Please enter course_id for which you want to see average score:\n")
        student.display_average_score_for_all_students_for_a_course_id(course_id)
    elif action_id==18:
        break
    else:
        print("Wrong Choice! Please enter from given choices only!\n")



    

