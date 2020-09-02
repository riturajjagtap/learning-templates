from django.shortcuts import render

# Create your views here.
def index(req):
    example_dict = {'text': 'some text value', 'num': 10, 'my_date':'2015-11-08'}
    return render(req, 'basicapp/index.html', example_dict)

def otherpage(req):
    return render(req, 'basicapp/other.html')

def relative(req):
    return render(req, 'basicapp/relative_url_templates.html')
