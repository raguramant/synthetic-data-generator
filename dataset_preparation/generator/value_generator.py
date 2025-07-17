# file: dataset_preparation/generator/value_utils.py

from faker import Faker
import string

class ValueGeneratorUtils:

    def __init__(self, faker=None):
        if faker:
            self._faker = faker
        else:
            self._faker = Faker()



    def get_property_value_generators(self, schema:dict, include_nulls=True):

        properties = schema.get('properties', {})

        value_generators = {}

        for prop_name, prop_schema in properties.items():

            if prop_schema.get('type') == 'string':
                value_generators[prop_name] = self.get_string_generator(prop_name, prop_schema)
            elif prop_schema.get('type') == 'integer':
                value_generators[prop_name] = lambda: self._faker.random_int(min=0, max=1000)
            elif prop_schema.get('type') == 'boolean':
                value_generators[prop_name] = lambda: self._faker.boolean()
            elif prop_schema.get('type') == 'null' and include_nulls:
                value_generators[prop_name] = lambda: None
            else:
                value_generators[prop_name] = lambda: None


    def get_string_generator(self, property_name=None, prop_schema=None):
        if "enum" in prop_schema:
            return lambda: self._faker.random_element(elements=prop_schema["enum"])
        elif prop_schema.get("format") == "email":
            return lambda: self._faker.email()
        elif prop_schema.get("format") == "date":
            return lambda: self._faker.date()
        elif "minLength" in prop_schema or "maxLength" in prop_schema:
            description = prop_schema.get("description", "")
            if ("name" in description.lower() and "first" in description.lower()) or \
               ("name" in property_name.lower() and "first" in property_name.lower()):
                return lambda: self._faker.first_name()
            elif ("name" in description.lower() and "last" in description.lower()) or \
                 ("name" in property_name.lower() and "last" in property_name.lower()):
                return lambda: self._faker.last_name()
            elif ("name" in description.lower() and "middle" in description.lower()) or \
                 ("name" in property_name.lower() and "middle" in property_name.lower()):
                return lambda: self._faker.random_element(elements=list(string.ascii_uppercase))
            elif ("name" in description.lower() and "prefix" in description.lower()) or \
                 ("name" in property_name.lower() and "prefix" in property_name.lower()):
                return lambda: self._faker.prefix()
            elif ("name" in description.lower() and "suffix" in description.lower()) or \
                 ("name" in property_name.lower() and "suffix" in property_name.lower()):
                return lambda: self._faker.suffix()
            elif "name" in description.lower() or "name" in property_name.lower():
                return lambda: self._faker.name()
            else:
                return lambda: self._faker.pystr(min_chars=prop_schema.get("minLength", 1), max_chars=prop_schema.get("maxLength", 10))
        else:
            return lambda: self._faker.pystr(min_chars=1,max_chars=10)





