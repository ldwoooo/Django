from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, 'calculators/cal_base.html')


def index(request, number, number2):

    if number2 == 0:
        divide = 0
    else:
        divide = number / number2

    context = {
        'number1' : number,
        'number2' : number2,
        'plus' : number + number2,
        'minus' : number - number2,
        'multiply' : number * number2,
        'divide' : divide
        
    }
        

    return render(request, 'calculators/cal.html', context)