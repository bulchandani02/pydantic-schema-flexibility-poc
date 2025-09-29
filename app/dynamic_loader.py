import yaml
from pydantic import create_model
from typing import Optional

def load_dynamic_model(schema_path: str):
    with open(schema_path, 'r') as f:
        schema = yaml.safe_load(f)
    fields = {}
    for field_name, props in schema['fields'].items():
        field_type = str if props['type'] == "str" else eval(props['type'])
        if props.get('required', False):
            fields[field_name] = (field_type, ...)
        else:
            fields[field_name] = (Optional[field_type], None)
    DynamicModel = create_model(schema['name'], **fields)
    return DynamicModel
