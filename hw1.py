# 4

# import random

# computer_guess = random.randint(1, 20)

# for shot in range (5):
#     user_guess =int ( input ("guess a number between 1 and 20: (you have 5 shots)"))

#     if user_guess > computer_guess:
#         print ("the number is smaller")
#     elif user_guess < computer_guess:
#         print ("the number is bigger")
#     elif user_guess == computer_guess:
#         print ("you won")
#         break
# else:
#     print ("you lost")


# 5 
# library = {}


# while True:
#     user_choice = int (input ("choose to 1)add items 2)search items 3)show items 4)exit. (for each action, type the number)"))

#     if user_choice == 1:
#         name = input ("type the books name:")
#         author = input ("type the authors name:")
#         library[name] = author
        

#     elif user_choice == 2:
#         search = input ("search the item:")
#         if search in library:
#             print (f"the item exists, by:, {library[search]}")
#         else:
#             print ("there is no such item")

#     elif user_choice == 3:
#         print (library)

#     elif user_choice == 4 :
#         print ("good luck")
#         break




#6

# inventory = {}

# with open("inventory.txt", "r") as file:
#     for line in file:
#         name, inventory_count = line.strip().split(" - ")
#         inventory[name] = int(inventory_count)

# while True:
#     user_choice = int (input ("choose the action: 1)add 2)sell 3)search 4)show 5)save 6)report 7)exit"))

#     if user_choice == 1:
#         name = input ("type the products name:")
#         inventory_count = int (input ("type the inventory_count:"))
#         if name in inventory:
#             inventory[name] += inventory_count
#         else: 
#             inventory[name] = inventory_count

#     elif user_choice == 2:
#         name = input ("type the products name:")
#         if name in inventory:
#             sell_count = int(input ("type the count you wanna sell:"))
#             if inventory[name] >= sell_count:
#                 inventory[name] -= sell_count
#                 if inventory[name] == 0:
#                     del inventory[name]
        
#             else:
#                 print ("not enough number to sell")
#         else:
#             print ("the product does not exist")

#     elif user_choice == 3:
#         name = input ("search the product:")
#         if name in inventory:
#             print (inventory[name])
#         else:
#             print ("the product does not exist")

#     elif user_choice == 4:
#         print (f"here is the inventory, {inventory}")

#     elif user_choice == 5:
#         with open("inventory.txt", "w") as file:
#             for name, inventory_count in inventory.items():
#                 file.write(f"{name} - {inventory_count}\n")
#                 print("done")

#     elif user_choice == 6:
#         total_products = len (inventory)
#         total_count = sum(inventory.values())
#         maximum_count = max(inventory.values())
#         minimum_count = min(inventory.values())

#         print (f"the total number of products is: {total_products}\nthe total count is: {total_count}\nthe maximum amount of one product is: {maximum_count}\nthe minimum amount of a product is: {minimum_count}")

#     elif user_choice == 7:
#         print ("good luck")
#         break


