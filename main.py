import sqlite3, time, sys

created = False


# import loginDatabase

class User():
    '''
            A student object holding the first name, last name, student number and grade of each student

            Attributes
            ----------
            firstName : str
                The first name of student
            lastName : str
                The last name of student
            username: str
              The username of user
            password: str
              The password of user

            Methods
            -------
            ChangePassword() -> None
                Allows user to change their password

          '''

    def __init__(self, firstName, lastName, username, password):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password

    def ChangePassword(self):
        """
        Let's user change their password

        This function is used when the user wants to change their password. The user has to re-enter their username and password to verify their identity.

        Parameters
        ----------
        none

        Return
        ------
        none
        """
        found = 0
        while found == 0:
            username = input("Please enter your username")
            with sqlite3.connect("login.db") as db:
                cursor = db.cursor()
            findUser = ("SELECT * FROM user WHERE username=?")
            cursor.execute(findUser, [(username)])
            if cursor.fetchall():
                found = 1
            else:
                print("Username does not exist")
        found1 = 0
        while found1 == 0:
            password = input("Please enter your current password: ")
            with sqlite3.connect("login.db") as db:
                cursor = db.cursor()
            findPass = ("SELECT * FROM user WHERE username=? and password=?")
            cursor.execute(findPass, [(username), (password)])
            if cursor.fetchall():
                found1 = 1
            else:
                print("Please enter the right password")
        password1 = input("Please enter your new password")
        while password == password1:
            print("Please enter in a different password, please try again")
            found2 = 0
            while found2 == 0:
                password = input("Please enter your current password: ")
                with sqlite3.connect("login.db") as db:
                    cursor = db.cursor()
                findPass = ("SELECT * FROM user WHERE username=? and password=?")
                cursor.execute(findPass, [(username), (password)])
                if cursor.fetchall():
                    found2 = 1
                    password1 = input("Please re-enter new password: ")
                else:
                    print("Please enter the correct password")

        self.password = password
        updateDate = '''Update user set password=? where username =?'''
        cursor.execute(updateDate, [(password1), (username)])
        db.commit()


class Teacher(User):
    '''
          A teacher object holding their first name and last name

          Attributes
          ----------
          firstName : str
              The first name of student
          lastName : str
              The last name of student
          studentNumber : int
            The number associated with the student
          grade : int
            The grade a teacher assigns to the student
          plagiarized : bool
            Showcases whether or not a student is reported for plagarism

          Methods
          -------
          printStudent() -> None
              Prints the full name of the student to console
          printStudentNumber() -> None
              Prints the student's student number to console
          changeStudentNumber(studentNumber : int) -> None
              Allows user to change a student's student number
          changeStudentFirstName(studentFirstName : str) -> None
              Allows user to change a student's first name
          changeStudentLastName(studentLastName : str) -> None
              Allows user to change a student's last name
          inputStudentGrade(studentGrade : int) -> None
              User inputs student's grade into the system
          printStudentGrade() -> None
            Prints the student's grade to console
          reportPlagarism() -> None
              User can report student for plagarism based upon the results of plagarism detector
          plagarismChecker() -> None:
               Checks two files and determines similiarity

        '''

    def __init__(self, firstName, lastName, username, password):
        '''
        Constructor to build a student object


        Parameters
        ----------
        firstName : str
        The first name of student

        lastName : str
        The last name of student

        username: str
        username of student

        password: str
        password of studnet's account

        studentNumber : int
         The number associated with the student

        grade : int
        grade assigned to student by teacher after their work is marked

        plagiarized : bool
        If the plagarism detector detects plagarism, teacher is able to report student by assigning this variable to true

        '''

        super().__init__(firstName, lastName, username, password)

    def plagarismChecker(self):
        plagiarized = False
        with open('firstFile.txt', "r") as file1:
            firstFile = file1.readlines()

        with open('secondFile.txt', "r") as file2:
            secondFile = file2.readlines()

        compFirstFile = ''.join(firstFile).split(' ')
        compSecondFile = ''.join(secondFile).split(' ')

        final_list = []
        for word in compFirstFile:
            for word2 in compSecondFile:
                if word == word2:
                    final_list.append(word)

        if len(final_list) > len(compFirstFile) // 2:
            print("This student plagiarized")
            if input(" Enter 'Yes' if you want to report plagarism?").lower() == "yes":
                studentFirstName = input("What is the student's first name?")
                studentLastName = input("What is the student's last name?")

        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
            updateData = '''UPDATE user SET plagarized = 'True' WHERE firstname = ? and surname = ?'''
            cursor.execute(updateData, [(studentFirstName), (studentLastName)])
            db.commit()

            # self.plagiarized = True
            # print("reported")
            # return
            # else:
            # print("Not reported")
            # return
        # return


