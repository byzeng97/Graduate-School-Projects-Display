# Group Project: Yating Wang, Xuejun Shen, Bingyue Zeng, Xin Sui
import pandas as pd
import csv

Display_all = 1
Search_last_name = 2
Search_graduating_year = 3
Program_summary = 4
Add_new_student = 5
Quit = 6


def main():
    print('Welcome to Student Query Tool')
    content = pd.read_csv("Students.txt", sep="\t")  # get student data
    choice = 0
    while choice != Quit:
        choice = get_user_choice()
        if choice == Display_all:
            display_all(content)
        elif choice == Search_last_name:
            search_last_name(content)
        elif choice == Search_graduating_year:
            search_graduating_year(content)
        elif choice == Program_summary:
            program_summary(content)
        elif choice == Add_new_student:
            add_new_student(content)
        elif choice == Quit:
            print('Thank you for using our system! Bye.')


def get_user_choice():
    print('1. Display all student records')
    print('2. Display students whose last name begins with a certain string(case insensitive)')
    print('3. Display all records for students whose graduating year is a certain year')
    print('4. Display a summary report of each program for students graduating on/after a certain year')
    print('5. Add a new student record to the system')
    print('6. Quit')
    temp_choice = input('Please enter your query code： ').strip()
    is_valid = False
    choice = None
    while not is_valid:
        is_valid, error_type = validate(temp_choice)
        if is_valid:
            choice = int(temp_choice)
        else:
            if error_type == 'OUTOFBOUND':
                temp_choice = input('Unsupported query code. Please re-enter your query code: ')
            elif error_type == 'NONDIGIT':
                temp_choice = input('Unsupported query format. Please re-enter numerical query code： ')
    return choice


def validate(input):  # input is a tring which potentially represents a number
    if input.isdigit():
        if 1 <= int(input) <= 6:
            return True, 'NONE'
        else:
            return False, 'OUTOFBOUND'
    else:
        return False, 'NONDIGIT'


def display_all(InfoBook):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)
    print(InfoBook)


def search_last_name(InfoBook):
    lastname = input("Please enter certain beginning string of the Last name "
                     + "to start for searching for records:").strip()
    lastname = lastname.strip().capitalize()  # strip off leading and trailing spaces including tabs and capitalize and unify the user input

    if InfoBook['Last'].str.contains(lastname).any():
        print("------------------------------------------------------------------")
        print("Here is the students' records start with " + lastname + " : ")
        print(InfoBook[InfoBook['Last'].str.contains(lastname)])
        print("-------------------------------------------------------------------")

    else:
        print("No Record Found")


def search_graduating_year(InfoBook):
    ylist = InfoBook['GradYear'].tolist()
    year = input("Please enter the graduate year:").strip()
    while not year.isdigit():
        year = input("Non numerical input. Please re-enter the graduate year:").strip()
    year = int(year)
    if year in ylist:
        print("--------------------------------------------------------------------")
        print(f"Here are the students' records with graduate year in {year} : ")
        print(InfoBook[InfoBook['GradYear'] == year])
        print("--------------------------------------------------------------------")
    else:
        print(f"No matching records found for year： {year}")


