# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   IB, 5/27/2024, Created Script
#   IB, 5/28/2024, Updated Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


class Person:
    """
    A class representing a person's data

    Properties:
    - student_first_name
    - student_last_name

    ChangeLog:
    IB,5/27/2024,Created Class
    """

    def __init__(self, student_first_name: str = '', student_last_name: str = ''):
          """
         This function is a constructor.

         ChangeLog: (Who, When, What)
         IB,5/27/2024,Created function
         IB,5/28/2024,Added Docstring

         :param student_first_name:
         :param student_last_name:
         """
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

    @property
    def student_first_name(self):
        """
        This function is for "getting" student_first_name.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring

        :return:
        """
        return self.__student_first_name.title()

    @student_first_name.setter
    def student_first_name(self, value: str):
        """
        This function is for "setting" student_first_name to add validation
        and error handling.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring

        :param value:
        :return:
        """
        if value.isalpha() or value == "":
            self.__student_first_name = value
        else:
            raise ValueError("The first name should only contain alphabetic characters")

    @property
    def student_last_name(self):
        """
        This function is for "getting" student_last_name.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring

        :return:
        """
        return self.__student_last_name.title()

    @student_last_name.setter
    def student_last_name(self, value: str):
        """
        This function is for "setting" student_first_name to add validation
        and error handling.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring

        :param value:
        :return:
        """
        if value.isalpha() or value == "":
            self.__student_last_name = value
        else:
            raise ValueError("The last name should only contain alphabetic characters")

    def __str__(self):
        """
        This method returns a string representation of class object.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring
        """
        return f'{self.student_first_name}, {self.student_last_name}'


class Student(Person):
    """
    A collection of data about students

    Properties:
    - course_name (str): The student's course to enroll

    ChangeLog:
    IB,5/27/2024,Created Class
    """

    def __init__(self, student_first_name: str = '', student_last_name: str = '', course_name: str = ''):
        """
        This function is a constructor.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring

        :param student_first_name:
        :param student_last_name:
        :param course_name:
        """
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        """
        This function is for "getting" course_name.

        :return:
        """
        return self.__course_name

    @course_name.setter
    def course_name(self, value: str):
        """
        This function is for "setting" course_name to add validation
        and error handling.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring

        :param value:
        :return:
        """
        if value.isalpha() or value == "":
            self.__course_name = value
        else:
            raise ValueError("The course name should only contain alphabetic characters")

    def __str__(self):
        """
        This method returns a string representation of class object.

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function
        IB,5/28/2024,Added Docstring
        """
        return f'{self.student_first_name}, {self.student_last_name}, {self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    IB,5/27/2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
         IB,5/27/2024,Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed is False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file.closed is False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    IB, 5/27/2024,Created Class
    IB, 5/27/2024,Added menu output and input functions
    IB, 5/27/2024,Added a function to display the data
    IB, 5/27/2024,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        IB,5/27/2024,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


"""
This is the start of the main body.
When the program starts, the file data will be read into a list of lists.
"""
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)


while True:
    """
    This while loop will present a menu of choices to a user and ask the user to select a choice of 1,2,3, or 4.
    
    If the user selects menu choice 1: the user will input student data to be enrolled in a course
    If the user selects menu choice 2: the current student names and courses they are enrolled in will be presented.
    If the user selects menu choice 3: The student names and courses they are enrolled in will be saved to a json file.
    If the user selects menu choice 4: The program will end.
    """

    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
