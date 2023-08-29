import os
import re
from pathlib import Path
import copy
def menu():
    #print("\n")
    print('''  
    --------------------Welcome to students management system-----------------------
    |                                                                              |
    |       ==============          Function List          =================       |
    |                                                                              |
    |   1. Record a student info                                                   |
    |   2. Search a student info                                                   |
    |   3. Delete a student info                                                   |
    |   4. Modify a student info                                                   |
    |   5. Sort out a result                                                       |
    |   6. Count the total number of students                                      |
    |   7. Show all the students info                                              |
    |   0. Exit the system                                                         |
    |   ========================================================================   |
    |   NOTE: Use number or ‘↓’ ‘↑’ to select the directions                       |
    --------------------------------------------------------------------------------
       '''
          )

def save(student):
    #filePath = Path("C:\\Users\\caifulai\\PycharmProjects\\pythonProject1_student_management_system")
    #fileName = "studentsInfo.txt"
    #file = filePath.joinpath(fileName)
    try:
        filePoint = open(file, 'a')
    except Exception as e:
        filePoint = open(file, 'w')
    for item in student:
        filePoint.write(str(item) + '\n')
    filePoint.close()

def insert():
    studentList = []
    mark = True
    while mark:
        id = input("Please input the ID (such as 11860914): ")
        while not id or len(id) != 8:
            print("Input error! Pls input again")
            id = input("Please input the ID (such as 11860914): ")
        name = input("Please input the NAME (such as CaifuLai): ")
        if not name:
            break
        try:
            english = int(input("Please input English Score: "))
            while not english or english < 0 or english > 100:
                print("Input error! Pls input again")
                english = int(input("Please input English Score: "))

            python = int(input("Please input Python Score: "))
            while not python or python < 0 or python > 100:
                print("Input error! Pls input again")
                python = int(input("Please input Python Score: "))

            c = int(input("Please input C Score: "))
            while not c or c < 0 or c > 100:
                print("Input error! Pls input again")
                c = int(input("Please input C Score: "))
        except:
            print("input invalid, not integrated numbers......failed to insert info, pls retry! ")
            continue
        #Save the info into dict
        student = {'ID': id, 'NAME': name, 'ENGLISH': english, 'PYTHON': python, 'C': c}
        studentList.append(student)
        inputMark = input("Do you want to continue insert? (y/n) ")
        if inputMark == 'y':
            mark = True
        else:
            mark = False
    save(studentList)
    print("Finish to insert studdent info! Thanks.")

def show_caifu():
    print("Show all the students info:")
    filePoint = open(file, 'r')
    fileContent = filePoint.readlines()
    studentList = []
    for line in fileContent:
        studentList.append(dict(eval(line)))
    show_student(studentList)
    #for line in fileContent:
    #    print(dict(eval(line)))

def show():
    AllStudents = []
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            students = file.readlines()
        for list in students:
            AllStudents.append(eval(list))
        if AllStudents:
            show_student(AllStudents)
    else:
        print("DataBase not initialized!")

def delete_caifu():
    deleteID = input("Please input the student ID to be delete: ")
    lineList = []
    filePoint = open(file, 'r')
    fileContent = filePoint.readlines()
    deleteMark = False
    for line in fileContent:
        dict(eval(line))
    for line in fileContent:
        if deleteID in line:
            print("Find the student info: ")
            deleteStudent = dict(eval(line))
            deleteMark = True
        else:
            lineList.append(line)
    if deleteMark:
        print("Student: " + deleteStudent["NAME"]+ " has been deleted!")
    else:
        print("Student: "+ deleteID + " Not found in the datastore")
#    print(lineList)
    filePoint.close()
    filePoint = open(file, 'w')
    for line in lineList:
        filePoint.write(line)

