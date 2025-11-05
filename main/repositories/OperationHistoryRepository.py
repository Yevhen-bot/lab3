from main.repositories.IRepository import IRepository
from main.models import *

class OperationHistoryRepository(IRepository):
    def get_all(self):
        return OperationHistory.objects.all()
    
    def get_by_id(self, id):
        return OperationHistory.objects.filter(id=id).first()

    def delete_all(self):
        return OperationHistory.objects.all().delete()

    def delete_by_id(self, id):
        return OperationHistory.objects.filter(id=id).delete()[0]

    def add_one(self, client, item, operation, store, date, price, info):
        return OperationHistory.objects.create(
            operation=operation,
            client=client,
            item=item,
            store=store,
            date=date,
            price=price,
            info=info
        )
    
    def update_by_id(self, id, client, item, operation, store, date, price, info):
        oh = OperationHistory.objects.filter(id=id).first()

        if not oh: return 0

        if client == 0: client = oh.client
        if item == 0: item = oh.item
        if operation == 0: operation = oh.operation
        if store == 0: store = oh.store

        oh.client = Client.objects.filter(id=client).first()
        oh.item = Item.objects.filter(id=item).first()
        oh.operation = Operation.objects.filter(id=operation).first()
        oh.store = Store.objects.filter(id=store).first()
        oh.date = date
        oh.price = price
        oh.info
