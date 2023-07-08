from eddb.student.student_view import StudentView
from eddb.student.student_controller_concrete import StudentControllerConcrete
from eddb.student.student_repository_concrete import StudentRepositoryConcrete
from eddb.loan.loan_repository_concrete import LoanRepositoryConcrete

class StudentComposer:
    @staticmethod
    def create() -> StudentView:
        repository = StudentRepositoryConcrete("eddb/db_teste.json")
        loan_repo = LoanRepositoryConcrete("eddb/db_teste.json")
        controller = StudentControllerConcrete(repository,loan_repo)
        view = StudentView(controller)
        controller.set_view(view)
        return view
