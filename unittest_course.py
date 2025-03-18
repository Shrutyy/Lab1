import unittest
import time
import csv


class Course:

    def __init__(self):
        self.course_dict = dict()
    
    def display_courses_all(self): #display the course details
        print("Courses are as follows:\n")
        print("COurse_Id\tCredits\tCourse_name")

        for key, entry in self.course_dict.items():
            print(str(key)+","+str(entry[0])+","+str(entry[1]))
        return True
    
    def display_courses(self, course_id): #disoplay the time to run
        start = time.time()
        course_record = self.course_dict[course_id]
        end = time.time() - start
        print("It took " + str(end-start) + " seconds to get the course record for course id: " + str(course_id))
        
        print("Course is as follows:\n")
        print("COurse_Id\tCredits\tCourse_name")
        print(str(course_id)+","+str(course_record[0])+","+str(course_record[1]))
        return True

    def display_records_sorted_by_course_name(self): #function for sorting the records
        start = time.time()
        sorted_dict_by_course_name = dict(sorted(self.course_dict.items(), key=lambda item: item[1][1]))
        end = time.time()
        print("It took " + str(end-start) + " seconds to sort the course records by course name.")
        print("Courses are as follows:\n")
        print("CourseName\tCourse_Id\tCredits")

        for course_id, course_record in sorted_dict_by_course_name.items():
            print(str(course_record[1]) + "," + str(course_id)+","+str(course_record[0]))
        return True
            
    
    def add_new_course(self, course_id, credits, course_name): #to add a new course to the curriculum
        if course_id is None or str(course_id)=="":
            print("It is mandatory to enter a non empty and non null course id!! Please try again.")
            return
        self.course_dict[course_id] = [credits, course_name]
        print("Course details are added.")
        return True
    
    def delete_course(self, course_id): #to delete a new course from the curriculum
        del self.course_dict[course_id]
        return True



class TestCourse(unittest.TestCase):
    def test_display_courses_all(self):
        course = Course()
        self.assertEqual(course.display_courses_all(),True)
        
    def test_display_records_sorted_by_course_name(self):
        course = Course()
        self.assertEqual(course.display_records_sorted_by_course_name(), True)
        

        

if __name__ == '__main__':
    unittest.main()