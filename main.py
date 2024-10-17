from tkinter import *
from tkinter import ttk
import requests
from city import capitals

def data_get():
    city = city_name.get()
    data = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'API').json()
    w_label_1.config(text = data["weather"][0]['main'])
    wd_label_1.config(text = data['weather'][0]["description"])
    temp_label_1.config(text = str(int(data['main']['temp']-273.15)) )
    pre_label_1.config(text = data['main']['pressure'])
    hum_label_1.config(text = data['main']['humidity'])





win=Tk()
win.title('Weather API')
win.config(bg='pink')
win.geometry('500x650')

name_label = Label(win, text='Weather API Project', 
                   font=('Time New Roman', 20, 'bold'))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()


list_name=[]

for country in capitals:
    list_name.append(capitals[country])
com = ttk.Combobox(win, text='Weather API Project', values=list_name,
                   font=('Time New Roman', 15), textvariable = city_name)
com.place(x=25, y=120, height=50, width=450)






w_label = Label(win, text='Weather Climate', 
                   font=('Time New Roman', 17))
w_label.place(x=25, y=260, height=50, width=215)

w_label_1 = Label(win, text='', 
                   font=('Time New Roman', 17))
w_label_1.place(x=250, y=260, height=50, width=215)

wd_label = Label(win, text='Weather Description', 
                   font=('Time New Roman', 17))
wd_label.place(x=25, y=330, height=50, width=215)

wd_label_1 = Label(win, text='', 
                   font=('Time New Roman', 17))
wd_label_1.place(x=250, y=330, height=50, width=215)

temp_label = Label(win, text='Temperature', 
                   font=('Time New Roman', 17))
temp_label.place(x=25, y=400, height=50, width=215)

temp_label_1 = Label(win, text='', 
                   font=('Time New Roman', 17))
temp_label_1.place(x=250, y=400, height=50, width=215)

pre_label = Label(win, text='Pressure', 
                   font=('Time New Roman', 17))
pre_label.place(x=25, y=470, height=50, width=210)

pre_label_1 = Label(win, text='', 
                   font=('Time New Roman', 17))
pre_label_1.place(x=250, y=470, height=50, width=210)

hum_label = Label(win, text='Humidity', 
                   font=('Time New Roman', 17))
hum_label.place(x=25, y=540, height=50, width=210)

hum_label_1 = Label(win, text='', 
                   font=('Time New Roman', 17))
hum_label_1.place(x=250, y=540, height=50, width=210)


done_button =Button(win, text='DONE', 
                   font=('Time New Roman', 20), command=data_get)
done_button.place(y=190, height=50, width=100, x=200)

win.mainloop() 

