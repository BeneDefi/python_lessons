library = ["python for beginners", "data structures in c", "ai basics"]
borrowed_books = {}
student_id = 1

def start():
	while True:
		print("""
			1. Display all Books
			2. Add Books
			3. Borrow Books
			4. Return Books
			5. List of Borrowed Books
			6. List of Students that Borrowed Books
			7. Terminate session.
             """)
		user_choice = int(input(" "))
		call_function(user_choice)

def call_function(user_choice):
	if user_choice == 1:
		display_books()
	elif user_choice == 2:
		book_name = input("Book to add: ").lower().strip()
		add_book(book_name)
	elif user_choice == 3:
		book_name = input("Book to borrow: ").lower().strip()
		borrow_book(book_name)
	elif user_choice == 4:
		book_returned = input("Enter title of book to return: ").lower().strip() 		
		return_book(book_returned)
	elif user_choice == 5:
		borrowed_books_list()
	elif user_choice == 6:
		student_list()
	elif user_choice == 7:
		terminate_session()
	else:
		print("Invald selection")
		
def display_books():
	if len(library) != 0:
		for book in library:
			print(f"Book Available: {book}")

def add_book(book_name):
	if book_name in library:
		print("Book already exist")
	else:
		library.append(book_name)
		print(f"{book_name} added successfully")

def borrow_book(book_name):
	global student_id
	if book_name in library:
		library.remove(book_name)
		borrowed_books[student_id] = book_name
		student_id +=1
		print(f"{borrowed_books} borrowed successfully")
	else:
		print("Book not in Library")

def return_book(book_returned):
	if len(borrowed_books) != 0:
		for student_id, book in list(borrowed_books.items()):
			if book_returned in book:
				library.append(book)
				del borrowed_books[student_id]
				print(f"Borrowed books: {borrowed_books}")
				print(f"Library: {library}")
			else:
				print(f"'{book_returned}' was not found in borrowed books.")
	else:
		print("Cannot Return!, Borrowed books list empty.")

def borrowed_books_list():
	if len(borrowed_books) != 0:
		for student_id, book in borrowed_books.items():
			print(f"Student ID: {student_id}, Book Borrowed: {book}")
	else:
		print("Borrowed books list empty.")

def student_list():
	if len(borrowed_books) != 0:
		print(f"Number of student(s) that borrowed books are:", len(borrowed_books))
	else:
		print("Borrowed books list empty")

def terminate_session():
	print("Terminating session. Goodbye!")
	exit()

start()
