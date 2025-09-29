import yaml
import json

def get_static_schema():
    # Load static schema definition
    with open("schemas/schema_static.json", "r") as f:
        return json.load(f)

def get_dynamic_schema():
    with open("schemas/schema_dynamic.yaml", "r") as f:
        return yaml.safe_load(f)
