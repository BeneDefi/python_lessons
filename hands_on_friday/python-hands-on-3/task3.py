"""
Task 4: Pocket Money Records
You're building a small tracker for your younger sibling's weekly pocket money.
The amounts (in naira) for the past 5 weeks are stored like this:
money = [1000, 1200, 800, 1500, 1100]

1. Calculate and display the total amount received so far.
2. A mistake was made in the third week's entry (800). It should have been 1000. Fix it.
3. Display the list in reverse order to check most recent payments first.

→ Perform the corrections and computations, and print all results.
"""

money = [1000, 1200, 800, 1500, 1100]

total = money[0] + money[1] + money[2] + money[3] + money[4]
print(f"The total money recived is ₦ {total}")

money[2] = 1000
print(money)

print(money[::-1])






