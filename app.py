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

    elif user_choice == 2:
                             
        try:     #using this, if we have sth but a number, the code wont crash.
             id_search = int(input("enter the karvands id to edit the info:"))
        except ValueError:
            print ("enter a number as an id:")
            continue

        for karvand in karvands:

            if id_search == karvand["id"]:
                user_choice2 = int(input(
                    "the karvand exist, choose to edit: 1)name 2)email 3)city 4)education 5)skills:"))
                if user_choice2 == 1:
                    new_name = input("enter the new name:")
                    karvand["name"] = new_name
                    print("done")
                elif user_choice2 == 2:
                    new_email = input("enter the new email address:")
                    karvand["email_address"] = new_email
                    print ("done")
                elif user_choice2 == 3:
                    new_city = input("enter the new city name:")
                    karvand["city"] = new_city
                    print("done")
                elif user_choice2 == 4:
                    new_education = input("enter the new education:")
                    karvand["education"] = new_education
                    print("done")
                elif user_choice2 == 5:
                    
                    new_skill_name = input("enter the new skill name:")
                    new_skill_level = input ("enter the new skill level: ")
                    new_skill_score = int (input ("enter the new skill score ( 0 to 100):"))
                    while True:
                        if 0 <= new_skill_score <= 100:
                            break
                        elif new_skill_score < 0 or new_skill_score > 100:
                            new_skill_score = int (input("the score must be between 0 to 100:"))
                            break
                    new_skills = {
                        "skill_name" : new_skill_name,
                        "skill_level": new_skill_level,
                        "skill_score": new_skill_score
                    }

                    karvand ["skills"].append(new_skills)
                    print("done")
                    break
                
        else:
            print("such a karvand does not exist")          # if the id is invalid >> this will be printed

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

    elif user_choice == 5:
        print(json.dumps(karvands, indent=2))

    elif user_choice == 6:
        name = input("enter the name you wish to delete:")
        for karvand in karvands:
            if name == karvand["name"]:
                karvands.remove(karvand)
                print("done")
                break
        else:
            print("such a karvand does not exist")

        with open("data/karvands.json", "w") as file:
            json.dump(karvands, file, indent=2)

    elif user_choice == 7:
        print("good luck")
        break

    elif user_choice == 8:

        if not os.path.exists("data/report.json"):       # if the report file does not exist, it makes it.

            with open("data/report.json", "w") as file:

                json.dump({}, file)

        skills_name = set()    # here I used set to avoid counting repeated skills.
                            # all of them went to a set and then I defined
                            # another variable and used len to count the items in skills_name
                            # then I put it in the report dictionary.
        cities = set()

        all_skills = []
        unique_skills = []        #for the report part >> showing the unique skills



        for karvand in karvands:

            for skill in karvand["skills"]:

                skills_name.add(skill["skill_name"])


        skill_score_total = 0

        skill_score_count = 0

        for karvand in karvands:

            for skill in karvand["skills"]:

                skill_score_total += skill["skill_score"]

                skill_score_count += 1


        if skill_score_count > 0:

            average_score = skill_score_total / skill_score_count

        else:

            average_score = 0


        total_skills = len(skills_name)

        for karvand in karvands:
            cities.add(karvand["city"])


        for karvand in karvands:
            for skill in karvand["skills"]:
                all_skills.append(skill["skill_name"])



        for skill in all_skills:
            if all_skills.count(skill) == 1:
                unique_skills.append(skill)


        report = {

            "total_karvands": len(karvands),

            "total_skills": total_skills,

            "scores_average": average_score,
            "cities": list(cities),                #we used list because we need to have names beside eachother
             "unique_skills" : unique_skills

        }


        with open("data/report.json", "w") as file:
            json.dump(report, file, indent=2)

