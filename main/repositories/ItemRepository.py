from main.repositories.IRepository import IRepository
from main.models import Item

class ItemRepository(IRepository):
    def get_all(self):
        return Item.objects.all()
    
    def get_by_id(self, id):
        return Item.objects.filter(id=id).first()

    def delete_all(self):
        return Item.objects.all().delete()

    def delete_by_id(self, id):
        return Item.objects.filter(id=id).delete()

    def add_one(self, description, name):
        return Item.objects.create(
            description=description,
            name=name
        )
    
    def update_by_id(self, id, description, name):
        return Item.objects.filter(id=id).update(
            description=description,
            name=name
        )
