
class individualClass(object):
    def __init__(self, ID = 'NA', Name = 'NA', Gender = 'NA', Birthday = 'NA', Age = '0', Alive = 'NA', Death = 'NA', Child =[], Spouse = []):
        self.ID =  ID
        self.Name = Name
        self.Gender = Gender
        self.Birthday = Birthday
        self.Age = Age
        self.Alive = Alive
        self.Death = Death
        self.Child = []
        self.Spouse = []

    def Set_ID(self, ID):
        self.ID = ID

    def Set_name(self, Name):
        self.Name = Name

    def Set_gender(self, Gender):
        self.Gender = Gender

    def Set_birthday(self, Birthday):
        self.Birthday = Birthday

    def Set_age(self, Age):
        self.Age = Age

    def Set_alive(self, Alive):
        self.Alive = Alive

    def Set_death(self, Death):
        self.Death = Death

    def Set_child(self, Child_arg):
        self.Child.append(Child_arg)

    def Set_spouse(self, Spouse_arg):
        self.Spouse.append(Spouse_arg)

    def Get_ID(self):
        return self.ID

    def Get_name(self):
        return self.Name

    def Get_gender(self):
        return self.Gender

    def Get_birthday(self):
        return self.Birthday

    def Get_age(self):
        return self.Age

    def Get_alive(self):
        return self.Alive

    def Get_death(self):
        return self.Death

    def Get_child(self):
        return self.Child

    def Get_spouse(self):
        return self.Spouse

    def Get_details(self):
        if(self.Child == [] and self.Spouse == []):
            return [self.ID, self.Name, self.Gender, self.Birthday, self.Age, self.Alive, self.Death, 'NA', 'NA']
        elif(self.Spouse == []):
            return [self.ID, self.Name, self.Gender, self.Birthday, self.Age, self.Alive, self.Death, self.Child, 'NA']
        elif(self.Child == []):
            return [self.ID, self.Name, self.Gender, self.Birthday, self.Age, self.Alive, self.Death, 'NA', self.Spouse]
        else:
            return [self.ID, self.Name, self.Gender, self.Birthday, self.Age, self.Alive, self.Death, self.Child, self.Spouse]

    def Check_valid_birth_death(self):
        if (self.Death == "NA"):
            return True;
        deathDate = self.Get_death();
        birthDate = self.Get_birthday();

        countDeath = int(deathDate[:deathDate.find("-")])
        countBirth = int(birthDate[:birthDate.find("-")])

        if (countDeath < countBirth):
            return False;
        if (countDeath > countBirth):
            return True;

        deathDate = deathDate[deathDate.find("-") + 1:]
        birthDate = birthDate[birthDate.find("-") + 1:]

        countDeath = int(deathDate[:deathDate.find("-")])
        countBirth = int(birthDate[:birthDate.find("-")])
        if (countDeath < countBirth):
            return False;
        if (countDeath > countBirth):
            return True;

        deathDate = deathDate[deathDate.find("-") + 1:]
        birthDate = birthDate[birthDate.find("-") + 1:]
        countDeath = int(deathDate);
        countBirth = int(birthDate);
        if (countDeath <= countBirth):
            return False;
        return True;



