
class individualClass(object):
    def __init__(self, ID = 'NA', Name = 'NA', Gender = 'NA', Birthday = 'NA', Age = '0', Alive = 'NA', Death = 'NA', Child = 'NA', Spouse = 'NA'):
        self.ID =  ID
        self.Name = Name
        self.Gender = Gender
        self.Birthday = Birthday
        self.Age = Age
        self.Alive = Alive
        self.Death = Death
        self.Child = Child
        self.Spouse = Spouse

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

    def Set_child(self, Child):
        self.Child = Child
        
    def Set_spouse(self, Spouse):
        self.Spouse = Spouse

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
        return [self.ID, self.Name, self.Gender, self.Birthday, self.Age, self.Alive, self.Death, self.Child, self.Spouse]




