
def is_float(value):
    try:
        # caster une valeur
        float(value)
        return True
    except ValueError:
        return False


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

class Passenger:
    def __init__(self, id, name, survived, sex, age):
        self.id = id
        self.survived = survived
        self.sex = sex
        self.age = age
        self.name = name

    def getId(self):
        return self._id

    def setId(self, value):
        self._id = value

    def getSurvived(self):
        return self._survived

    def setSurvived(self, value):
        if is_int(value):
            self._survived = int(value)
        else:
            self._survived = None

    def getSex(self):
        return self._sex

    def getSex(self, value):
        # TODO pour savoir si un champ n'existe pas dans le CSV qu'est ce que l'on fait ?
        if bool(value.trim()) and value.upper() in ('FEMALE', 'MALE', 'OTHER'):
            self._sex = value.upper()[0]

    def getAge(self):
        return self.age

    def setAge(self, value):
        # TODO
        if bool(value.trim()) \
                and is_float(value):
            self.age = float(value)

    def getName(self):
        return self._id

    def setName(self, value):
        self.name = value
