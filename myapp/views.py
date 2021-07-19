from django.shortcuts import render,HttpResponse
import requests
# Create your views here.
def home(request):
    data=[]
    showit=False
    if request.method=="POST":
        country=request.POST.get('Country',False)
        #country="Pakistan"
        print(country)
        url='https://api.covid19api.com/summary'
        c=requests.get(url).json()
        # print(c)
        
        labels=[]
        labels.append('TotalConfirmed')
        labels.append('NewConfirmed')
        labels.append('value')
        labels.append('NewDeaths')
        labels.append('TotalDeaths')
        labels.append('NewRecovered')
        labels.append('TotalRecovered')
        for x in c['Countries']:
            # print(x['Country'])
            if x['Country'] == country:
                data.append(x['TotalConfirmed'])
                data.append(x['NewConfirmed'])
                data.append(x['NewDeaths'])
                data.append(x['TotalDeaths'])
                data.append(x['NewRecovered'])
                data.append(x['TotalRecovered'])
    
        #data.append('1000000')
        # 
        print(data)
        return render(request,'Datashow.html',{'data':data,'labels':labels})
    else:
        return render(request,'home.html',{'data':data})
    