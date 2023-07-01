
import os
import argparse
from environment_config.options import Options, OptionsBuilder
parser = argparse.ArgumentParser(prog = 'environment_config')

ob = OptionsBuilder(os.getcwd())
ob.folder = args.configs
ob.environment = args.environment
ob.extension = args.extension
ob.file_name = args.file
ob.secret_path = args.secret

options = ob.build()
secrets = load_secrets(options)