

from django.shortcuts import render, redirect

from application.forms import ApplicationForm
from homes.models import Home


def list_views(request):
    homes = Home.objects.all()
    return render(request, 'index.html', {'homes': homes})


def detail_view(request, pk):
    home = Home.objects.get(id=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homes:main_page')
    else:
        form = ApplicationForm()

    return render(request, 'detail.html', {'home': home, 'form': form})