def delete():
    mark = True # mark if need to loop
    while mark:
        studentID = input("Please input the studentID: ")
        if studentID != "":   # to decide if there is a student to be deleted
            if os.path.exists(fileName):  # to find if the file is existed
                with open(fileName, 'r') as rfile:  # open the file
                    student_old = rfile.readlines()  # read all the sutdnets` info into a list
            else:
                student_old = [] # file not exist, create an empty list
            ifdel = False # Mark if to delete
            if student_old:  # if the student info file exists
                with open(fileName, 'w') as wfile:
                    d = {}
                    for list in student_old:  # loop every student of the whole list
                        d = dict(eval(list))   # transfer string to dictionary, one string item is a student
                        if d['ID'] != studentID: # if current student is not the target
                            wfile.write(str(d)+"\n")   # write the non-delete student to file equals not save target equals deletion
                        else: # current student is the target
                            ifdel = True    # target has been cleared
                    if ifdel: # really find the target to be deleted in the datastore
                        print("student(ID): %s has been cleared!" %studentID)
                    else: # no such studentID find in the datastore
                        print("student(ID): %s not found in the datastore! pls check the ID" %studentID)
            else: # student_old is an empty list means no original student info file found
                print("No student datastore found!")
                break
            show()
            inputMark = input("Continue to delete next one ? (y/n): ")
            if inputMark == 'y':
                continue
            else:
                mark = False

def modify():
    mark = True  # decide to modify next
    student_new=[] # create a new list to store new student info table
    while mark:
        studentID = int(input("please input the studentID or Q to quit modify: "))   # transfer the studentID to int
        if 10000000 <= studentID <= 99999999:  # to detect if the studentID is valid
            print(studentID,"????")
            if os.path.exists(fileName): # to check if the datastore file is existing
                with open(fileName, 'r') as rfile:  # open the datastore file
                    student_old = rfile.readlines()  #get all the original files
#               modifyContent = {} # define a dictionary to store the data of student which is going to be modified
                for item in student_old: # each item is a list, and represents a student(come from readlines function)
                    item = dict(eval(item))
                    modifyContent = copy.deepcopy(item)
                    originalContent = item
                    print(item["ID"])
                    markModifyLoop = True
                    if str(studentID) == item["ID"]: # to check if the current student is the target
                        print("find the student to be modified:   student Name: %s" %item["NAME"])
                        while markModifyLoop:
                            modifyItem = int(input("Please choose a object to modify or next studentID:\n  studentID --->0, \n  English ---> 1,  \n  Python ---> 2,  \n  C ---> 3,   \n  Quit ---> 4,  \nYour input:" )) #setup options for modifying different scores
                            if 0 <= modifyItem <= 4:
                                if modifyItem == 0:
                                    markModifyLoop = False
                                if modifyItem == 1:
                                    content = input("Please input the new Englisn score:")
                                    modifyContent["ENGLISH"] = content
                                if modifyItem == 2:
                                    content = input("Please input the new Python score:")
                                    modifyContent["PYTHON"] = content
                                if modifyItem == 3:
                                    content = input("Please input the new C score:")
                                    modifyContent["C"] = content
                                if modifyItem == 4:
                                    markModifyLoop = False
                                    mark = False
                        print("old-------------")
                        print(item)
                        print("new-----------")
                        print(modifyContent)
                        #originalContent = modifyContent
                        student_new.append(modifyContent)
                    else: # if the current student is not the target, save it
                        pass
                        #student_new.append(item)
                    student_new.append(originalContent)
                    with open(fileName, 'w') as wfile:  # write modified info into data files
                        for item in student_new:
                            wfile.write(str(item) + "\n")
                    rfile.close()
                    wfile.close()

                print("=============")
                print(student_new)

        else:  # if the studentID is not valid
            print("please input the right studentID! \n")
            continue

                #mark = False

#def modify():
#    show()

