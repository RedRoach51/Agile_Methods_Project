from project2 import processGedFile

'''
Author: Srikanth Uppada
User story 07:
Requirement: Death should be less than 150 years after birth for dead people, 
             and current date should be less than 150 years after birth for all living people
'''

# Method: userStory07_150yrs
def userStory07_150yrs(file):

    # Fetch the parsed object's from input ged file
    indiDict, famDict = processGedFile(file)
    # Create a list of
    resultList = list()

    # Process through all individual's details
    for index in indiDict:

        # Fetch individual details like age, deceased, ID, birthdDate and deathDate.
        individualAge= indiDict[index].Get_age()
        isIndiAlive = indiDict[index].Get_alive()
        individualID = indiDict[index].Get_ID()
        birthDate = indiDict[index].Get_birthday()
        deathDate = indiDict[index].Get_death()

        # If Age is greater than or equal to 150 prompt Invalid data
        if (individualAge >= 150):
            # Check if an individual is alive or not
            if (isIndiAlive == False):
                #error 1
                result_1_str = f"ERROR: INDIVIDUAL: US07: {individualID} More than 150 years old at death - Birth {birthDate}: Death {deathDate}"
                resultList.append(result_1_str)
            else:
                # error 2
                result_2_str = f"ERROR: INDIVIDUAL: US07: {individualID} More than 150 years old - Birth date {birthDate}"
                resultList.append(result_2_str)

    # Print the information of validated data
    for output in resultList:
        print(output)

    # return the list of validated data
    return resultList

# userStory07's Main function
if __name__ == "__main__":
   userStory07_150yrs("FamilyTree.ged")