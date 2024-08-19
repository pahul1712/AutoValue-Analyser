from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np


model=pickle.load(open('LinearRegressionModel3.pkl','rb'))
car=pd.read_csv('Cleaned_Car_data3.csv')



def index(request):
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()

    companies.insert(0,'Select Company')
    asdf = {'companies':companies, 'car_models':car_models, 'years':year,'fuel_types':fuel_type}
    return render(request,'index.html',asdf)



def predict(request):
    print(request)
    if request.method == 'POST':
        

        company=request.POST.get('company')
        print(company)

        car_model=request.POST.get('car_models')
        year=request.POST.get('year')
        fuel_type=request.POST.get('fuel_type')
        driven=request.POST.get('kilo_driven')

        prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
        
    
    pred2=np.round(prediction[0],2)
    pred3={"pred2":pred2}

    return render(request, 'new.html',pred3)


def about(request):
    return render(request, 'about.html')
