from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    print(djtext)
    analyzed = ""
    if removepunc == "on":
        punctuations = '''!()-[]{};:`'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (fullcap == "on"):
        for char in djtext:
            if char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(newlineremover == "on"):
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New line Remover', 'analyzed_text1': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
