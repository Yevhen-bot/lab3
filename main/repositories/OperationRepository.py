from main.repositories.IRepository import IRepository
from main.models import Operation

class OperationRepository(IRepository):
    def get_all(self):
        return Operation.objects.all()
    
    def get_by_id(self, id):
        return Operation.objects.filter(id=id).first()

    def delete_all(self):
        return Operation.objects.all().delete()

    def delete_by_id(self, id):
        return Operation.objects.filter(id=id).delete()[0]

    def add_one(self, operation):
        return Operation.objects.create(
            operation=operation
        )
    
    def update_by_id(self, id, operation):
        return Operation.objects.filter(id=id).update(
            operation=operation
        )
