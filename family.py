import pandas as pd
from enum import Enum


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


class RelationshipType(Enum):
    WIFE = 1
    FATHER = 2


class Relationship:
    def __init__(self, id, from_person, to_person, type: RelationshipType):
        self.id = id
        self.from_person = from_person
        self.to_person = to_person
        self.type = type

    def get_id(self):
        return self.id

    def get_from_person(self):
        return self.from_person

    def get_to_person(self):
        return self.to_person

    def get_type(self):
        return self.type


PERSON_FILEPATH = "person.csv"
RELATIONSHIP_FILEPATH = "relationship.csv"

PLACEHOLDER_NAME = "-"

# Generate dataframes
person_data = pd.read_csv(PERSON_FILEPATH)
relationship_data = pd.read_csv(RELATIONSHIP_FILEPATH)

puml_text = "@startuml" + "\n" + "skinparam monochrome true" + "\n" + "hide empty members" + "\n" + "hide circle" + "\n"

# Collect all person data
persons = dict()
for index, row in person_data.iterrows():
    person_name = str(row['person_name'])
    person_id = str(row['person_id']).replace(" ", "_")
    person = Person(person_id, person_name)
    persons[person_id] = person

# Collect all relationship data
relationships = dict()
for index, row in relationship_data.iterrows():
    relationship_id = str(row['person_relationship_id']).replace(" ", "_")
    from_person_id = str(row['person_id_1']).replace(" ", "_")
    to_person_id = str(row['person_id_2']).replace(" ", "_")

    if from_person_id not in persons:
        persons[from_person_id] = Person(from_person_id, PLACEHOLDER_NAME)
    if to_person_id not in persons:
        persons[to_person_id] = Person(to_person_id, PLACEHOLDER_NAME)
    from_person = persons[from_person_id]
    to_person = persons[to_person_id]

    type = str(row['relationship_type'])
    if type == "wife":
        relationship = Relationship(relationship_id, from_person, to_person, RelationshipType.WIFE)
        relationships[relationship_id] = relationship
    elif type == "father":
        relationship = Relationship(relationship_id, from_person, to_person, RelationshipType.FATHER)
        relationships[relationship_id] = relationship
    else:
        pass

# Declare all persons
for person in persons.values():
    puml_text += "class \"" + person.get_name() + "\" as " + person.get_id() + "\n"

# Declare all relationships
for relationship in relationships.values():
    from_person_id = relationship.get_from_person().get_id()
    to_person_id = relationship.get_to_person().get_id()
    type = relationship.get_type()

    if type is RelationshipType.WIFE:
        puml_text += from_person_id + " .right. " + to_person_id + "\n"
    if type is RelationshipType.FATHER:
        puml_text += from_person_id + " --> " + to_person_id + "\n"


puml_text += "@enduml" + "\n"

print(puml_text)


