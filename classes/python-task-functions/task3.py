#  Task 3: Expense Tracker
def record_expenses(expenses, **items):
    """
    Record multiple expenses in a temporary expense dictionary.
    
    Parameters:
    expenses: Existing dictionary to store expenses.
   items: Key-value pairs of expenses (category=amount).
    
    Example:
        expenses = {}
        record_expenses(expenses, food=2500, transport=1500, books=3000)
       print(expenses[“food”]) # should return 2500 
    """

    
    expenses.update(items)
    print(expenses)
    print(expenses['food'])

expenses = {}
record_expenses(expenses, food=2500, transport=1500, books=3000)
