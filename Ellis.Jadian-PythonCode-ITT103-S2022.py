#Author: JADIAN ELLIS
#Date Created: Monday, April 25, 2022
#Course: ITT103
#Purpose: This program will find the appropriate commission rate based on the sales representative's class, compute the commission earned and print the 
    # Sales Representative Commission Report for JamEx Limited. It will loop indefinitely until the predetermined termination trigger is entered.
#NAME OF PROGRAM: JamEx Limited Salesperson Commission Report

from pickle import FALSE, TRUE
import string

#A user defined function is used to perform error handling for the variable fName to ensure the value inputted is valid and does not contain any symbols nor numbers.
def confirmfName():
    #To ensure the values stored within these variables is not limited to the function, they are declared as global variables 
    global fName
    special_chr = set(string.punctuation)
    
    #The variable is being initialized pending use in WHILE DO loop.
    fConfirm=int(0)

    while fConfirm == 0:
        fName = input("What is your first name.")

        #Nested IF-THEN-ELSE statements that check if the input contains a symbol and/or digit.
        if any(dig.isdigit() for dig in fName):
            
            #The appropriate error message is displayed if a symbol is detected within the string.
            print("An error has been detected. Please ensure no numbers are inserted.")
            confirm1=int(0)
        else:
            confirm1=int(1)

        if any( spec in special_chr for spec in fName):
            #The appropriate error message is displayed if a number is detected within the string.
            print("Symbols are not an acceptable input.")
            confirm2=int(0)
        else:
            confirm2=int(1)
            
        #The variable for final confirmation, fConfirm is updated pending re-testing of the while loop condition.
        #If either confirm1 or confirm2 contain a symbol or number, the final confirm will continue loop until the data type is acceptable.
        fConfirm =(int(confirm1*confirm2))

#A user defined function is used to perform error handling for the variable surName to ensure the value inputted is valid and does not contain any symbols nor numbers.
def confirmsurName():
    #To ensure the values stored within these variables is not limited to the function, they are declared as global variables 
    global surName
    special_chr = set(string.punctuation)
    
    #The variable is being initialized pending use in WHILE DO loop.
    fConfirm=int(0)

    while fConfirm == 0:
        surName = input("What is your last name.")

        #Nested IF-THEN-ELSE statements that check if the input contains a symbol and/or digit.
        if any(dig.isdigit() for dig in surName):
            #The appropriate error message is displayed if a symbol is detected within the string.
            print("An error has been detected. Please ensure no numbers are inserted.")
            confirm1=int(0)
        else:
            confirm1=int(1)

        if any( spec in special_chr for spec in surName):
            #The appropriate error message is displayed if a number is detected within the string.
            print("Symbols are not an acceptable input.")
            confirm2=int(0)
        else:
            confirm2=int(1)

        #The variable for final confirmation, fConfirm is updated pending re-testing of the while loop condition.
        #If either confirm1 or confirm2 contain a symbol or number, the final confirm will continue loop until the data type is acceptable.
        fConfirm =(int(confirm1*confirm2))

#A user defined function is used to perform error handling to ensure the value inputted by the user is valid (does not contain symbols, empty entry nor negative figure).
def confirmRepID():

    #To ensure the values stored within these variables is not limited to the function, they are declared as global variables 
    global saleRepNum
    while True:
        try:
            saleRepNum=int(input("Please enter the unique salesperson number. "))
            break
        except ValueError:

            #The appropriate error message is displayed if a symbol, letter or empty value is detected within saleRepNum variable.
            print("There is an error with the ID number entered, please try again.")
            continue
    while saleRepNum<0:
        
        #The appropriate error message and prompt are displayed if a negative value is detected within saleRepNum variable.
        saleRepNum=int(input("This cannot be a negative figure, please try again. What is the unique salesperson number? "))

#A user defined function is used to perform error handling to ensure the value inputted by the user is valid.
def confirmSalesAmt():

    #To ensure the values stored within these variables is not limited to the function, they are declared as global variables 
    global salesAmt
    while True:
        try:
            salesAmt=float(input("Please enter the amount of sales. $ "))
            break
        except ValueError:

            #The appropriate error message is displayed if a symbol, letter or empty value is detected within salesAmt variable.
            print("An error has occured. Please try again using numbers only.")
            continue
    #WHILE-DO Loop to ensure the sales amount is positive, and gives an error message otherwise.
    while salesAmt<0:
        #The appropriate error message and prompt are displayed if a negative value is detected within salesAmt variable.
        salesAmt=float(input("The amount of sales figure cannot be less than zero, please try again. What is the unique salesperson number? "))

