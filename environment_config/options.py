import os

class OptionsBuilder:
    secret_path = "/run/secrets/env"
    application = "application"
    folder = "settings"
    file_name = "config"
    environment = "local"
    extension = "properties"

    def __init__(self, cwd):
        self.cwd = cwd

    def build(self):
        return Options(
            self.cwd,
            self.secret_path,
            self.application,
            self.folder,
            self.file_name,
            self.environment,
            self.extension
        )

class Options:
    """
    Options for loading classes
    """

    def __init__(
        self,
        cwd: str,
        secret_path: str = "/run/secrets/env",
        application: str = None,
        folder: str = "settings",
        file_name: str = "config",
        environment: str = "local",
        extension: str = "properties"
    ):
        self.cwd = cwd
        self.secret_path = secret_path
        self.application = application
        self.folder = folder
        self.file_name = file_name
        self.environment = environment
        self.extension = extension

    

    def has_environment(self):
        return not not self.environment

    def get_full_path(self, file) -> str:
        return os.path.join(self.cwd, self.folder, file)
    
    def get_base_file(self) -> str:
        return self.get_full_path(f'{self.file_name}.{self.extension}')

    def get_environment_file(self) -> str:
        if(self.environment):
            return self.get_full_path(f'{self.file_name}-{self.environment}.{self.extension}')
        return False