class Student(User):
    '''
          A student object holding the first name, last name, student number and grade of each student

          Attributes
          ----------
          firstName : str
              The first name of student
          lastName : str
              The last name of student
          studentNumber : int
            The number associated with the student
          grade : int
            The grade a teacher assigns to the student
          plagiarized : bool
            Showcases whether or not a student is reported for plagarism

          Methods
          -------
          printStudent() -> None
              Prints the full name of the student to console
          printStudentNumber() -> None
              Prints the student's student number to console
          changeStudentNumber(studentNumber : int) -> None
              Allows user to change a student's student number
          changeStudentFirstName(studentFirstName : str) -> None
              Allows user to change a student's first name
          changeStudentLastName(studentLastName : str) -> None
              Allows user to change a student's last name
          inputStudentGrade(studentGrade : int) -> None
              User inputs student's grade into the system
          printStudentGrade() -> None
            Prints the student's grade to console
          reportPlagarism() -> None
              User can report student for plagarism based upon the results of plagarism detector
          plagarismChecker() -> None:
               Checks two files and determines similiarity

        '''

    def __init__(self, firstName, lastName, username, password, grade, plagiarized, studentNumber):
        '''
        Constructor to build a student object


        Parameters
        ----------
        firstName : str
        The first name of student

        lastName : str
        The last name of student

        username: str
        username of student

        password: str
        password of studnet's account

        studentNumber : int
         The number associated with the student

        grade : int
        grade assigned to student by teacher after their work is marked

        plagiarized : bool
        If the plagarism detector detects plagarism, teacher is able to report student by assigning this variable to true

        '''

        super().__init__(firstName, lastName, username, password)
        self.grade = 0
        self.plagiarized = False
        self.studentNumber = studentNumber

    def printStudent(self):
        '''
        Prints the full name of student to the console

        '''
        print(self.firstName + " " + self.lastName)
        return

    def printStudentNumber(self):
        '''
        Prints the student's student number to the console

        '''
        print(self.studentNumber)
        return

    def changeStudentNumber(self, newStudentNumber):
        '''
        Allows user to change student's student number

        Parameters
            ----------
            newStudentNumber : int
          The new studentNumber assigned to student

        '''
        self.studentNumber = newStudentNumber
        return

    def inputStudentGrade(self, studentGrade):
        '''
        Allows user to input student's grade into system

            Parameters
            ----------
            grade : int
          The grade assigned to student inputted by the teacher into the system

        '''
        self.grade = studentGrade
        return

    def printStudentGrade(self):
        '''
        Prints student's grade to console

        '''
        print(self.grade)
        return

    def reportPlagarism(self):
        '''
        Reports student for plagarism

        '''
        self.plagiarized = True
        return

    def plagarismChecker(self):
        plagiarized = False
        with open('firstFile.txt', "r") as file1:
            firstFile = file1.readlines()

        with open('secondFile.txt', "r") as file2:
            secondFile = file2.readlines()

        compFirstFile = ''.join(firstFile).split(' ')
        compSecondFile = ''.join(secondFile).split(' ')

        final_list = []
        for word in compFirstFile:
            for word2 in compSecondFile:
                if word == word2:
                    final_list.append(word)

        if len(final_list) > len(compFirstFile) // 2:
            print("This student plagiarized")
            if input(" Enter 'Yes' if you want to report plagarism?").lower() == "yes":
                studentFirstName = input("Enter student's first name")
            studentLastName = input("Enter student's last name")
            selectData = '''SELECT count (*) FROM user WHERE firstname = studentFirstName and surname = studentLastName'''
            if selectData == 1:
                updateData = '''UPDATE user SET plagarized = true WHERE firstname = studentFirstName and surname = studentLastName'''

                self.plagiarized = True
                print("reported")
                return
            else:
                print("Not reported")
                return
        return


