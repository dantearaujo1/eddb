from eddb.student.student_interface.student_repository import StudentRepository
from eddb.util.util import open_json,write_data
from eddb.model.usuario import Usuario
class StudentRepositoryConcrete(StudentRepository):
    def __init__(self, file):
        self.file = file

    def __open(self):
        json_data = None
        if self.file:
            json_data = open_json(self.file)
        return json_data
    """
       Return a list of dictionary objects that with data
       """

    def get_all(self):
        json_data = self.__open()
        if json_data:
            return json_data["students"]
        return []