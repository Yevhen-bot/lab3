from main.repositories.IRepository import IRepository
from main.models import Store

class StoreRepository(IRepository):
    def get_all(self):
        return Store.objects.all()
    
    def get_by_id(self, id):
        return Store.objects.filter(id=id).first()

    # returns (count of ALL deleted rows, dictionary of 'name' - times deleted) 
    def delete_all(self):
        return Store.objects.all().delete()

    def delete_by_id(self, id):
        return Store.objects.filter(id=id).delete()[0]

    # returns created entity
    def add_one(self, name, country, street, city, house_number):
        return Store.objects.create(
            name=name,
            country=country,
            street=street,
            city=city,
            house_number=house_number
        )
    
    # returns count of updated rows
    def update_by_id(self, id, name, country, street, city, house_number):
        return Store.objects.filter(id=id).update(
            name=name,
            country=country,
            street=street,
            city=city,
            house_number=house_number
        )
