import os
import argparse
from environment_config.options import OptionsBuilder

from environment_config.environment_config import load_secrets, load_configs, secret_exporter

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

