from main.repositories.IRepository import IRepository
from abc import abstractmethod

class IPersonRepository(IRepository):
    @abstractmethod
    def get_by_email(self, email):
        pass

    @abstractmethod
    def get_by_phone_number(self, phone_number):
        pass