import unittest
import time
import csv


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
        return True
    
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
        return True
    
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
        return True
    
    def add_new_student(self, student_id, first_name, last_name, email_address, course_id, grades, marks): #function to add a new student
        if student_id is None or str(student_id)=="":
            print("It is mandatory to enter a non empty integeer non null student id!! Please try again.")
            return False
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
        return True
    
    def delete_student(self, student_id): #function to delete a studnet
        del self.student_details_dict[student_id]
        print("Student record deleted successfully")
        return True
    
    def check_my_grades(self, student_id): #function to check the grades
        course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
        print("Grades for student " + str(student_id) + " are:\n")
        print("Course_Name\tGrade:\n")
        for course_id, entry in course_grade_marks_dict.items():
            print(str(course_id)+ "," + str(entry[0]))
        return True
            
        
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
        return True

    def check_my_marks(self, student_id):#to check the marks obtained
        course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
        print("Grades for student " + str(student_id) + " are:\n")
        print("Course_Name\tMarks:\n")
        for course_id, entry in course_grade_marks_dict.items():
            print(str(course_id)+ "," + str(entry[1]))
        return True

    def display_sum_of_all_scores_for_a_student_id(self, student_id): 
        course_grade_marks_dict = self.student_details_dict[student_id]['courses_taken']
        sum=0
        for course_id, entry in course_grade_marks_dict.items():
            sum = sum + int(entry[1])
        print("Sum of all coureses scored by student is:\n")
        print(sum)
        return True

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
        return True



class TestStudent(unittest.TestCase):
    def test_display_records_all(self):
        student = Student()
        self.assertEqual(student.display_records_all(),True)
        
    def test_display_records_sorted_by_email_address(self):
        student = Student()
        self.assertEqual(student.display_records_sorted_by_email_address)

    def test_add_new_student(self):
        student = Student()
        self.assertEqual(student.add_new_student(), False)
        

        

if __name__ == '__main__':
    unittest.main()