"""
Task 4: Tech Conference Registration
The Jos Tech Conference registered participants under ticket categories:

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

During the first day:
- A "Guest" participant named "Daisy" joined.
- The "Student" participant canceled their registration.
- The organizers created a record for the day before removing the most recently added participant from the live system.
"""

participants = {"VIP": "Alice", "Regular": "Bob", "Student": "Charlie"}

print("Question One")
added_guest = participants.update({"Guest": "Daisy"})
print(participants)

total_participants = participants.copy()

print("Question Two")
cancelled_participants = participants.pop("Student")
print(participants)

print("Question Three")
recently_removed = participants.popitem()
print(participants)
print(total_participants)

# print(participants_snapshot)
# print(participants)