def program_summary(InfoBook):
    L = len(InfoBook.index)

    print(
        "A Summary Report of Number and Percent of Students in Each Program, for Students Graduating On/After a Certain Year")
    Gradyr = int(input("Which year are you expecting students to graduate on/after?: "))
    # test if Gradyr exist in the dataset
    while Gradyr not in InfoBook.GradYear.values:
        Gradyr = int(input(
            "Not an eligible year. Please re-enter Which year your are expecting students to graduate on/after?: "))
    #
    print('\n')
    choice = str(input(f"is it on {Gradyr} or after {Gradyr}(Please enter O or A): ")).upper()
    while choice != 'O' and choice != 'A':
        choice = str(input(
            f"Your input is not eligible, please re-enter: is it on {Gradyr} or after {Gradyr}(Please enter O or A): ")).upper()
    if choice == "O":
        InfoBook0 = InfoBook[InfoBook['GradYear'] == Gradyr]

        print(f"a summary report of number and percent of students in MSGF, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSGF = InfoBook0[InfoBook0['DegreeProgram'] == 'MSGF']
        MSGF = len(InfoBook0_MSGF.index)
        P_MSGF = MSGF / L
        print(f"There are {MSGF} and {P_MSGF} percentage of students in MSGF, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSA, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSA = InfoBook0[InfoBook0['DegreeProgram'] == 'MSA']
        MSA = len(InfoBook0_MSA.index)
        P_MSA = MSA / L
        print(f"There are {MSA} and {P_MSA} percentage of students in MSA, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSSD, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSSD = InfoBook0[InfoBook0['DegreeProgram'] == 'MSSD']
        MSSD = len(InfoBook0_MSSD.index)
        P_MSSD = MSSD / L
        print(f"There are {MSSD} and {P_MSSD} percentage of students in MSSD, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSBA, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSBA = InfoBook0[InfoBook0['DegreeProgram'] == 'MSBA']
        MSBA = len(InfoBook0_MSBA.index)
        P_MSBA = MSBA / L
        print(f"There are {MSBA} and {P_MSBA} percentage of students in MSBA, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSIT, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSIT = InfoBook0[InfoBook0['DegreeProgram'] == 'MSIT']
        MSIT = len(InfoBook0_MSIT.index)
        P_MSIT = MSIT / L
        print(f"There are {MSIT} and {P_MSIT} percentage of students in MSIT, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSM, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSM = InfoBook0[InfoBook0['DegreeProgram'] == 'MSM']
        MSM = len(InfoBook0_MSM.index)
        P_MSM = MSM / L
        print(f"There are {MSM} and {P_MSM} percentage of students in MSM, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSMM, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSMM = InfoBook0[InfoBook0['DegreeProgram'] == 'MSMM']
        MSMM = len(InfoBook0_MSMM.index)
        P_MSMM = MSMM / L
        print(f"There are {MSMM} and {P_MSMM} percentage of students in MSMM, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSMI, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSMI = InfoBook0[InfoBook0['DegreeProgram'] == 'MSMI']
        MSMI = len(InfoBook0_MSMI.index)
        P_MSMI = MSMI / L
        print(f"There are {MSMI} and {P_MSMI} percentage of students in MSMI, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MST, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MST = InfoBook0[InfoBook0['DegreeProgram'] == 'MST']
        MST = len(InfoBook0_MST.index)
        P_MST = MST / L
        print(f"There are {MST} and {P_MST} percentage of students in MST, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSSC, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSSC = InfoBook0[InfoBook0['DegreeProgram'] == 'MSSC']
        MSSC = len(InfoBook0_MSSC.index)
        P_MSSC = MSSC / L
        print(f"There are {MSSC} and {P_MSSC} percentage of students in MSSC, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MBA, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MBA = InfoBook0[InfoBook0['DegreeProgram'] == 'MBA']
        MBA = len(InfoBook0_MBA.index)
        P_MBA = MBA / L
        print(f"There are {MBA} and {P_MBA} percentage of students in MBA, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MBAP, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MBAP = InfoBook0[InfoBook0['DegreeProgram'] == 'MBAP']
        MBAP = len(InfoBook0_MBAP.index)
        P_MBAP = MBAP / L
        print(f"There are {MBAP} and {P_MBAP} percentage of students in MBAP, graduating on {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MBAE, graduating on {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MBAE = InfoBook0[InfoBook0['DegreeProgram'] == 'MBAE']
        MBAE = len(InfoBook0_MBAE.index)
        P_MBAE = MBAE / L
        print(f"There are {MBAE} and {P_MBAE} percentage of students in MBAE, graduating on {Gradyr}")
        print('\n')

    if choice == "A":
        InfoBook0 = InfoBook[InfoBook['GradYear'] > Gradyr]

        print(f"a summary report of number and percent of students in MSGF, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSGF = InfoBook0[InfoBook0['DegreeProgram'] == 'MSGF']
        MSGF = len(InfoBook0_MSGF.index)
        P_MSGF = MSGF / L
        print(f"There are {MSGF} and {P_MSGF} percentage of students in MSGF, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSA, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSA = InfoBook0[InfoBook0['DegreeProgram'] == 'MSA']
        MSA = len(InfoBook0_MSA.index)
        P_MSA = MSA / L
        print(f"There are {MSA} and {P_MSA} percentage of students in MSA, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSSD, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSSD = InfoBook0[InfoBook0['DegreeProgram'] == 'MSSD']
        MSSD = len(InfoBook0_MSSD.index)
        P_MSSD = MSSD / L
        print(f"There are {MSSD} and {P_MSSD} percentage of students in MSSD, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSBA, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSBA = InfoBook0[InfoBook0['DegreeProgram'] == 'MSBA']
        MSBA = len(InfoBook0_MSBA.index)
        P_MSBA = MSBA / L
        print(f"There are {MSBA} and {P_MSBA} percentage of students in MSBA, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSIT, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSIT = InfoBook0[InfoBook0['DegreeProgram'] == 'MSIT']
        MSIT = len(InfoBook0_MSIT.index)
        P_MSIT = MSIT / L
        print(f"There are {MSIT} and {P_MSIT} percentage of students in MSIT, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSM, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSM = InfoBook0[InfoBook0['DegreeProgram'] == 'MSM']
        MSM = len(InfoBook0_MSM.index)
        P_MSM = MSM / L
        print(f"There are {MSM} and {P_MSM} percentage of students in MSM, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSMM, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSMM = InfoBook0[InfoBook0['DegreeProgram'] == 'MSMM']
        MSMM = len(InfoBook0_MSMM.index)
        P_MSMM = MSMM / L
        print(f"There are {MSMM} and {P_MSMM} percentage of students in MSMM, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSMI, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSMI = InfoBook0[InfoBook0['DegreeProgram'] == 'MSMI']
        MSMI = len(InfoBook0_MSMI.index)
        P_MSMI = MSMI / L
        print(f"There are {MSMI} and {P_MSMI} percentage of students in MSMI, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MST, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MST = InfoBook0[InfoBook0['DegreeProgram'] == 'MST']
        MST = len(InfoBook0_MST.index)
        P_MST = MST / L
        print(f"There are {MST} and {P_MST} percentage of students in MST, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MSSC, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MSSC = InfoBook0[InfoBook0['DegreeProgram'] == 'MSSC']
        MSSC = len(InfoBook0_MSSC.index)
        P_MSSC = MSSC / L
        print(f"There are {MSSC} and {P_MSSC} percentage of students in MSSC, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MBA, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MBA = InfoBook0[InfoBook0['DegreeProgram'] == 'MBA']
        MBA = len(InfoBook0_MBA.index)
        P_MBA = MBA / L
        print(f"There are {MBA} and {P_MBA} percentage of students in MBA, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MBAP, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MBAP = InfoBook0[InfoBook0['DegreeProgram'] == 'MBAP']
        MBAP = len(InfoBook0_MBAP.index)
        P_MBAP = MBAP / L
        print(f"There are {MBAP} and {P_MBAP} percentage of students in MBAP, graduating after {Gradyr}")
        print('\n')

        print(f"a summary report of number and percent of students in MBAE, graduating after {Gradyr}")
        print("--------------------------------------------------------------------------------------")
        InfoBook0_MBAE = InfoBook0[InfoBook0['DegreeProgram'] == 'MBAE']
        MBAE = len(InfoBook0_MBAE.index)
        P_MBAE = MBAE / L
        print(f"There are {MBAE} and {P_MBAE} percentage of students in MBAE, graduating after {Gradyr}")
        print('\n')


def add_new_student(InfoBook):
    existing_ids = InfoBook['ID'].tolist()
    newid = input('Please enter ID:').strip()
    is_valid_id = False
    while not is_valid_id:
        error_type = 'NONE'
        if not newid.isdigit():
            is_valid_id = False
            error_type = 'NONDIGIT'
        elif int(newid) in existing_ids:
            is_valid_id = False
            error_type = 'DUPLICATE'
        else:
            is_valid_id = True
            error_type = 'NONE'

        if not is_valid_id:
            if error_type == 'NONDIGIT':
                newid = input('Unsupported ID format. Please re-enter numerical ID:')
            elif error_type == 'DUPLICATE':
                newid = input('This ID already exists. Please re-enter ID:')

    newFirstname = input('Please enter First Name:').strip().capitalize()
    newlastname = input('Please enter Last Name:').strip().capitalize()
    newgrad = input('Please enter Graduation Year:').strip()
    newterm = input('Please enter Graduation Term:').strip().capitalize()
    newdp = input('Please enter Degree Program:').strip()
    print('Below is the new record: ')
    print(f'Student ID: {newid}')
    print(f'First Name: {newFirstname}')
    print(f'Last Name: {newlastname}')
    print(f'Graduation Year: {newgrad}')
    print(f'Graduation Term: {newterm}')
    print(f'Degree Program: {newdp}')
    req = input('Are you sure you want to add this record to the system?(yes/no):').strip()
    if req.lower() == "no":
        print("Adding new student record operation canceled.")
        return
    newindex = str(len(InfoBook))
    InfoBook.loc[newindex] = [int(newid), newFirstname, newlastname, newgrad, newterm, newdp]
    InfoBook.to_csv("Students.txt", index=False, sep="\t", quoting=csv.QUOTE_NONE)
    req = input('Record added successfully. Do you want to see the result?(yes/no):').strip()
    if req.lower() == 'yes':
        display_all(InfoBook)


main()
