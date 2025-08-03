"""
Task 3: Hotel Room Allocation
Hill View Hotel tracked room occupancy as follows:

rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}

During the evening:
- A new guest "Daisy" was checked into room 104.
- Room 102 was vacated after Bob checked out.
- A last-minute cancellation happened for the most recently allocated room just after the manager backed up the current allocation.
"""

rooms = {"101": "Alice", "102": "Bob", "103": "Charlie"}

print("Question One")
rooms_updated = rooms.update({"104": "Daisy"})
print(rooms)

rooms_allocated = rooms.copy()

print("Question Two")
rooms_vacated = rooms.pop("102")
print(rooms)

print("Question Three")
print(rooms_allocated)




