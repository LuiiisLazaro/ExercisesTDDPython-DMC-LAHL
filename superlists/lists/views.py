from django.shortcuts import redirect, render
from lists.models import Item


# Create your views here.
def home_page(request):
    # if request.method == 'POST': delete
        # Item.objects.create(text=request.POST['item_text']) delete
        #return redirect('/lists/the-only-list-in-the-world/') delete

    # items = Item.objects.all() delete
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')

