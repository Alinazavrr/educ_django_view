from django.db.models import Q
from django.shortcuts import render

from homes.models import Home, Category


def search_views(request):
    query = request.GET.get('q')
    max = request.GET.get('max')
    min = request.GET.get('min')
    cat_id = request.GET.get('category')
    categories = Category.objects.all()

    if query:
        words = query.split()
        q_objects = Q()
        for word in words:
            q_objects &= (Q(info__iregex=word) | Q(title__iregex=word))
        homes = Home.objects.filter(q_objects)


        #homes = Home.objects.filter(Q(info__iregex=query) | Q(title__iregex=query))
    else:
        homes = Home.objects.all()

    if max:
        homes = homes.filter(cost__lte=max)

    if min:
        homes = homes.filter(cost__gte=min)

    if cat_id:
        homes = homes.filter(category=cat_id)


    return render(request, 'search.html', {'homes': homes, 'categories': categories})