#A user defined function is used to perform error handling to ensure the value inputted by the user is valid.   
def confirmClass():

    #To ensure the values stored within these variables is not limited to the function, they are declared as global variables.
    global s_class
    while True:
        try:
            s_class=int(input("Which class category does the salesperson belong to? "))
            break
        except ValueError:
            
            #The appropriate error message is displayed if a symbol, letter or empty value is detected within s_class variable.
            print("There is an error with the class number entered, please try again using numbers.")
            continue
    #WHILE-DO Loop to ensure the class is within the respective range (1 to 3), and gives an error message otherwise.
    while s_class < 1 or s_class > 3:
        
        #The appropriate error message and prompt are displayed if a value outside the range of 1 to 3 is detected within s_class variable.
        s_class=int(input("I am sorry, the information entered for the saleperson's class category is not within the respective range. Please enter a valid class category. "))

#A user defined function is used to capture data needed from the user.
def getData():
    
    #The user is being prompted to input essential information needed for the program. The respective data is being accepted and stored in the corresponding variables.
    #Each function called will prompt the user input, verify the validity of the input before accepting and storing the value.
    confirmfName()
    confirmsurName()
    confirmRepID()
    confirmSalesAmt()
    confirmClass()

#The getData function is called to action and information is collected from the user.
getData()

#The variable count, which is used to count the amount of entry records, is assigned an initial value.
count=int(1)

#The variable trig, which is used to continue or terminate information entry and report printing - WHILE DO Loop, is set to an initial value.
trig = TRUE

#Nested WHILE-DO Loop which will display the appropriate error messages, process calculations, print the commission report and promt the user for the information for 
    # the consecutive entry.
while trig == TRUE:
    if s_class == 1 or s_class == 2 or s_class == 3:
        print("The sales representative's class information entered has been accepted.")

    #Nested IF-THEN-ELSE statement to derive at the respective commission rate based on the sales amount 
       #and the class category entered.
    if s_class == 1:
        #Nested IF-THEN-ELSE statement to derive at the respective commission rate based on the 
            #sales amount entered
        if salesAmt == 1000 or salesAmt < 1000:
            comm_rate = 0.06
            #Given that the amount of sales in class 1 is below or equal to $1,000.00 then the commission rate is 6%.
        elif salesAmt > 1000 and salesAmt < 2000:
                comm_rate = 0.07
                #Given that the amount of sales in class 1 is between $1,000.00 and $2,000.00 then the commission rate is 7%.
        else:
                comm_rate = 0.1
                #Given that the amount of sales in class 1 is above or equal to $2,000.00 then the commission rate is 10%.
    elif s_class == 2:
        if salesAmt < 1000:
            comm_rate = 0.04
            #Given that the amount of sales in class 2 is below $1,000.00 then the commission rate is 4%.
        else:       
            comm_rate = 0.06
            #Given that the amount of sales in class 2 is above or equal to $1,000.00 then the commission rate is 6%.
    else: comm_rate = 0.045
    #For class 3 the standard commission rate is 4.5%.
    
    #Internal Program Process - formula to calculate the commission amount.
    commission=float(comm_rate * salesAmt)

    #Print the Salesperson's information to the user displaying the Commission Report per entry.
    print("Sales Rep. Information - Entry Number:", count)
    print("Sales Representative's First name:", fName)
    print("Sales Representative's Surname:", surName)
    print("Sales Representative ID Number:", saleRepNum)
    print("Sales Representative Class Category:", s_class)
    #The sales amount is rounded to two decimal places.
    print("Sales Amount: $", "{:.2f}".format(salesAmt))
    #The commission rate is converted from decimal to percentage format.
    print("Commission Rate:", comm_rate*100, "%")
    #The commission earned is rounded to two decimal places.
    print("Commission Earned: $", "{:.2f}".format(commission))
    
    #Prompt request for the user to continue to input information for anther Sales Representative. Then accept the data and store in the respective variable.
    infoReq=input("Would you like to input the information for another sales representative? Please enter 'Y' for yes and to continue the program. ")
    if infoReq == "Y" or infoReq == "y":
        trig = TRUE
        print("You have opted to continue the program and enter another record.")
    else:
        trig = FALSE
        print("You have opted to terminate the program.")

    #Once the user chose to continue after entering 'Y' or 'y', they will receive a prompt to input information for the next entry.            
    if trig == TRUE:

        #The function getData is called to action.
        getData()

        #Increment for number of entry records.
        count=int(count+1)
#The nested WHILE-DO Loop will terminate once the user enters the predefined value.

#The message below is displayed after the user chooses to terminate the program and the WHILE-DO Loop has been terminate.
print("The total number of Salesperson's Commission Reports for JamEx Limited that have been processed is", count, ".")
