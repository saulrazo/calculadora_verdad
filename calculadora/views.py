from django.shortcuts import render


def index(request): #PÁGINA INICIAL

    # data = str(list(request.GET.values()))
    # datas = data.replace("[","") 
    # datas = datas.replace("]","")
    # datas = datas.replace("'","")

    dat = {"p":["F","F","F","F"],"A":["F","F","F","F"],"B":["F","F","F","F"],"C":["F","F","F","F"],}
    fin_lst = []

    for prop, lst in dat.items():
         sec_lst = []
         sec_lst.append(prop)
         for char in lst:
            sec_lst.append(char)

         fin_lst.append(sec_lst)


    context ={'lsts':fin_lst}
    return render(request, 'index.html', context)
  
