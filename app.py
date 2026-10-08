import json
import random
import os

if not os.path.exists("data"):     #if the data folder does not exist, the program makes it.
    os.mkdir("data")


if not os.path.exists("data/karvands.json"):       #like the one above, this also makes the json file if it does not exist.
    with open("data/karvands.json", "w") as file:
        json.dump([], file)




karvands = []
try:
    with open("data/karvands.json", "r") as file:
        karvands = json.load(file)

except (json.JSONDecodeError, FileNotFoundError):
    print("the JSON file is empty or damaged. a new file is getting ready.")

    karvands = []

    with open("data/karvands.json", "w") as file:
        json.dump(karvands, file, indent=2)
if not karvands:                              #or could be writtern >> if len(karvands) == 0: ....
    print ("the karvands file is empty.")

while True:

    user_choice = int(input(
        "choose to 1)add karvands 2)edit a karvand 3)search a karvand by karvands id 4)search a karvand by skills 5) show all karvands 6)delete a karvand 7)exit 8)report "))
    if user_choice == 1:
        name = input("enter the full name:")
        if name == "exit":
            break
        id = random.randint(1000,9999)
        while True:
                existsance = False
                for karvand in karvands:
                    if karvand["id"]== id:
                        existsance = True
                        break
                if existsance == False:
                    break
                id = random.randint(1000,9999)

                    
        email_address = input("enter karvands email address: ")
        city = input("enter karvands city:")
        education = input("enter karvands education:")
        study_field = input ("enter the field karvand studies: ")
        skills = []
        while True:
            skills_name = input("enter karvands skill:(enter exit to break) ")
            if skills_name == "exit":
                break
            skills_level = input("enter skills level:")
            while True:
                skills_score = int(input("enter skills score (0 to 100):"))
                if 0<= skills_score <= 100:
                    break
                elif skills_score < 0 or skills_score > 100:
                    skills_score = int(input("skills score must be between 0 to 100:"))
                    break
            skills_dict = {
                "skill_name" : skills_name,
                "skill_level": skills_level,
                "skill_score": skills_score
            }

            skills.append(skills_dict)


        karvand = {
            "id": id,
            "name": name,
            "email_address": email_address,
            "city": city,
            "education": education,
            "study_field": study_field,
            "skills": skills
            
        }

        karvands.append(karvand)

        with open("data/karvands.json", "w") as file:
            json.dump(karvands, file, indent=2)

  
    elif user_choice == 3:
        try:                  #using this, if the user types sth but number, wont be an error.
            user_search = int(input("search the id:"))
        except ValueError:
            print("please enter a number")
            continue
        for karvand in karvands:
           if user_search == karvand["id"]:
                           print(
                               f"the karvand exists, here is the name: {karvand["name"]}")
                           break
        else:
             print("such a karvand does not exist")

    elif user_choice == 4:
    
            found = False                
            user_search = input(
                "enter the skill or skills which you desire:").split(",")
            for karvand in karvands:
                for skill in user_search:
                    if skill in karvand["skills"]:
                
                        print(
                            f"such a karvand exists: {karvand["name"], karvand["skills"]}")
    
                        found = True
                        break
                        
            if not found:  #the same as if found == false (but more functional)
                print("such a karvand does not exist")
    
