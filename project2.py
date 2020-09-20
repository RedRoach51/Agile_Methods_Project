from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
import datetime

def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
def from_dob_to_death(born,death):
    today = death
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))





# Path to your `.ged` file
file_path ='C:\\Users\\Pratim\\Desktop\\FamilyTree-suppada.ged'

# Initialize the parser
gedcom_parser = Parser()

# Parse your file
gedcom_parser.parse_file(file_path)

root_elements = gedcom_parser.get_element_list()

# Iterate through allelements
for element in root_elements:
    if element.get_tag == "INDI" or element.get_tag == "FAM":
        tag = "Y"
    else:
        tag = "N"
            
    print ("-->" + str(element))
    print ("<-- |" + str(element.get_level()) + "|" + (element.get_tag())+ "|" + tag+ "|" + str(element.get_value()) + "|")

info = {"INDI": [], "FAM":[]}
#for element in root_elements:          
#    print (str(element.get_tag()))
#    if str(element.get_tag()) == "INDI" or str(element.get_tag()) =="FAM":
#        if element.get_tag() == "INDI" and len(info[element.get_tag()]) > 5000:
#            raise ValueError("Too many individuals in file")
#        if element.get_tag() == "FAM" and len(info[element.get_tag()]) >1000:
#            raise ValueError("Too many families in file")
#        print("test")
#        info[str(element.get_tag())] = info[str(element.get_tag())]+ [(element.get_element_list())] 
        
#print (info)

months = {"JAN" : 1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9,"OCT":10,"NOV":11, "DEC":12}


for element in root_elements:
    age = 0
    if isinstance(element, IndividualElement):
        (first, last) = element.get_name()
        if(element.is_deceased() == True):
            
            bday = element.get_birth_data()[0]
            
            death = element.get_death_data()[0]
            bday = bday.split(" ")
            print (months[bday[1]])
            bday = datetime.date(int(bday[2]),int(months[bday[1]]), int(bday[0]))
            death = death.split(" ")
            death = datetime.date(int(death[2]),int(months[death[1]]), int(death[0]))
            #age = from_dob_to_age(dob)
            #age = from_dob_to_age(dob)
            age = from_dob_to_death(bday, death)
            
        else:
            #dob = datetime.date(element.get_birth_data()[0])
            dob = element.get_birth_data()[0].split(" ")
            dob = datetime.date(int(dob[2]),int(months[dob[1]]), int(dob[0]))
            age = from_dob_to_age(dob)
        info[str(element.get_tag())] = info[str(element.get_tag())] + [(first+ " " + last, element.get_gender(), element.get_birth_data()[0], age, "Alive: " + str(not element.is_deceased()))] 
        if  (element.is_deceased()):
            info[str(element.get_tag())]= info[str(element.get_tag())] + ["Death Date: " + element.get_death_data()[0]]
        else:
            info[str(element.get_tag())]= info[str(element.get_tag())] + ["NA"]

        if (element.is_child()):
            info[str(element.get_tag())] = info[str(element.get_tag())] + ["Child: " + str(element.is_child())] # have to check for id
        else:
            info[str(element.get_tag())] = info[str(element.get_tag())] + ["Child: " + "Not a child"]
        
                
print(info)

#level, tag, valid?, arguments