def sort():
    show()
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            student_old = file.readlines()
            student_new = []
        for list in student_old:
            student_new.append(dict(eval(list)))
    else:
        return

    OrderSelect = input("plsase select 0-up order or 1-down order:")
    if OrderSelect == '0':
        OrderSelectBool = False
    elif OrderSelect == '1':
        OrderSelectBool = True
    else:
        print("input error!")
        sort()

    mode = input("PLease select the order path: (1-ENGLISH, 2-PYTHON, 3-C, 4-TOTAL):")
    if mode == '1':
        student_new.sort(key=lambda x: int(x['ENGLISH']), reverse=OrderSelectBool)
    elif mode == '2':
        student_new.sort(key=lambda x: int(x['PYTHON']), reverse= OrderSelectBool)
    elif mode == '3':
        student_new.sort(key=lambda x: int(x['C']), reverse= OrderSelectBool)
    elif mode == '4':
        student_new.sort(key=lambda x: x['ENGLISH']+x['PYTHON']+int(x['C']), reverse= OrderSelectBool)
    else:
        print("input error! pls check")
        sort()

    show_student(student_new)



def total():
    if os.path.exists(fileName):
        with open(fileName, 'r') as file:
            student_count = file.readlines()
            if student_count:
                print("Total has %s students!" %len(student_count))
            else:
                print("No student in database!")
    else:
        print("DataBase not initialized!")

def main():
    ctrl = True
    while(ctrl):
        menu()
        option = input("Please select a function: ")
        option_str = re.sub("\D","",option)
        #option_str = re.sub(r"[^0-9]", "", option)
        if option_str in ['0','1','2','3','4','5','6','7','q']:
            option_str = int(option_str)
            if option_str == 0:
                print("Exit the system now!  ")
                ctrl = False
            elif option_str == 1:
                insert()
            elif option_str == 2:
                search()
            elif option_str == 3:
                delete()
            elif option_str == 4:
                modify()
            elif option_str == 5:
                sort()
            elif option_str == 6:
                total()
            elif option_str == 7:
                show()
                #show_student(studentList)
            elif option_str == 'q':
                print("Abort the process")
                break
        else:
                print("Your input is not correct ! please try again")

def show_student(studentList):
    if not studentList:
        print("No data!")
        return
    format_title = "{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID","NAME","ENGLISH","PYTHON","C","TOTAL"))
    format_data = "{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}"
    for info in studentList:
        #print("----->3",info)
        #print(info.get('ID'),info.get('NAME'),info.get('ENGLISH'),info.get('PYTHON'),info.get("C"))
        print(format_data.format(info.get('ID'), info.get('NAME'), str(info.get('ENGLISH')),str(info.get('PYTHON')),str(info.get('C')),str(int(info.get('ENGLISH'))+int(info.get('PYTHON'))+int(info.get('C')))))

def search():
    mark = True
    student_query = []
    while mark:
        id = ''
        name = ''
        if os.path.exists(fileName):
            mode = input("Please select search by id (1) or name (2), q for quit: ")
            if mode == '1':
                id = input("Please input the ID:")
            elif mode == '2':
                name = input("Please input the name:")
            elif mode == 'q':
                return
            else:
                print("Input error, pls check!")
                search() # call self to input again
            with open(fileName, 'r') as file:
                student = file.readlines()
                print("----->",student)
                for list in student:
                    d=dict(eval(list)) # translate the string to dictionary
                    print("----->2",d)
                    if id is not "":
                        if d['ID'] == id:
                            student_query.append(d)
                    elif name is not "":
                        if d['NAME'] == name:
                            student_query.append(d)
                print(student_query)
                show_student(student_query)
                student_query.clear()
                inputMark = input("Continue to search? (y/n  q for quit):")
                if inputMark == 'y':
                    mark = True
                elif inputMark == 'n':
                    mark = False
                elif inputMark == 'q':
                    return
                else:
                    print("error input")
        else:
            print("cannot find the initial data file!")
            return


if __name__ == "__main__":
    filePath = Path("./")
    fileName = "studentsInfo.txt"
    file = filePath.joinpath(fileName)
    main()
    #save("A")
    #insert()