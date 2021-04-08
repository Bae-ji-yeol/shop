from django.shortcuts import render
from .forms import GeeksForm


# Create your views here.
def home_view(request):
    context = {}
    form = GeeksForm()
    context['form'] = form
    temp = request.POST.get('geeks_field')
    print(temp)
    if request.method == 'POST':
        form = GeeksForm(request.POST)
        if form.is_valid():
            ch = form.cleaned_data['geeks_field']
            print(ch)
            form.save()

    return render(request, "home.html", context)