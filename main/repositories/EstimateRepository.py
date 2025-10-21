from main.repositories.IRepository import IRepository
from main.models import Estimate

class EstimateRepository(IRepository):
    def get_all(self):
        return Estimate.objects.all()
    
    def get_by_id(self, id):
        return Estimate.objects.filter(id=id).first()

    def delete_all(self):
        return Estimate.objects.all().delete()

    def delete_by_id(self, id):
        return Estimate.objects.filter(id=id).delete()

    def add_one(self, item, worker, reasoning, date):
        return Estimate.objects.create(
            item=item,
            worker=worker,
            reasoning=reasoning,
            date=date
        )
    
    def update_by_id(self, id, item, worker, reasoning, date):
        e = Estimate.objects.all().filter(id=id).first()

        if not e: return 0

        if item==0: item = e.item
        if worker==0: worker = e.worker

        e.item = item
        e.worker = worker
        e.reasoning = reasoning
        e.date = date

        e.save()
        return 1