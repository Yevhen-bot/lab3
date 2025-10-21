from main.repositories.IRepository import IRepository
from main.models import Role

class RoleRepository(IRepository):
    def get_all(self):
        return Role.objects.all()
    
    def get_by_id(self, id):
        return Role.objects.filter(id=id).first()

    def delete_all(self):
        return Role.objects.all().delete()

    def delete_by_id(self, id):
        return Role.objects.filter(id=id).delete()

    def add_one(self, role):
        return Role.objects.create(
            role=role
        )
    
    def update_by_id(self, id, role):
        return Role.objects.filter(id=id).update(
            role=role
        )
