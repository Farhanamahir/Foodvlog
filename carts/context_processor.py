from .models import *
from .views import *
def count(request):
    item_count=0;
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=cartlists.objects.filter(cart_id=cid(request))
            cti=items.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count+=c.quan
        except cartlists.DoesNotExist:
            item_count=0
        return dict(itc=item_count)
