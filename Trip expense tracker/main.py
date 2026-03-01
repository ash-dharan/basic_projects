def main():
    import template as tem
    import json
    import os
    from pathlib import Path as path

    def save_expense(tripname,expense_name ,amount ,paid_by ,split):
        file_path = path(f"./Trip/{tripname}/expenses.json")

        if file_path.exists() and file_path.stat().st_size != 0 :
            with open(file_path,"r") as f: 
                expenses = json.load(f)
        else:
            expenses = []
        
        expenses.append({
            "name": expense_name,
            "amount": amount,
            "paid_by": paid_by,
            "split": split
        })
        with open(file_path,"w") as f:
            json.dump(expenses, f, indent=4)
        

    def add_member(member,tripname):
        file_path = path(f"./Trip/{tripname}/members.json")

        if file_path.exists() and file_path.stat().st_size != 0:
            with open(file_path,"r") as f:
                members = json.load(f)
        else:
            members = []
        
        members.append({
            "name" : member.name,
            "id" : member.id
        })

        with open(file_path,"w") as f:
            json.dump(members,f,indent=4)
    
    def remove_member(member,tripname):
        file_path = path(f"./Trip/{tripname}/members.json")

        if file_path.exists() and file_path.stat().st_size != 0:
            with open(file_path,"r") as f:
                members = json.load(f)
        else:
            print("The list is empty or no member exist")
            return None

        if member in members:
            members.remove(member)
        else:
            print(f'there is no member by the name {member["name"]} with the id of {member["id"]}.')
            print(f"this is the list\n {members}")
            print(f"this is what you gave {member}")
            return None

        print(f'member {member["name"]} has ben removed from the list')

        with open(file_path,"w") as f:
            json.dump(members,f,indent=4)

    def load_json(file_path):
        if file_path.exists() and file_path.stat().st_size > 0:
            with open(file_path) as f:
                return json.load(f)
        return []
    
    def calculate_balance(tripname):
        file_path = path(f"./Trip/{tripname}/expenses.json")
        expenses = load_json(file_path)
        balance = {}

        for e in expenses:
            if e["paid_by"] in balance:
                balance[e["paid_by"]] += e["amount"]
            else:
                balance[e["paid_by"]] = e["amount"]
            for s in e["split"].keys():
                if s in balance:
                    balance[s] -= e["split"][s]
                else:
                    balance[s] = -e["split"][s]
        return balance
    def equal_split():
        amount = float(input("Enter the expense amount: "))
        ex_name = input("Enter the name of the expense: ")
        paid_by = input("Who paid the expense?: ")

        if paid_by not in [m["name"] for m in members]:
            print("Invalid member")
            return None

        count = len(members)
        share = amount / count

        split = {}
        for m in members:
            split[m["name"]] = share

        save_expense(tripname, ex_name, amount, paid_by, split)

        print("Expense added successfully.")
    
    def unequal_split():
        amount = float(input("Enter the expense amount: "))
        ex_name = input("Enter the name of the expense: ")
        paid_by = input("Who paid the expense?: ")

        if paid_by not in [m["name"] for m in members]:
            print("Invalid member")
            return None

        count = len(members)
        # share = amount / count

        split = {}
        check = 0
        for m in members:
            share = ((float(input(f"enter the percentage split for {m['name']} :")))/100)
            split[m["name"]] = share
            check += share 
        
        if check == 1:
            for m in members:
                split[m["name"]] = split[m["name"]] * amount
        else:
            print("The percentages does not add to 100, Try again.")
            return None

        save_expense(tripname, ex_name, amount, paid_by, split)

        print("Expense added successfully.")

    def split_option():
        split_type = int(input("""Enter 1 if want equal split , 
                                        2 For unequal split on percent\n"""))
        if split_type == 1:
            equal_split()

        elif split_type == 2:
            unequal_split()



    while True:
        state = input("Create a new tracker or use an existing one? (new/saved/exit): ").strip().lower()
        if state == "new":
            try:    
                tripname = input("Enter your trip name: ").lower()
                ## creates a directory with tripname and creates files expenses and members within it. 
                os.makedirs(f"./Trip/{tripname}")
                exp_path = path(f"./Trip/{tripname}/expenses.json")
                mem_path = path(f"./Trip/{tripname}/members.json")

                exp_path.touch()
                mem_path.touch()
                ## opens the files for writing.
                with open(f"./Trip/{tripname}/expenses.json","a+") as f:
                    expenses = []
                with open(f"./Trip/{tripname}/members.json","a+") as f:
                    members = []
                print(f"Created a Trip Folder {tripname} and files - expenses and members")
                break
            except FileExistsError:
                print(f"A folder with the name already exists.")

        elif state == "saved" :
            dirlist = os.listdir("./Trip")
            ## prints the list of directories to choose from.
            print(dirlist)
            while True:
                tripname = input("Enter the trip name: ").lower()
                if tripname in dirlist:
                    break
                else:
                    print("There is no trip with that name in the list. Please try again ")
            ex = path(f"./Trip/{tripname}/expenses.json")
            mem = path(f"./Trip/{tripname}/members.json")
                    
            expenses = load_json(ex)
            members = load_json(mem)
            print(f"Loaded '{tripname}' trip data.")

            break

        elif state == "exit":
            print("Goodbye")
            break

        else:
            print(f"Enter a valid option")

    while True:

        choice = input("""enter the option
                        1 for adding expenses
                        2 for adding members
                        3 for exit
                        4 for expenses list
                        5 for remove members
                        6 for show balance\n""")

        if choice == "3":
            print("Thank you for using the Program.")
            break

        elif choice == "2":
            person = tem.Member(input("Enter the name: "))
            members.append({"name": person.name,"id":person.id})
            add_member(person,tripname)

            print(f"Added member {person.name} to list\n")

        elif choice == "1":
            try:
                if not members:
                    print("No members found.")
                    continue

                split_option()
                
                # amount = float(input("Enter the expense amount: "))
                # ex_name = input("Enter the name of the expense: ")
                # paid_by = input("Who paid the expense?: ")

                # if paid_by not in [m["name"] for m in members]:
                #     print("Invalid member")
                #     continue

                # count = len(members)
                # share = amount / count

                # split = {}
                # for m in members:
                #     split[m["name"]] = share

                # save_expense(tripname, ex_name, amount, paid_by, split)

                # print("Expense added successfully.")

            except ValueError:
                print("EXPENSE VALUE MUST BE A NUMBER.")

        elif choice == "4":
            file_path = path(f"./Trip/{tripname}/expenses.json")
            print(load_json(file_path))

        elif choice == "5":
            print(members)
            person1 = {"name":input("Enter the name you want to remove: "),"id":input("enter their id: ")}
            remove_member(person1,tripname)

        elif choice == "6":
            print(calculate_balance(tripname)) 
            
        else:
            print("Enter a valid option.")


if __name__ == "__main__" :
    main()
