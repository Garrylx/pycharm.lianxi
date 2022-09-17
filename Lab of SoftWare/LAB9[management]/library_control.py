class Book(object):

    def __init__(self,code,title,):
        self.__code = code
        self.__title = title
        self.__status = True

    def get_book_code(self):
        return self.__code

    def get_book_title(self):
        return self.__title

    def is_available(self):
        return self.__status

    def borrow_book(self):
        self.__status = False

    def return_book(self):
        self.__status = True

    def __str__(self):
        if self.__status == True:
            return "%s, %s (Available)"%(self.__title,self.__code)
        else:
            return "%s, %s (On Loan)"%(self.__title,self.__code)

class Member(object):

    def __init__(self,member_id,name,on_loan_books_list=None):
        self.__member_id = member_id
        self.__name = name
        self.__on_loan_books_list = on_loan_books_list
        if self.__on_loan_books_list == None:# 赋值给None 在创建多个对象时，防止两个对象共用一个列表
            self.__on_loan_books_list = []
        else:
            pass

    def get_name(self):
        return self.__name

    def get_member_id(self):
        return self.__member_id

    def get_on_loan_books(self):
        return self.__on_loan_books_list

    def borrow_book(self, book):
        book.borrow_book()
        if book.get_book_title() not in self.__on_loan_books_list:
            self.__on_loan_books_list.append(book.get_book_title())

    def return_book(self, book):
        book.return_book()
        if book.get_book_title() in self.__on_loan_books_list:
            self.__on_loan_books_list.remove(book.get_book_title())

    def __str__(self):
        str1 = ""
        str1 += (self.__name + "\n" + "On loan book(s):" + '\n')
        if self.__on_loan_books_list != []:
            for i in range(len(self.__on_loan_books_list)):
                if i != len(self.__on_loan_books_list)-1:
                    str1 += (self.__on_loan_books_list[i] + '\n')
                else:
                    str1 += self.__on_loan_books_list[i]
            return str1
        else:
            str1 += "-"
            return str1

class Record(object):

    def __init__(self,book,member,issue_date,is_on_loan=True):
        self.__book = book
        self.__member = member
        self.__is_on_loan = is_on_loan
        self.__issue_date = issue_date
        member.borrow_book(book)

    def get_member_id(self):
        return self.__member.get_member_id()

    def get_book_code(self):
        return self.__book.get_book_code()

    def get_issue_date(self):
        return self.__issue_date

    def is_on_loan(self):
        if self.__book.is_available() == True:
            return False
        else:
            return True

    def return_book(self):
        self.__member.return_book(self.__book)


    def __str__(self):
        return "%s, %s, issued date=%s" % (self.__member.get_name(), self.__book.__str__(), self.__issue_date)

class MyLibrary(object):

    def __init__(self,filename):
        self.__book__list = []
        self.__on_loan_records_list = []
        self.__record_list = []
        self.__dict_book = {}
        try:
            f = open(filename,"r")
            self.__book__list = f.readlines()
            print(str(len(self.__book__list))+" books loaded.\n",end="")
            for indexs in range(len(self.__book__list)):
                b = self.__book__list[indexs].split(",")
                if indexs != len(self.__book__list) - 1:
                    eachbook = Book(b[0], b[1][:-1])
                    self.__dict_book["book{}".format(indexs)] = eachbook
                else:
                    eachbook = Book(b[0], b[1])
                    self.__dict_book["book{}".format(indexs)] = eachbook
            f.close()
        except FileNotFoundError:
            print("ERROR: The file '%s' does not exist."%filename)

    def show_all_books(self):
        for indexs in range(len(self.__book__list)):
            b = self.__book__list[indexs].split(",")
            if indexs != len(self.__book__list)-1:
                eachbook = Book(b[0],b[1][:-1])
            else:
                eachbook = Book(b[0],b[1])
            print(eachbook)

    def find_book(self, code):
        for info in self.__dict_book.values():
            if info.get_book_code() == code and info.is_available() == True:
                return info
            else:
                pass

    def borrow_book(self, book = None,member="",issue_date=""):
        if book != None and book in [x for x in self.__dict_book.values()]:
            r1 = Record(book,member,issue_date)
            self.__on_loan_records_list = self.__on_loan_records_list + [r1]
            self.__record_list = self.__record_list + [r1]
            print("%s is borrowed by %s."%(book.get_book_title(),member.get_name()))
        else:
            print("ERROR: could not issue the book.")

    def show_available_books(self):
        lists = []
        for book in self.__dict_book.values():
            if book.is_available() == True:
                lists.append(book)
            else:
                pass
        for book in lists:
            print(book)

    def find_record(self, code):
        for rec in self.__on_loan_records_list:
            if rec.get_book_code() == code:
                return rec
        else:
            return None

    def return_book(self, record = None):
        if record != None and record in self.__on_loan_records_list:
            record.return_book()
            self.__on_loan_records_list.remove(record)
            print("%s is returned successfully." % record.get_book_code())
        else:
            print("ERROR: could not return the book.")

    def show_on_loan_records(self):
        for rec in self.__on_loan_records_list:
            print(rec)

    def show_all_records(self):
        for rec in self.__record_list:
            print(rec)


