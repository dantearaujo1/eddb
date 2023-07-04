from abc import ABC,abstractmethod
import time

class FeedbackStudentView(ABC):
    @abstractmethod
    def show_students(self, student):
        pass
