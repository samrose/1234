from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories' : category_list} 
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    return HttpResponse("Rango says here is the about page<br /> <a href='/rango/'>Index</a>")
def show_category(request,category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context_dict)
def add_category(request):
    form = CategoryForm()

    #HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        #have we been provided with a valid form?
        if form.is_valid():
            #Save the new category to the database
            form.save(commit=True)
            #Now we return to index page since the categoy
            #was entered there
            return index(request)
        else:
            #the supplied form contained errors 
            #so we print them 
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})

