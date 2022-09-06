from pharmacycart.models import Drugscart




def cartpros(request):
    carty= Drugscart.objects.filter(user__username = request.user.username, item_paid=False)

    cartcount = 0
    
    for item in carty:
        cartcount += item.quantity
    
    context ={
        'cartcount':cartcount,
    }

    return context