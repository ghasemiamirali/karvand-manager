import json
import random
import os

if not os.path.exists("data"):     #if the data folder does not exist, the program makes it.
    os.mkdir("data")


if not os.path.exists("data/karvands.json"):       #like the one above, this also makes the json file if it does not exist.
    with open("data/karvands.json", "w") as file:
        json.dump([], file)

    

