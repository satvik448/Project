from tkinter import *
from tkinter import ttk
import requests

def get_data():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=119a50f31254070a2d0c62dd343c23ac").json()
    a_label.config(text=data['weather'][0]['main'])
    b_label.config(text=data['weather'][0]['description'])
    c_label.config(text=str(int(data['main']['temp'])-273)+"°C")
    d_label.config(text=str(data['main']['pressure'])+" hPa")





win=Tk()

win.title("My First Python Project")
win.config(bg="teal")
win.geometry("500x520")

name_label=Label(win, text="Wether Fetcher", font=("Arial", 30, "bold"))
name_label.place(x=80,y=50,height=50,width=320)
list_name=["New Delhi", "Mumbai", "Chennai", "Kolkata", "Bangalore"]
city_name=StringVar()
com=ttk.Combobox(win, text="Select City", font=("Arial", 20, "bold"), values=list_name, textvariable=city_name)
com.place(x=80,y=130,height=40,width=320)

done_button=Button(win, text="Get Data", font=("Arial", 20, "bold"), command=get_data)
done_button.place(x=150,y=190,height=40,width=200)

w_label=Label(win, text="Wether Climate:", font=("Arial", 17))
w_label.place(x=25,y=250,height=40,width=210)

t_label=Label(win, text="Wether Description:", font=("Arial", 17))
t_label.place(x=25,y=320,height=40,width=210)

te_label=Label(win, text="Temperature:", font=("Arial", 17))
te_label.place(x=25,y=390,height=40,width=210)

p_label=Label(win, text="Pressure:", font=("Arial", 17))
p_label.place(x=25,y=460,height=40,width=210)

a_label=Label(win, text="", font=("Arial", 17))
a_label.place(x=260,y=250,height=40,width=210)

b_label=Label(win, text="", font=("Arial", 17))
b_label.place(x=260,y=320,height=40,width=210)

c_label=Label(win, text="", font=("Arial", 17))
c_label.place(x=260,y=390,height=40,width=210)

d_label=Label(win, text="", font=("Arial", 17))
d_label.place(x=260,y=460,height=40,width=210)





win.mainloop()

