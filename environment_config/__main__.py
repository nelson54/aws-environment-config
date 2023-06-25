#! /usr/bin/env python3

from environment_config.options import Options, OptionsBuilder
from configobj import ConfigObj
import os
import json
import re
import argparse
import subprocess

cmd = os.environ["RUN"]

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

parser = argparse.ArgumentParser(prog = 'environment_config')
parser.add_argument('--configs', '-c', required=False, default="settings")
parser.add_argument('--environment', '-e', required=False, default="local")
parser.add_argument('--extension', '-x', required=False, default="properties")
parser.add_argument('--file', '-f', required=False, default="config")
parser.add_argument('--secret', '-s', required=False, default="/run/secrets/env")

args = parser.parse_args()
ob = OptionsBuilder(os.getcwd())
ob.folder = args.configs
ob.environment = args.environment
ob.extension = args.extension
ob.file_name = args.file
ob.secret_path = args.secret

options = ob.build()
secrets = load_secrets(options)

for k, v in load_configs(options).items():
    secret_exporter((k, v), secrets)

print(cmd)
if(cmd):
    cmd = cmd.split()
    print(cmd)
    subprocess.Popen(cmd)
