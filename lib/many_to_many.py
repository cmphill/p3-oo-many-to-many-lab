class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract (self, book, date, royalties):
        return Contract(self,book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
        
    def authors(self):
        return [contract.author for contract in self.contracts()]
        



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    def contracts_by_date():
        return sorted(Contract.all, key=lambda c: c.date)
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, set_date):
        if isinstance(set_date, str):
            self._date = set_date
        else:
            raise Exception
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, new_royalties):
        if isinstance(new_royalties, int):
            self._royalties = new_royalties
        else:
            raise Exception ('not a valid royalty')

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, new_book):
        if isinstance(new_book, Book):
            self._book = new_book
        else:
            raise Exception ("not a valid book")
        
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception
        self._author = new_author