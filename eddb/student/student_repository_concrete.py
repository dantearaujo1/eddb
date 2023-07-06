'''
    Class that will handle our data management using JSON as the stored
    File
'''

from eddb.student.student_interface.student_repository import StudentRepository
from eddb.util.util import open_json,write_data
from eddb.student.student_model import Student

class StudentRepositoryConcrete(StudentRepository):
    def __init__(self, file):
        self.file = file

    def __open(self):
        json_data = None
        if self.file:
            json_data = open_json(self.file)
        return json_data

    def __student_to_JSON(self,student):
        return vars(student)()

    def __JSON_to_student(self,json):
        return Student(json["id"],json["name"],json["surname"],json["email"])

    def get_all(self):
        '''
        Return a list of dictionary objects that with data
        '''
        json_data = self.__open()
        if json_data:
            students = json_data["students"]
            students = list(map(lambda s: self.__JSON_to_student(s),students))
            return students
        return []

    def get_by_id(self,ID):
        json_data = self.__open()
        if json_data:
            students = json_data["students"]
            result = []
            for student in students:
                if student["id"] == int(ID):
                    result.append(self.__JSON_to_student(student))
        return result

    def add_item(self,item):
        '''
        Add a student item into our JSON database
        '''
        json_data = self.__open()
        incoming_student = self.__student_to_JSON(item)
        items = []
        if json_data:
            items = json_data["students"]
            for student in items:
                if student["id"] == incoming_student["id"]:
                    return False
            items.append(incoming_student)
            json_data["students"] = items
            write_data(self.file,json_data)
            return True
        return False

    def update_item(self, edited, old_id):
        '''
        Update a student item into our JSON database
        '''
        json_data = self.__open()
        incoming_student = self.__student_to_JSON(edited)
        items = []
        if json_data:
            items = json_data["students"]
            for student in items:
                if student["id"] == old_id:
                    student["id"] = incoming_student["id"]
                    student["name"] = incoming_student["name"]
                    student["surname"] = incoming_student["surname"]
                    student["email"] = incoming_student["email"]
            json_data["students"] = items
            write_data(self.file,json_data)
            return True
        return False

    def delete_item(self,student):
        '''
        Delete student item from JSON
        '''
        json_data = self.__open()
        ongoing_student = self.__student_to_JSON(student)
        items = []
        if json_data:
            items = json_data["students"]
            for student in items:
                if student["id"] == ongoing_student["id"]:
                    items.remove(student)
            json_data["students"] = items
            write_data(self.file,json_data)
            return True
        return False
