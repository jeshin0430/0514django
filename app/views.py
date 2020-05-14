from django.shortcuts import render
import re 


def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(" ", ""))
    count_word = len(re.findall(r"['\w']+", text))

    return render(request, 'result.html',{
        'total_len': total_len,
        'text': text,
        'no_blank_len': no_blank_len,
        'count_word' : count_word
        })