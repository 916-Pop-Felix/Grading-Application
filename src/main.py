
from Domain.Settings import Settings


if __name__ == '__main__':
    settings=Settings("settings.properties")
    settings.read_settings()
    settings.config()
