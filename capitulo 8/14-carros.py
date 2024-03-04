def  make_car(company, model, **car_info):
    car = {}
    car['company'] = company 
    car['model'] = model 
    
    for key,value in car_info.items():
     car[key] = value   
    return car

car =  make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)