def login():
    """
    User log in

    User enters their username and password in order to log in to their account

    Parameters
    ----------
    None

    Return
    ------
    None
    """
    while True:
        firstname = input("Please enter your first name: ")
        surname = input("Please enter your last name:")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE firstname = ? AND surname = ? AND username = ? AND password = ?")
        cursor.execute(find_user, [(firstname), (surname), (username), (password)])
        results = cursor.fetchall()
        if results:
            for i in results:
                print("Welcome " + i[2])
                # Systembypassblocker()
            break

        else:
            print("Incorrect login information!")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == 'n':
                print("Good bye")
                time.sleep(1)
                break
    if created == False:
        global firstName
        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
        find_user_2 = ("SELECT position FROM user WHERE firstname = ? AND surname = ?")
        cursor.execute(find_user_2, [(firstname), (surname)])
        results2 = cursor.fetchall()
        if results2 == [('student',)]:
            find_user_1 = ("SELECT grade FROM user WHERE firstname = ? AND surname = ?")
            cursor.execute(find_user_1, [(firstname), (surname)])
            results = cursor.fetchall()
            # print(results)
            firstName = Student(firstname, surname, username, password, results, 'False',
                                input("What is your student number?"))
        else:
            firstName = Teacher(firstname, surname, username, password)

    return


def newUser():
    """
    User creates account

    The user creates their account by entering in their username and password as well as their name

    Parameters
    ----------
    None

    Return
    ------
    None
    """
    found = 0
    while found == 0:
        username = input("Please enter a username: ")
        with sqlite3.connect("login.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username=?")
        cursor.execute(findUser, [(username)])

        if cursor.fetchall():
            print("Username Taken, Please try again")
        else:
            found = 1

    firstname = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    password = input("Please enter your password: ")
    password1 = input("Please reenter your password: ")
    while password != password1:
        print("Your password didn't match, please try again")
        password = input("Please enter your password: ")
        password1 = input("Please reenter your password: ")
    position = input("Are you a student or teacher?")
    plagarized = "False"

    insertData = '''INSERT INTO user (username, firstname, surname, password, position, grade, plagarized) VALUES (?,?,?,?,?,'',? )'''
    cursor.execute(insertData, [(username), (firstname), (surname), (password), (position), (plagarized)])
    db.commit()
    global firstName
    if position == "student":
        firstName = Student(firstname, surname, username, password, None, False, input("What is your student number?"))
        with open("studentInfo.txt", 'w') as studentFile:
            studentFile.write(
                "Firstname: {}, Lastname: {}, Username: {}, Password: {}, Grade: {}, Plagiarized: {}, Student number: {}".format(
                    firstName.firstName, firstName.lastName,
                    firstName.username, firstName.password,
                    firstName.grade, firstName.plagiarized,
                    firstName.studentNumber))

    else:
        firstName = Teacher(firstname, surname, username, password)

    return None


