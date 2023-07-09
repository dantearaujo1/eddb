'''
    Class that will handle our loans management using JSON as the stored
    File
'''
from eddb.loan.loan_interface.loan_repository import LoanRepository
from eddb.loan.loan_model import Loan
from eddb.util.util import open_json,write_data

class LoanRepositoryConcrete(LoanRepository):
    def __init__(self, file):
        self.file = file

    def __open(self):
        json_data = None
        if self.file:
            json_data = open_json(self.file)
        return json_data

    def __loan_to_JSON(self,loan):
        return vars(loan)()

    def __JSON_to_loan(self,json):
        return Loan(json["id"],json["book_id"],json["student_id"],json["loan_date"],json["payday"],json["status"])

    def get_all(self):
        """
        Return a list of loan objects or empty if not found
        """
        json_data = self.__open()
        if json_data:
            loans = json_data["loans"]
            loans = list(map(lambda loan: self.__JSON_to_loan(loan),loans))
            return loans
        return []

    def get_by_ID(self,ID):
        """
        Return a list with loan objects or empty if not found
        """
        json_data = self.__open()
        if json_data:
            loans = json_data["loans"]
            for loan in loans:
                if loan["ID"] == ID:
                    return [self.__JSON_to_loan(loan)]
        return []

    def get_all_by_book_id(self,ID):
        """
        Return a list with loan objects or empty if not found
        """
        json_data = self.__open()
        list_of_loans = []
        if json_data:
            loans = json_data["loans"]
            for loan in loans:
                if loan["book_id"] == ID:
                    list_of_loans.append(self.__JSON_to_loan(loan))
        return list_of_loans

    def get_all_by_student_id(self,ID):
        """
        Return a list with loan objects or empty if not found
        """
        json_data = self.__open()
        list_of_loans = []
        if json_data:
            loans = json_data["loans"]
            for loan in loans:
                if loan["student_id"] == ID:
                    list_of_loans.append(self.__JSON_to_loan(loan))
        return list_of_loans

    def add_item(self,item):
        '''
        Add a loan item into our JSON database
        '''
        json_data = self.__open()
        incoming_loan = self.__loan_to_JSON(item)
        items = []
        if json_data:
            items = json_data["loans"]
            for loan in items:
                if loan["id_book"] == incoming_loan["id_book"] and loan["id_student"] == incoming_loan["id_student"]:
                    return False
                if loan["id"] == incoming_loan["id"]:
                    return False
            items.append(incoming_loan)
            json_data["loans"] = items
            write_data(self.file,json_data)
            return True
        return False

    def update_item(self,edited):
        '''
        Update a loan item into our JSON database
        '''
        json_data = self.__open()
        incoming_loan = self.__loan_to_JSON(edited)
        items = []
        if json_data:
            items = json_data["loans"]
            for loan in items:
                if loan["id"] == incoming_loan["id"]:
                    loan["id_book"] = incoming_loan["id_book"]
                    loan["id_student"] = incoming_loan["id_student"]
                    loan["loan_date"] = incoming_loan["loan_date"]
                    loan["payday"] = incoming_loan["payday"]
                    loan["status"] = incoming_loan["status"]
            json_data["loans"] = items
            write_data(self.file,json_data)
            return True
        return False

    def delete_item(self,loan):
        '''
        Delete loan from JSON
        '''
        json_data = self.__open()
        ongoing_loan = self.__loan_to_JSON(loan)
        items = []
        if json_data:
            items = json_data["loans"]
            for loan in items:
                if loan["id"] == ongoing_loan["id"]:
                    items.remove(loan)
            json_data["loans"] = items
            write_data(self.file,json_data)
            return True
        return False

    def delete_all_with_book_id(self,ID):
        json_data = self.__open()
        items = []
        if json_data:
            items = json_data["loans"]
            for loan in items:
                if loan["id_book"] == ID:
                    items.remove(loan)
            json_data["loans"] = items
            write_data(self.file,json_data)
            return True
        return False

    def delete_all_with_student_id(self,ID):
        json_data = self.__open()
        items = []
        if json_data:
            items = json_data["loans"]
            for loan in items:
                if loan["id_student"] == ID:
                    items.remove(loan)
            json_data["loans"] = items
            write_data(self.file,json_data)
            return True
        return False
