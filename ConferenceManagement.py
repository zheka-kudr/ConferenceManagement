import sys


class Conference:
    def __init__(self, name_conf, theme_conf, place_conf, leader_conf, date_conf):
        self.name_conf = name_conf
        self.theme_conf = theme_conf
        self.place_conf = place_conf
        self.leader_conf = leader_conf
        self.date_conf = date_conf

    def __str__(self):
        return str(
            self.name_conf + " " + self.theme_conf + " " + " " + self.place_conf + " " + self.leader_conf + " " + self.date_conf)


class Member:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return str(self.name + " " + self.surname + " " + str(self.age))


def main():
    conference = Conference("a", "a", "a", "a", "a")
    conference2 = Conference("b", "b", "b", "b", "b")
    conference3 = Conference("c", "c", "c", "c", "c")
    member = Member("iwan", "quahog", 22)
    list_of_members = [member]
    list_of_conferences = [conference, conference2, conference3]
    done = False
    while not done:
        print(
            """\nMenu\n1. Display all conferences\n2. Add conference\n3. Search conference\n4. Delete conference\n5. Show all members\n6. Add member\n7. Search members\n8. Delete member\n0. Exit""")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            exit("\nHy! That's Not A Number")  # Error Message
        else:
            if choice == 1:
                if len(list_of_conferences) != 0:
                    for idx, val in enumerate(list_of_conferences):
                        print(idx, val)
                else:
                    print("List of conferences is empty")
            elif choice == 2:
                print()
                name_conf = input("Enter name of conference: ")
                theme_conf = input("Enter theme of conference: ")
                place_conf = input("Enter place of conference: ")
                leader_conf = input("Enter leader of conference: ")
                date_conf = input("Enter date of conference: ")
                new_conference = Conference(name_conf, theme_conf, place_conf, leader_conf, date_conf)
                list_of_conferences.append(new_conference)
            elif choice == 3:
                index_search = input("\nEnter index: ")
                if int(index_search) < len(list_of_conferences):
                    print(str(list_of_conferences[int(index_search)]))
                else:
                    print("Index error")
            elif choice == 4:
                delete_search = input("\nEnter index: ")
                if int(delete_search) < len(list_of_conferences):
                    del list_of_conferences[(int(delete_search))]
                    print("Conference with index " + delete_search + " was deleted")
                else:
                    print("Index error")
            elif choice == 5:
                if len(list_of_members) != 0:
                    for idx, val in enumerate(list_of_members):
                        print(idx, val)
                else:
                    print("List of members is empty")
            elif choice == 6:
                name = input("\nEnter name: ")
                surname = input("Enter surname ")
                age = input("Enter age: ")
                new_member = Member(name, surname, age)
                list_of_members.append(new_member)
            elif choice == 7:
                index_search = input("\nEnter index: ")
                if int(index_search) < len(list_of_members):
                    print(str(list_of_members[int(index_search)]))
                else:
                    print("Index error")
            elif choice == 8:
                delete_search = input("\nEnter index: ")
                if int(delete_search) < len(list_of_members):
                    del list_of_members[(int(delete_search))]
                    print("Member with index " + delete_search + " was deleted")
                else:
                    print("Index error")
            elif choice == 9:
                index_search_member = input("\nEnter index of member: ")
                if int(index_search_member) < len(list_of_members):
                    index_search_conf = input("\nEnter index of conferences: ")
                    if int(index_search_conf) < len(list_of_conferences):
                        print("Add member: \n" + str(
                            list_of_members[int(index_search_member)]) + "\nTo conference: \n" + str(
                            list_of_conferences[int(index_search_conf)]))
                    else:
                        print("Index error")
                else:
                    print("Index error")
            elif choice == 0:
                sys.exit()


main()
