
def create_file():
    file = open("resume1.txt", "w")
    name = input("Enter your name:")
    roll = input("Enter your roll:")
    experiance = input("Experiance details:")
    objective = input("enter the objective:")
    technical = input("Technical skills:")
    project = input("project details:")
    education = input("Education details:")
    print("----footer---")
    email = input("Email address:")

    mob = input("Phone no:")
    data = ['                                         RESUME\n', f'       NAME: {name}\n', '\n',
            f'       ROLL: {roll}\n', '\n', '                                        EXPERIENCE\n',
            f'       {experiance}\n', '                                         OBJECTIVE\n', f'       {objective}\n',
            '                                       TECHNICAL SKILLS\n', f'       {technical}\n',
            '                                        PROJECT DETAILS\n', f'       {project}\n',
            '                                       EDUCATION DETAILS\n', f'       {education}\n', '\n',
            '--------------------------------------------------------------------------------------------------------------------------------------------------\n',
            f'      EMAIL ADDRESS: {email}\n', f'      PHONE NO      : {mob}\n', '\n', '\n', '\n', '\n', '\n', '\n'
            ]
    # list_data = []
    # for i in data:
    #     list_data.append(i)
    # print(list_data)
    file.writelines(data)

    file.close()

exp_newline = 0
remove_line = 0
def change_value(select, value):
    fileData = open("resume1.txt", "r+")
    listData = fileData.readlines()
    count = 0;
    cap_count = 0
    capTech_count = 0
    capProject_count = 0
    capEdu_count = 0
    capob_count = 0

    cap = "\t   "
    if select == 1:
        for line in listData:
            if len(line.split(":")) == 2:
                if line.split(":")[0].strip() == "NAME":
                    listData[count] = line.split(":")[0] + ": " + value + "\n"
            count += 1
    if select == 2:
        for line in listData:
            if len(line.split(":")) == 2:
                if line.split(":")[0].strip() == "ROLL":
                    listData[count] = line.split(":")[0] + ": " + value + "\n"
            count += 1
    if select == 3:

        for line in listData:
            if not len(line.split(":")) == 2:
                if line.split("\n")[0].strip() == "EXPERIENCE":
                    cap_count = count
                elif count == cap_count + 1:
                    check_len = 0
                    for i in list(value.split()):

                        if check_len > 10:
                            cap += i + "\t\t"

                            check_len = 0

                        else:
                            cap += i + "\t"
                        check_len += 1
                    # print(cap)
                    global exp_newline
                    exp_newline = count
                    listData[count] = cap + "\n"

            count += 1
    if select == 4:
        for line in listData:
            if not len(line.split(":")) == 2:
                if line.split("\n")[0].strip() == "OBJECTIVE":

                    capob_count = count
                    global remove_line
                    remove_line = count
                elif count == capob_count + 1:
                    checkob_len = 0
                    capob = "\t   "
                    for i in list(value.split(",")):
                        if checkob_len > 10:
                            capob += i + "\t\t"
                            checkob_len = 0
                        else:
                            capob += i + "\t"
                        checkob_len += 1
                    # print(capTech)
                    listData[count] = capob + "\n"

            count += 1

    if select == 5:
        for line in listData:
            if not len(line.split(":")) == 2:
                if line.split("\n")[0].strip() == "TECHNICAL SKILLS":
                    capTech_count = count
                elif count == capTech_count + 1:
                    checkTech_len = 0
                    capTech = "\t   "
                    for i in list(value.split(" ")):
                        if checkTech_len > 10:
                            capTech += i + "\t\t"
                            checkTech_len = 0
                        else:
                            capTech += i + "\t"
                        checkTech_len += 1
                    # print(capTech)
                    listData[count] = capTech + "\n"

            count += 1

    if select == 6:
        for line in listData:
            if not len(line.split(":")) == 2:
                if line.split("\n")[0].strip() == "PROJECT DETAILS":
                    capProject_count = count
                elif count == capProject_count + 1:
                    checkProject_len = 0
                    capProject = "\t   "
                    for i in list(value.split(",")):
                        if checkProject_len > 10:
                            capProject += i + "\t\t"
                            checkProject_len = 0
                        else:
                            capProject += i + "\t"
                        checkProject_len += 1
                    # print(capProject)
                    listData[count] = capProject + "\n"

            count += 1

    if select == 7:
        for line in listData:
            if not len(line.split(":")) == 2:
                if line.split("\n")[0].strip() == "EDUCATION DETAILS":
                    capEdu_count = count
                elif count == capEdu_count + 1:
                    checkEdu_len = 0
                    capEdu = "\t   "
                    for i in list(value.split(",")):
                        if checkEdu_len > 10:
                            capEdu += i + "\t\t"
                            checkEdu_len = 0
                        else:
                            capEdu += i + "\t"
                        checkEdu_len += 1
                    # print(capEdu)
                    listData[count] = capEdu + "\n"

            count += 1
    if select == 8:
        for line in listData:
            if len(line.split(":")) == 2:
                if line.split(":")[0].strip() == "EMAIL ADDRESS":
                    listData[count] = line.split(":")[0] + ": " + value + "\n"
            count += 1
    if select == 9:
        for line in listData:
            if len(line.split(":")) == 2:
                if line.split(":")[0].strip() == "PHONE NO":
                    listData[count] = line.split(":")[0] + ": " + value + "\n"
            count += 1
    # print(remove_line, exp_newline)
    # lst_count = 0
    # for i in listData:
    #     if i.split("\n")[0].strip() == "EXPERIENCE":
    #         if not listData[lst_count+2] == "OBJECTIVE":
    #             del listData[lst_count+1]
    #     lst_count += 1
    # if not remove_line - exp_newline == 0:
    #     for i in range(exp_newline, remove_line):
    #         print(listData[i])
    fileData.seek(0)
    fileData.writelines(listData)
    fileData.close()


