import datetime
class Library:
    author=''
    title=''
    counter = 0
    availablebooks=[]
    book=[]
    year=0
    x = datetime.datetime.now()
    def __init__(self,title,author,year):
        self.author=author
        self.title=title
        self.year = year
        self.book.append(title)
        self.book.append(author)
        self.book.append(year)
        self.availablebooks.append(title)
        self.counter += 1
    def set_year(self,year):
        if (year > self.x.year) or (year < 1990):
            print("Invalid Year!!")
        else:
            self.year = year
            self.book.append(year)
    def get_year(self):
    	return self.year
    def displayAvailablebooks(self):
        print("Choose a book:")
        for book in self.availablebooks:
            print(book)
    def borrowBook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("You got the book!")
            self.availablebooks.remove(requestedBook)
        else:
                  print("Sorry the book not Found")
    def s_year(self,year):
    	if year in self.book:
    		print("Books published in ",year," are:")
    		print("Title: ",self.title," Author: ",self.author," Year:",self.year)
    	else:
    		print("Book not Found")
            


def main():            
    b1=Library("Harry potter","J. K. Rolling",1997)
    b2=Library("The Da Vinci Code","Dan Brown",2003)
    b3=Library("Life of PI","Yann Martel",2001)
    print("====== Welcom to the Library we have a total of 3 books =======")
    while True:
            print("What would you like to do? \n 1. Borrow a book \n 2. Search a book by year \n")
            choice=int(input("Enter your Choice, -1 to stop: "))
            if choice==1:
                b3.displayAvailablebooks()
                borrow = input()
                b3.borrowBook(borrow)
            elif choice==2:
            	x=int(input("Enter Year: "))
            	b3.s_year(x)
            elif choice==-1:
                break
            else:
            	print("Invlid Choice")
                  
main()

#Sample OutPut
# ====== Welcom to the Library we have a total of 3 books =======
# What would you like to do?     
#  1. Borrow a book 
#  2. Search a book by year      

# Enter your Choice, -1 to stop: 3
# Invlid Choice
# What would you like to do?     
#  1. Borrow a book 
#  2. Search a book by year      

# Enter your Choice, -1 to stop: 2
# Enter Year: 2001
# Books published in  2001  are:
# Title:  Life of PI  Author:  Yann Martel  Year: 2001
# What would you like to do? 
#  1. Borrow a book 
#  2. Search a book by year 

# Enter your Choice, -1 to stop: 1
# Choose a book:   
# Harry potter     
# The Da Vinci Code
# Life of PI       
# Life of PI
# You got the book!
# What would you like to do?
#  1. Borrow a book
#  2. Search a book by year

# Enter your Choice, -1 to stop: 1
# Choose a book:
# Harry potter
# The Da Vinci Code
# Harry potter
# You got the book!
# What would you like to do?
#  1. Borrow a book
#  2. Search a book by year

# Enter your Choice, -1 to stop: 1
# Choose a book:
# The Da Vinci Code
# The Da Vinci Code
# You got the book!
# What would you like to do?
#  1. Borrow a book
#  2. Search a book by year

# Enter your Choice, -1 to stop: -1
                   

