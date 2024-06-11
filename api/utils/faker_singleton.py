import os

from faker import Faker

from api.utils.custom_providers import medical_professions_provider, payment_method_provider, record_locator_provider


class SingletonMeta(type):
    """
    A Singleton metaclass. All classes with this metaclass will only have one instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonFaker(metaclass=SingletonMeta):
    """
    A Singleton wrapper for the Faker class.
    """

    def __init__(self):
        self.faker = Faker(os.getenv('FAKER_I18N', 'en_US'))
        self.faker.add_provider(medical_professions_provider)
        self.faker.add_provider(payment_method_provider)
        self.faker.add_provider(record_locator_provider)

    def set_locale(self, locale):
        """
        Set a new locale for the Faker instance.
        """
        self.faker = Faker(locale)

    def __getattr__(self, name):
        return getattr(self.faker, name)