def binarySearch(arr, leftNum, rightNum, target):
    """
    A biinary search function

    Searches a list using a binary search

    Parameters
    ----------
    arr: Name of list to be searched
    leftNum:
    rightNum:
    target:

    Returns
    -------
    None
    """

    while leftNum <= rightNum:
        midSearchPos = leftNum + (rightNum - leftNum) // 2;

        if arr[midSearchPos] == target:
            return midSearchPos

        elif arr[midSearchPos] < target:
            leftNum = midSearchPos + 1

        else:
            rightNum = midSearchPos - 1

    return None


def linearSearch(arr, numWanted):
    """
    A linear search functiion

    A function that searches a list using linear search.

    Parameters
    ----------
    arr:
      Name of array

    numWanted:
      number that is required to be found

    Returns
    -------
    None
    """
    for i in range(len(arr)):
        if arr[i] == numWanted:
            return i

    return None


def bubbleSort(array):
    """
      A bubble sort functiion.

      A function that sorts a list using bubble sort.

      Parameters
      ----------
      arr:
        Name of list

      Returns
      -------
      None
      """
    for num in range(len(array) - 1, 0, -1):
        for i in range(num):
            if array[i] > array[i + 1]:
                j = array[i]
                array[i] = array[i + 1]
                array[i + 1] = j


def selectionSort(array):
    """
    A selectioni sort function.

    A function that uses selection sort to sort a list.

    Parameters
    ----------
    arr:
      Name of list

    Returns
    -------
    None
    """
    for num in range(len(array) - 1, 0, -1):
        Max = 0
        for index in range(1, num + 1):
            if array[index] > array[Max]:
                Max = index

        j = array[num]
        array[num] = array[Max]
        array[Max] = j


