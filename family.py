import pandas as pd


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.children = set()
        self.mother = None
        self.father = None

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def add_child(self, child):
        self.children.add(child)

    def set_mother(self, mother):
        self.mother = mother

    def set_father(self, father):
        self.father = father


class Marriage:
    def __init__(self, husband, wife):
        self.husband = husband
        self.wife = wife

    def get_husband(self):
        return self.husband

    def get_wife(self):
        return self.wife


PERSON_FILEPATH = "person.csv"
RELATIONSHIP_FILEPATH = "relationship.csv"

# Generate dataframes
person_data = pd.read_csv(PERSON_FILEPATH)
relationship_data = pd.read_csv(RELATIONSHIP_FILEPATH)

puml_text = ""

# Collect all person data
persons = dict()
for index, row in person_data.iterrows():
    name = str(row['person_name'])
    id = str(row['person_id']).replace(" ", "_")
    person = Person(id, name)
    persons[id] = person

# Declare all persons
for person in persons.values():
    puml_text += "class \"" + person.get_name() + "\" as " + person.get_id() + "\n"

# Collect all parental data


print(puml_text)