def change_all(select):
    if select == 10:
        fileData = open("resume1.txt", "r+")
        listData = fileData.readlines()
        count = 0;
        cap_count = 0
        capTech_count = 0
        capProject_count = 0
        capEdu_count = 0
        capob_count = 0
        name = input("enter the alternative name:")
        roll = input("enter the alternative roll:")
        experiance = input("enter the alternative experiance detail:")
        objective = input("enter the alternative objective:")
        Technical_skills = input("enter the alternative Technical skills:")
        project = input("enter the alternative project detail:")
        Education = input("enter the alternative education detail:")

        email = input("enter the alternative email address:")
        mob = input("enter the alternative mobile number:")
        cap = "\t\t\t"
        for line in listData:

            if len(line.split(":")) == 2:
                if line.split(":")[0].strip() == "NAME":
                    listData[count] = line.split(":")[0] + ": " + name + "\n"

                elif line.split(":")[0].strip() == "ROLL":
                    listData[count] = line.split(":")[0] + ": " + roll + "\n"

                elif line.split(":")[0].strip() == "EMAIL ADDRESS":
                    listData[count] = line.split(":")[0] + ": " + email + "\n"

                elif line.split(":")[0].strip() == "PHONE NO":
                    listData[count] = line.split(":")[0] + ": " + mob + "\n"

            else:

                if line.split("\n")[0].strip() == "EXPERIENCE":
                    cap_count = count
                elif count == cap_count + 1:
                    check_len = 0
                    for i in list(experiance.split()):

                        if check_len > 10:
                            cap += i + "\t\t"
                            check_len = 0
                        else:
                            cap += i + "\t"
                        check_len += 1
                    # print(cap)

                    listData[count] = cap + "\n"

                elif line.split("\n")[0].strip() == "OBJECTIVE":
                    capob_count = count
                elif count == capob_count + 1:
                    checkob_len = 0
                    capob = "\t\t\t"
                    for i in list(objective.split(",")):
                        if checkob_len > 10:
                            capob += i + "\t\t"
                            checkob_len = 0
                        else:
                            capob += i + "\t"
                        checkob_len += 1
                    # print(capTech)
                    listData[count] = capob + "\n"

                elif line.split("\n")[0].strip() == "TECHNICAL SKILLS":

                    # techData_count = count
                    capTech_count = count
                elif count == capTech_count + 1:
                    checkTech_len = 0
                    capTech = "\t\t\t"
                    for i in list(Technical_skills.split(",")):
                        if checkTech_len > 10:
                            capTech += i + "\t\t"
                            checkTech_len = 0
                        else:
                            capTech += i + "\t"
                        checkTech_len += 1
                    # print(capTech)
                    listData[count] = capTech + "\n"
                elif line.split("\n")[0].strip() == "PROJECT DETAILS":
                    capProject_count = count
                elif count == capProject_count + 1:
                    checkProject_len = 0
                    capProject = "\t\t\t"
                    for i in list(project.split(",")):
                        if checkProject_len > 10:
                            capProject += i + "\t\t"
                            checkProject_len = 0
                        else:
                            capProject += i + "\t"
                        checkProject_len += 1
                    # print(capProject)
                    listData[count] = capProject + "\n"
                elif line.split("\n")[0].strip() == "EDUCATION DETAILS":
                    capEdu_count = count
                elif count == capEdu_count + 1:
                    checkEdu_len = 0
                    capEdu = "\t\t\t"
                    for i in list(Education.split(",")):
                        if checkEdu_len > 10:
                            capEdu += i + "\t\t"
                            checkEdu_len = 0
                        else:
                            capEdu += i + "\t"
                        checkEdu_len += 1
                    # print(capEdu)
                    listData[count] = capEdu + "\n"

            count += 1

        fileData.seek(0)

        fileData.writelines(listData)

        fileData.close()


def show_resume():
    file = open("resume1.txt", "r")
    lst = file.readlines()
    for line in lst:
        print(line)
    file.close()


def edit_resume():
    print('''Select Which data you want to edit:
             1. name 
             2.ROLL 
             3. Experiance 
             4.Objective 
             5.Technical skills
             6.project details
             7.Education details
             8.Email
             9.phone number
             10. Want to alter entire data
             ''')
    select = int(input("Enter your choice:"))
    if select == 1:
        name = input("enter the alternative name:")
        change_value(select, name)
    if select == 2:
        roll = input("enter the alternative roll:")
        change_value(select, roll)
    if select == 3:
        experiance = input("ALternative experience details:")
        change_value(select, experiance)
    if select == 4:
        objective = input("Alternative Objective details:")
        change_value(select, objective)
    if select == 5:
        technical = input("Alternative Technical skills:")
        change_value(select, technical)
    if select == 6:
        project = input("Alternative Project details:")
        change_value(select, project)
    if select == 7:
        education = input("Alternative education details:")
        change_value(select, education)
    if select == 8:
        email = input("alternative email address:")
        change_value(select, email)
    if select == 9:
        mob = input("alternative mob number:")
        change_value(select, mob)
    if select == 10:
        change_all(select)


print('''WELCOME TO RESUME CREATION:
             Choose your option:
               1. create a resume
               2. Edit resume details
               3. show the resume''')
choice = int(input("enter your choice"))

if choice == 1:
    create_file()
elif choice == 2:
    edit_resume()
elif choice == 3:
    show_resume()
