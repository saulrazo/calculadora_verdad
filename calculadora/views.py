from django.shortcuts import render


def index(request): #PÁGINA INICIAL

    data = str(list(request.GET.values()))
    datas = data.replace("[","") 
    datas = datas.replace("]","")
    datas = datas.replace("'","")



 

    context ={'datas':datas}
    return render(request, 'index.html', context)
