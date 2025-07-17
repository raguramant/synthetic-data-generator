from dataset_preparation.generator.value_generator import ValueGeneratorUtils
import json
import jsonschema



def get_nm1_segment(rec):
    entity_identifier_code = rec.get("entity_identifier_code", "")
    entity_type_qualifier = rec.get("entity_type_qualifier", "")
    name_last_or_organization_name = rec.get("name_last_or_organizationName", "")
    name_first = rec.get("name_first", "")
    name_middle = rec.get("name_middle", "")
    name_prefix = rec.get("name_prefix", "")
    name_suffix = rec.get("name_suffix", "")
    identification_code_qualifier = rec.get("identification_code_qualifier", "")
    identification_code = rec.get("identification_code", "")
    return f"NM1*{entity_identifier_code}*{entity_type_qualifier}*{name_last_or_organization_name}*{name_first}*{name_middle}*{name_prefix}*{name_suffix}*{identification_code_qualifier}*{identification_code}~"


def validate_json(json_data, target_schema=None) -> bool:
    try:
        jsonschema.validate(instance=json_data, schema=target_schema)
        return True
    except jsonschema.ValidationError as e:
        print(f"Validation error for object: {e}")
        return False


def remove_none(d):
    if isinstance(d, dict):
        return {k: remove_none(v) for k, v in d.items() if v is not None}
    elif isinstance(d, list):
        return [remove_none(v) for v in d if v is not None]
    else:
        return d

with open("../name_schema.json", "r") as f:
    schema = json.load(f)

value_generator_utils = ValueGeneratorUtils()
generators = value_generator_utils.get_property_value_generators(schema, include_nulls=True)


with open("../../data/combinations.jsonl", "w") as outfile:
    no_of_training_records = 100
    records_generated = 0
    while records_generated < no_of_training_records:
        record = {}
        for key, generator in generators.items():
            record[key] = generator()

        record['nm1_segment'] = get_nm1_segment(record)
        record = remove_none(record)

        if validate_json(record, schema):
            json.dump(record, outfile)
            outfile.write("\n")
            records_generated += 1
            print(record)





