'''
    Class that will handle our book management using JSON as the stored
    File
'''
from eddb.util.util import open_json,write_data
from eddb.book.book_interface.book_repository import BookRepository
from eddb.book.book_model import Book

class BookRepositoryConcrete(BookRepository):
    def __init__(self,file):
        self.file = file

    def __open(self):
        json_data = None
        if self.file:
            json_data = open_json(self.file)
        return json_data

    def __book_to_JSON(self,book):
        return vars(book)()

    def __JSON_to_book(self,json):
        return Book(id=json["id"],title=json["title"],author=json["author"])

    def get_all(self):
        '''
        Return a list of dictionary objects that with data
        '''
        json_data = self.__open()
        if json_data:
            books = json_data["books"]
            books = list(map(lambda b: self.__JSON_to_book(b),books))
            return books
        return []

    def get_by_id(self,ID):
        json_data = self.__open()
        items = []
        if json_data:
            items = json_data["books"]
            for book in items:
                if book["id"] == ID:
                    return [self.__JSON_to_book(book)]
        return []

    def get_by_title(self,title):
        json_data = self.__open()
        items = []
        if json_data:
            items = json_data["books"]
            for book in items:
                if book["title"] == title:
                    return self.__JSON_to_book(book)
        return []

    def add_item(self,item):
        '''
        Add a book item into our JSON database
        '''
        json_data = self.__open()
        incoming_book = self.__book_to_JSON(item)
        items = []
        if json_data:
            items = json_data["books"]
            for book in items:
                if book["title"] == incoming_book["title"] or book["id"] == incoming_book["id"]:
                    return False
            items.append(incoming_book)
            json_data["books"] = items
            write_data(self.file,json_data)
            return True
        return False

    def update_item(self,edited):
        '''
        Update a book item into our JSON database
        '''
        # TODO: talvez a nesse caso a ideia do dicionário seria boa
        # ja que conhecemos de antemão o id do livro
        json_data = self.__open()
        incoming_book = self.__book_to_JSON(edited)
        items = []
        if json_data:
            items = json_data["books"]
            for book in items:
                if book["id"] == incoming_book["id"]:
                    book["title"] = incoming_book["title"]
                    book["author"] = incoming_book["author"]
            json_data["books"] = items
            write_data(self.file,json_data)
            return True
        return False

    def delete_item(self,book):
        '''
        Delete book from JSON
        '''
        json_data = self.__open()
        ongoing_book = self.__book_to_JSON(book)
        items = []
        if json_data:
            items = json_data["books"]
            for book in items:
                if book["id"] == ongoing_book["id"]:
                    items.remove(book)
            json_data["books"] = items
            write_data(self.file,json_data)
            return True
        return False


