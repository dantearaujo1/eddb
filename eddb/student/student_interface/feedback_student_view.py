from abc import ABC,abstractmethod
class FeedbackStudentView(ABC):
    @abstractmethod
    def show_students(self, student):
        pass
