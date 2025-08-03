"""
Task 1: Music Concert Ticketing System
During the Jos Summer Music Concert, ticket sales were recorded as follows:

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

Later in the day:
- A new "Backstage" experience with 10 tickets was introduced.
- The "Student" category sold out completely.
- The team wanted to keep a record of the day’s sales before preparing for next week’s concert.
"""

tickets = {"VIP": 50, "Regular": 150, "Student": 75}


tickets["Backstage"] = 10
print(tickets)

record = tickets.copy()

tickets.pop("Student")
print(tickets)

print(record)



