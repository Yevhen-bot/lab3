from main.repositories.IPersonRepository import IPersonRepository
from main.models import Client
class ClientRepository(IPersonRepository):
    def get_all(self):
        return Client.objects.all()
    
    def get_by_id(self, id):
        return Client.objects.filter(id=id).first()
    
    def get_by_email(self, email):
        return Client.objects.filter(email=email).first()
    
    def get_by_phone_number(self, phone_number):
        return Client.objects.filter(phone_number=phone_number).first()

    def delete_all(self):
        return Client.objects.all().delete()[0]

    def delete_by_id(self, id):
        return Client.objects.filter(id=id).delete()

    # returns created enity
    def add_one(self, first_name, last_name, email, birth_date, phone_number):
        return Client.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            birth_date=birth_date,
            phone_number=phone_number
        )
    
    # returns count of updated rows
    def update_by_id(self, id, first_name, last_name, email, birth_date, phone_number):
        return Client.objects.filter(id=id).update(
            first_name=first_name,
            last_name=last_name,
            email=email,
            birth_date=birth_date,
            phone_number=phone_number
    )