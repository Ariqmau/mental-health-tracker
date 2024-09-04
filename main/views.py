from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306211622',
        'name': 'Ariq Maulana Malik Ibrahim',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)