from eddb.student.student_view import StudentView
from eddb.student.student_controller_concrete import StudentControllerConcrete
from eddb.student.student_repository_concrete import StudentRepositoryConcrete

class StudentComposer:

    @staticmethod
    def create() -> StudentView:
        repository = StudentRepositoryConcrete()
        controller = StudentControllerConcrete(repository)
        view = StudentView(controller)
        controller.set_view(view)
        return view
