from configparser import ConfigParser
import config.appConfig as appConfig


class InfoLogin:
    user_name: str = ''
    pwd: str = ''
    pin: str = ''

    def __init__(self, user_name: str, pwd: str, pin: str):
        self.user_name = user_name
        self.pwd = pwd
        self.pin = pin


class EnvConfig:
    __instance__ = None
    INFO_LOGIN_SECTION_KEY: str = 'INFO_LOGIN'

    def __init__(self):
        if EnvConfig.__instance__ is None:
            try:
                config: ConfigParser = ConfigParser()
                config.read(appConfig.ENV_FILE_PATH)

                user_name = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'UserName')
                pwd = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'Password')
                pin = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'PIN')

                self.infoLogin = InfoLogin(user_name=user_name, pwd=pwd, pin=pin)

                EnvConfig.__instance__ = self
            except Exception as ex:
                print("Load evn.ini error", ex)
        else:
            raise Exception("You cannot create another EnvConfig class")

    @staticmethod
    def getInstance():
        """ Static method to fetch the current instance.
        """
        if not EnvConfig.__instance__:
            EnvConfig()
        return EnvConfig.__instance__
