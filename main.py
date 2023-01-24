import uuid
import json

class About:

    def __init__(self, Name, Age, Profession, About_me, Organisation, Skills):
        self._id = uuid.uuid4()
        self.Name = Name
        self.Age = Age
        self.Profession = Profession
        self.About_me = About_me
        self.Organisation = Organisation
        self.Skills = Skills
        self.dict_1 = {}

    def entry(self):
        self.dict_1 = \
            {
                str(self._id): {
                    "Name": self.Name,
                    "Age": self.Age,
                    "Profession": self.Profession,
                    "About_me": self.About_me,
                    "Organisation": self.Organisation,
                    "Skills": self.Skills
                }
            }
        return self.dict_1, str(self._id)

try:
    with open("test.json", "r") as main_file:
        main_dict = json.load(main_file)
except ValueError:
    main_dict = {}


def mergeDictionary(dict_1, dict_2):
    dict_3 = {**dict_1, **dict_2}
    for key, value in dict_3.items():
        if key in dict_1 and key in dict_2:
            dict_3[key] = [value, dict_1[key]]
    return dict_3


def create_entry(Name = 0, Age = 0, Profession = 0, About_me = 0, Organisation = 0, Skills = 0):
    Name = str(input("Enter your name: "))
    Age = int(input("Enter your age: "))
    Profession = str(input("Enter your profession: "))
    About_me = input("Enter about you: ")
    Organisation = input("Enter the name of your organisation: ")
    Skills = input("Enter your skills: ")
    details = About(Name, Age, Profession, About_me, Organisation, Skills)
    input_dict, unique_id = About.entry(details)
    final_dict = mergeDictionary(input_dict, main_dict)
    with open("test.json", "w") as final_json:
        json.dump(final_dict, final_json)
    print("Your entry is saved & unique ID to edit or delete entry is: {}\n\n"
          "{}".format(unique_id, final_dict[unique_id]))


def view(key):
    print(main_dict[uid])


def view_all():
    if main_dict == {}:
        print("File is empty!! Nothing to view.")
    else:
        for i, v in main_dict.items():
            print("{}\n".format(v))



def edit(key):
    key = int(input("Choose the field number you want to edit from below option-:\n"
                    "1. Name\n"
                    "2. Age\n"
                    "3. Profession\n"
                    "4. About_me\n"
                    "5. Organisation\n"
                    "6. Skills\n"
                    "Enter here: "))
    if key < 1 or key > 6:
        print("Please choose correct field number from the options.")
        exit()
    list1 = ["Name", "Age", "Profession", "About_me", "Organisation", "Skills"]
    field = list1[key - 1]
    updated_value = input("Enter the new {}: ".format(field))
    for i, v in main_dict.items():
        if i == uid:
            main_dict[i][field] = updated_value
            print("Your {} is successfully updated-:\n"
                  "{}".format(field, main_dict[uid]))
    with open("test.json", "w") as updated_json:
        json.dump(main_dict, updated_json)


def delete_entry(key):
    for i, v in main_dict.copy().items():
        if i == str(uid):
            del main_dict[i]
            print("Your entry is successfully deleted.")
    with open("test.json", 'w') as deleted_json:
        json.dump(main_dict.copy(), deleted_json)


option = int(input("Choose the option number from the below menu-:\n"
                "1. Add an entry\n"
                "2. View an entry\n"
                "3. Edit an entry\n"
                "4. Delete an entry\n"
                "5. View all entries\n"
                "Enter here: "))
if option == 2 or option == 3 or option == 4:
    c = 0
    uid = input("Enter the unique ID here: ")
    for i, v in main_dict.items():
        if i == uid:
            c = 1
    if c != 1:
        print("NO such unique ID found.")
        exit()
if option == 1:
    create_entry()
elif option == 2:
    view(uid)
elif option == 3:
    edit(uid)
elif option == 4:
    delete_entry(uid)
elif option == 5:
    view_all()
else:
    print("Please choose correct option number from the menu.")
