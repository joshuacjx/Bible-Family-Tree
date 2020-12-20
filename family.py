import pandas as pd


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


PERSON_FILEPATH = "person.csv"
RELATIONSHIP_FILEPATH = "relationship.csv"

# Generate dataframes
person_data = pd.read_csv(PERSON_FILEPATH)
relationship_data = pd.read_csv(RELATIONSHIP_FILEPATH)

puml_text = ""

# Collect all person data
persons = []
for index, row in person_data.iterrows():
    person = Person(str(row['person_id']).replace(" ", "_"), str(row['person_name']))
    persons.append(person)

# Declare all persons
for person in persons:
    puml_text += "class \"" + person.get_name() + "\" as " + person.get_id() + "\n"

print(puml_text)


