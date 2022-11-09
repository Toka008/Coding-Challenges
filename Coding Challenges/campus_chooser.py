
def user_details():
    getFirstName()
    getLastName()
    getCohortYear()

def create_user_name(first_name, last_name, cohort, final_campus):
    print("First name :" , first_name)
    print("Last name :" , last_name)
    print("Cohort year :", cohort)
    print("Final Campus: ",final_campus)
    
    #############################################
    #Algorithm for creating user name goes here #
    #use the above variables to create user name#                  #        -  here and display  it -         #      
    #############################################
    
    
    
    
#Checks for numbers in words
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
        else:
            return False
    
#Get Name    
def getFirstName():
    name =   input("Please Enter Your First Name : ")
     #Check Numbers in  first name
    if containsNumber(name) == False:
         first_name = name
         
         return first_name
    else :
         print("Your first name should contain none numerical values try again")
         #Repeat if it has numerical values 
         getFirstName()
                    
            
#Get Last Name        
def getLastName():
    surname =  input("Please Enter Your Last name : ")
    #Check Numbers in  last  name
    if containsNumber(surname) == False :
       last_name = surname 
       return last_name 
    else :   
        print("Your last name should contain none numerical values try again")
        #Repeat if it has numerical values 
        getLastName()
    
    
    
 #Get Year of Cohort 
def getCohortYear():
      #Convert string for comparing
      year = int(input("Which year are you applying for :"))
      #Check if cohort is not in past
      if year >=2022:
        cohort = year
        return cohort 
      else :
           ("invalid year try again ! ")
           getCohortYear()#Restart if cohort year invalid 
           
           
           
#Get Campus
def user_campus():
     #Options
     print("- Select campus ")
     print("Reply 1 for Johannesburg ")
     print("Reply 2 for Durban")
     print("Reply 3 for Cape Town")
     print()
     
     
     
     #selection of campus
     selection = int(input("Enter your campus selection :"))
     if selection < 4 and selection > 0:#Makes sure between 1 2 3
         if selection == 1:
            final_campus = "JHB"
            return final_campus
         elif selection == 2:
            final_campus = "DBN"
            return final_campus
         else: 
            final_campus = "CPT"
            return final_campus
     else:
            getFinalCampus()# Restarts if value is not between 1 2 3 
              
              
    
create_user_name(getFirstName(), getLastName(), getCohortYear(),user_campus())#This is the running code overall NB IT GETS AND Prints 