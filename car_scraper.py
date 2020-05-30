from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

file_name = input("Enter File Name: ")
start_id = int(input("Which id do you want to start with? : "))
n = int(input("How many id's do you want to scan? : "))

def scrapeCarObj(url,id,n):  # Function to scrape "n" cars starting with id and taking url 
    listofcars=list()
    max = id+n
    for i in range(id,max,1):
        idString = str(i)  # converting i to string to pass as id queryString to url
        iURL = url+idString
        html = urlopen(iURL)
        bsObj = BeautifulSoup(html,"lxml")
        carName = bsObj.find(id="d_carname")
        className = bsObj.find(id="d_classname")
        model = bsObj.find(id="d_modelname")
        color = bsObj.find(id="d_outcolor")
        year = bsObj.find(id="d_year")
        gear = bsObj.find(id="d_gear")
        cyl = bsObj.find(id="d_cylinder")
        drivetrain = bsObj.find(id="d_DriveTrain")
        icolor = bsObj.find(id="d_insidecolor")
        interior = bsObj.find(id="d_insidetype")
        sensors = bsObj.find(id="d_Sensors")
        cam = bsObj.find(id="d_Camera")
        fuel = bsObj.find(id="d_fuel")
        mileage = bsObj.find(id="d_km")
        price = bsObj.find(id="d_price")

        if carName == None:
            pass
        else:
            car = {"Car Name":carName.get_text(), "Class": className.get_text(),"Model": model.get_text(),"Color": color.get_text(), "Year": year.get_text(), "Gear Type ": gear.get_text(), "Cylinders": cyl.get_text(),"Drive Train": drivetrain.get_text(), "Interior Color": icolor.get_text(), "Interior ": interior.get_text(),"Sensors": sensors.get_text(),"Camera": cam.get_text(),"Fuel Type": fuel.get_text(), "Mileage": mileage.get_text(), "Price": price.get_text()}
            listofcars.append(car)
    
    return listofcars

def dict2csv(dictlist):  # Dictionary to CSV File converter method.
    toCSV = dictlist
    with open(file_name+".csv", 'w', encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file,fieldnames=toCSV[0].keys(),)
        fc.writeheader()
        fc.writerows(toCSV)


clist  = scrapeCarObj("https://kuwaitsale.com/KS_e_car.aspx?carid=", start_id,n)

dict2csv(clist)
