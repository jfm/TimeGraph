import configparser
from pathlib import Path


class Settings:

    def __init__(self, path):
        self.config = configparser.RawConfigParser()
        config_file_path = Path(path)
        if config_file_path.is_file():
            self.config.read(path)
        else:
            config_file_path.open(mode='w')

    def save_property(self, key, value):
        pass

    def load_property(self, key):
        pass

# '~/.config/timegraph/session.properties'