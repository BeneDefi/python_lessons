"""
Task 5: Online Shopping Cart
Two friends, Daniella and Godiya, walk into a mall and pick up just one cart to shop with.
Once inside, they split up and go to different wings of the mall, 
but since they share the same cart, everything either of them adds goes into the same cart.

cart = {}
godiya = ???
daniella = ???

During shopping:
- Daniella finds and adds "Shoes" (2 quantity).
- Godiya picks up "Watch" (1 quantity).
- Daniella later changes her mind and removes "Shoes" from the cart.
- Godiya also adds a "Bag" (1 quantity), then later removes it.

At checkout:
- The store takes a snapshot of the final order as an order summary for records.
- The shared cart is then emptied to prepare it for the next customer.
"""

cart = {}

godiya = {}
print("Godiya:", godiya)

daniella ={}
print("Daniella:",daniella)

daniella["first_shoe"], daniella["second_shoe"] = 1,1
godiya["watch"] = 1

cart.update(daniella)
cart.update(godiya)

cart = {
    "godiya": godiya,
    "daniella": daniella
}
print(cart)

daniella = cart["daniella"].pop("second_shoe")
print(cart)

godiya = cart["godiya"].update({"Bag":1})
print(cart)

godiya = cart["godiya"].pop("Bag")
print(cart)

summary_of_cart = cart

print("Godiya == Daniella", len(cart["godiya"]) == len(cart["daniella"]))
print(summary_of_cart)
cart.clear()


# print(godiya)
# print(daniella)
# print(godiya == daniella) # should return true
# print(summary_of_cart)
# print(cart)
