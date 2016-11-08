import os
import yaml


def load_yaml(yaml_file):
    with open(yaml_file) as f:
        return yaml.load(f)

directory = os.path.dirname(os.path.realpath(__file__))
app = load_yaml(os.path.join(directory, 'app.yaml'))