def menu():
    """
    A menu of options

    The menu for the log in system where users decide to either create an account, log-in or exit the application.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    while True:
        print("Welcome to my system")
        menu = ('''
    1 - Create New User
    2 - Login to system
    3 - Exit system\n ''')

        userChoice = input(menu)

        if userChoice == "1":
            newUser()

        elif userChoice == "2":
            login()
            break

        elif userChoice == "3":
            print("Thanks for visiting")
            sys.exit()
        else:
            print("Command not recognized: ")
    return


def Mainprogram():
    """
    A menu of options

    This function will print out a list of options the user can choose from

    Parameters
    ----------
    None

    Return
    ------
    None
    """
    if isinstance(firstName, Teacher):
        while True:
            print("Choose an option below?")

            print(
                "1: CheckForPlagarism (Copy and paste file contents into firstFile.txt and secondFile.txt to compare for plagarism.(Only a teacher has access)")

            print("2: Quit")
            print("3: Change Password")
            print("4: Enter student mark(Only teachers have access)")
            print("5: Calculate class median")
            print("6: Calculate student mark percentile(Enter Student mark first)")

            print("7: Change a student's grade")
            print("8: View student grades")

            option = int(input())
            if option == 1:
                firstName.plagarismChecker()

            if option == 2:
                break

            if option == 3:
                Student.ChangePassword(firstName)

            if option == 4:
                Student.grade = int(input("enter student grade here"))
                with open("studentGrade.txt", 'a') as studentGrade:
                    studentGrade.write(" " + str(Student.grade))

            if option == 5:
                with open('studentGrade.txt', "r") as gradeFile:
                    studentGradeFile = gradeFile.read().split()

                grades = [int(x) for x in studentGradeFile]
                # selectionSort(grades)
                grades.sort()

                # print(grades)

                if len(grades) % 2 == 0:
                    print((grades[len(grades) // 2] + grades[(len(grades) // 2) - 1]) / 2)

                else:
                    print(grades[len(grades) // 2])

            if option == 6:
                with open('studentGrade.txt', "r") as gradeFile:
                    studentGradeFile = gradeFile.read().split()

                grades = [int(x) for x in studentGradeFile]
                # bubbleSort(grades)
                grades.sort()

                gradePercentile = (binarySearch(grades, 0, len(grades) - 1, Student.grade) + 1) / len(grades) * 100

                markRanking = linearSearch(grades, Student.grade)
                print(markRanking)

                print(grades)
                print(str(gradePercentile) + "th percentile")
                print(str(markRanking + 1) + "th highest in the class!")

            if option == 7:
                studentFirstName = input("Enter student's first name")
                studentLastName = input("Enter student's last name")
                with sqlite3.connect("login.db") as db:
                    cursor = db.cursor()
                selectData = '''SELECT count (*) FROM user WHERE firstname = ? and surname = ?'''
                cursor.execute(selectData, [(studentFirstName), (studentLastName)])
                results1 = cursor.fetchall()

                if results1 == 1:
                    updateStudentGrade = input("Enter new student grade")
                    with sqlite3.connect("login.db") as db:
                        cursor = db.cursor()
                    updateData = '''UPDATE user SET grade = updateStudentGrade WHERE firstname = ? and surname = ?'''
                    cursor.execute(updateData, [(studentFirstName), (studentLastName)])
                    db.commit()

                    with sqlite3.connect("login.db") as db:
                        cursor = db.cursor()
                    selectData1 = '''SELECT * FROM user'''
                    cursor.execute(selectData1)
                    results2 = cursor.fetchall()

                    for i in results2:
                        with open("studentInfo1.txt", 'w') as studentFile1:
                            studentFile1.write(
                                "Firstname: {}, Lastname: {}, Username: {}, Password: {}, Grade: {}, Plagiarized: {}, Student number: {}".format(
                                    results2.firstName, results2.lastName,
                                    results2.username, results2.password,
                                    results2.grade, results2.plagiarized,
                                    results2.studentNumber))
            if option == 8:
                with open('studentGrade.txt', "r") as gradeFile:
                    studentGradeFile = gradeFile.read().split()
                grades = [int(x) for x in studentGradeFile]
                # bubbleSort(grades)
                grades.sort()
                print(grades)



    else:
        while True:
            print("Choose an option below?")

            print("1: Quit")
            print("2: Change Password")
            print("3: Calculate class median")
            print("4: Calculate student mark percentile(Teacher must enter Student mark first)")
            print("5: Check if you have been reported for plagarism")

            option = int(input())
            if option == 1:
                break

            if option == 2:
                Student.ChangePassword(firstName)

            if option == 3:
                try:
                    with open('studentGrade.txt', "r") as gradeFile:
                        studentGradeFile = gradeFile.read().split()

                    grades = [int(x) for x in studentGradeFile]
                    # selectionSort(grades)
                    grades.sort()

                    print(grades)

                    if len(grades) % 2 == 0:
                        print((grades[len(grades) // 2] + grades[(len(grades) // 2) - 1]) / 2)

                    else:
                        print(grades[len(grades) // 2])

                except:
                    print("No grades have been entered by the teacher yet.")

            if option == 4:
                try:
                    with open('studentGrade.txt', "r") as gradeFile:
                        studentGradeFile = gradeFile.read().split()

                    grades = [int(x) for x in studentGradeFile]
                    # bubbleSort(grades)
                    grades.sort()

                    gradePercentile = (binarySearch(grades, 0, len(grades) - 1, Student.grade) + 1) / len(grades) * 100

                    markRanking = linearSearch(grades, Student.grade)
                    print(markRanking)

                    print(grades)
                    print(str(gradePercentile) + "th percentile")
                    print(str(markRanking + 1) + "th highest in the class!")
                except:
                    print("Teacher did not enter a grade yet.")

            if option == 5:
                with sqlite3.connect("login.db") as db:
                    cursor = db.cursor()
                selectData1 = '''SELECT plagarized FROM user WHERE firstname = ? and surname = ?'''
                cursor.execute(selectData1, [(firstName.firstName), (firstName.lastName)])
                results2 = cursor.fetchall()
                if results2 == [('True',)]:
                    print("You have been reported for plagarism!")
                else:
                    print("You have not been reported for plagarism yet.")

    return option


#import loginDatabase
menu()
Mainprogram()
