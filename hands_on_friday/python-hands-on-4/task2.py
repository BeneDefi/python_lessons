"""
Task 2: Airport Luggage Tracker
At Jos Airport, the luggage department tracked passengers and their luggage weights:

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

- you need to map each user to its corresponding luggage weight value.

Before the flight took off:
- A late passenger "Daisy" checked in with 20kg of luggage.
- Bob’s luggage went missing.
- The staff prepared a daily report before resetting for the next flight.
"""

luggage = [("Alice", 23),( "Bob", 18), ("Charlie", 25)]

print("Question One")
luggage = dict(luggage)
print(luggage)

print("Question Three")
luggage_update = luggage.update({"Daisy": 20})
print(luggage)

report = luggage.copy()

print("Question Four")
luggage_missing = luggage.pop("Bob")
print(luggage)

print("Question Four")
print(report)



