#Importing Tkinter Modeule
from tkinter import *
from tkinter import ttk
import requests



#Creating a Module to use API
#Defining Function to get the data
def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                    +city+"&appid=f96f2a631ab6616aaf72a946486374d7").json()
    climate_label1.config(text=data["weather"][0]["main"])
    description_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))                     #to change temperature from kelvin to degree centigrade        
    tempfeel_label1.config(text=str(int(data["main"]["feels_like"]-273.15)))
    pressure_label1.config(text=data["main"]["pressure"])
    humidity_label1.config(text=data["main"]["humidity"])
    


#Creating a window for our Weather app (Graphical User Interface)
win = Tk()

#Adding title
win.title("O Level Project")
#Adding BG colour
win.config(bg = "navy")
#Reshaping the Window
win.geometry("600x670")



#Creating the User Interface

#Adding Title for our Weather app
title = Label(win, text="☀   ⇢ Weather App ⇠    ☃",
              font=("Bahnschrift",30,"bold"))
title.place(x=50, y=50, height=60, width=500)

#Creating List of all Indian States and it's Capitals
city_name = StringVar()
list_name = [
    "Hyderabad,Andhra Pradesh","Itanagar,Arunachal Pradesh",
    "Dispur,Assam","Patna,Bihar","Raipur,Chhattisgarh",
    "Panaji,Goa","Gandhinagar,Gujarat","Chandigarh,Haryana",
    "Shimla,Himachal Pradesh","Ranchi,Jharkhand","Bengaluru,Karnataka",
    "Thiruvananthapuram,Kerala","Bhopal,Madhya Pradesh",
    "Mumbai,Maharashtra","Imphal,Manipur","Shillong,Meghalaya",
    "Aizawl,Mizoram","Kohima,Nagaland","Bhubaneswar,Odisha",
    "Chandigarh,Punjab","Jaipur,Rajasthan","Gangtok,Sikkim",
    "Chennai,Tamil Nadu","Hyderabad,Telangana","Agartala,Tripura",
    "Lucknow,Uttar Pradesh","Dehradun,Uttarakhand","Kolkata,West Bengal"
    ]
#Creating Combobox
com = ttk.Combobox(win,
                   values=list_name,
                   font=("Bahnschrift SemiCondensed",30),textvariable=city_name)
com.place(x=50, y=130, height=60, width=500)



#Adding Information About Weather

#Creating Weather Climate Box
climate_label = Label(win, text="Current Weather :",
              font=("Bahnschrift",20,"bold"))
climate_label.place(x=50, y=300, height=40, width=300)

climate_label1 = Label(win, text="",
              font=("Bahnschrift",20,"bold"))
climate_label1.place(x=380, y=300, height=40, width=170)



#Creating Weather Description Box
description_label = Label(win, text="Weather Description :",
              font=("Bahnschrift",20,"bold"))
description_label.place(x=50, y=360, height=40, width=300)

description_label1 = Label(win, text="",
              font=("Bahnschrift",18,"bold"))
description_label1.place(x=380, y=360, height=40, width=170)



#Creating Temperature Box
temp_label = Label(win, text="Temperature in °C :",
              font=("Bahnschrift",20,"bold"))
temp_label.place(x=50, y=420, height=40, width=300)

temp_label1 = Label(win,
              font=("Bahnschrift",20,"bold"))
temp_label1.place(x=380, y=420, height=40, width=170)



#Creating Feel Like Temperature Box
tempfeel_label = Label(win, text="Temp Feels Like :",
              font=("Bahnschrift",20,"bold"))
tempfeel_label.place(x=50, y=480, height=40, width=300)

tempfeel_label1 = Label(win, text="",
              font=("Bahnschrift",20,"bold"))
tempfeel_label1.place(x=380, y=480, height=40, width=170)



#Creating Pressure Box
pressure_label = Label(win, text="Pressure in hPa :",
              font=("Bahnschrift",20,"bold"))
pressure_label.place(x=50, y=540, height=40, width=300)

pressure_label1 = Label(win, text="",
              font=("Bahnschrift",20,"bold"))
pressure_label1.place(x=380, y=540, height=40, width=170)



#Creating Humidity Box
humidity_label = Label(win, text="Humidity in % :",
              font=("Bahnschrift",20,"bold"))
humidity_label.place(x=50, y=600, height=40, width=300) 

humidity_label1 = Label(win, text="",
              font=("Bahnschrift",20,"bold"))
humidity_label1.place(x=380, y=600, height=40, width=170) 


#Creating Button
done_button = Button(win, text="Done",
                     font=("Time New Roman",20,"bold"), command=data_get)
done_button.place(x=250, y=210, height=50, width=100)




win.mainloop()
