#! /usr/bin/env python3
from environment_config.options import Options, OptionsBuilder
from configobj import ConfigObj
import os
import json
import re

print("running")

secret_matcher = re.compile(r"\$\{\{(?P<secret>.*)\}\}")

def secret_exporter(config: tuple, secrets: dict):
    (key, value) = config
    match = secret_matcher.match(value)
    if not match:
        os.environ[key] = value
    else:
        secret_name = match["secret"].strip()
        os.environ[key] = secrets[secret_name] or None

    print(f'{key}={os.environ[key]}')


def load_secrets(options: Options) -> dict:
    if not os.path.isfile(options.secret_path):
        return {}
    
    return json.load(options.secret_path)

def parse_file(file) -> dict:
    print(f"reading file {file}")
    if os.path.isfile(file):
        return ConfigObj(file)
    else:
        return {}


def load_configs(options: Options) -> dict:
    return parse_file(options.get_base_file()) | \
        parse_file(options.get_environment_file())