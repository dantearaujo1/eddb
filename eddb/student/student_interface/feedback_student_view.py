from abc import ABC,abstractmethod
import time

class FeedbackStudentView(ABC):
    @abstractmethod
    def show_students(self, student):
        pass

class SuccessFeedbackAddStudentView(FeedbackStudentView):

    def show_students(self,students):
        print(f"Parabéns, você adicionou o estudante: ")
        print(f"Nome: {students[0].name}")
        print(f"Sobrenome: {students[0].surname}")
        time.sleep(3)

class FailureFeedbackAddStudentView(FeedbackStudentView):

    def show_students(self,students):
        print(f"Não foi possível adicionar o estudante!")
        time.sleep(3)
