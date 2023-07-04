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
            students = list(map(lambda student: self.__JSON_to_student(student),students))
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
