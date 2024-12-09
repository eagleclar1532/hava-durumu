from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# KÜTÜPHANELER


root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="myWeatherApp")

    try: # denemek (comment line : yorum satırı)
        
        location = geolocator.geocode(city)
        if not location: # eğer 
            messagebox.showerror("Hata", "Şehir bulunamadı!")
            return

        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M")
        clock.config(text=current_time)
        name.config(text="Güncel Hava Durumu")

        
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid=5ff9947b31aa393fbada46a47df92406&units=metric&lang=tr"
       
        json_data = requests.get(api).json()
        if 'weather' in json_data and 'main' in json_data['weather'][0]:
            Durum = json_data['weather'][0]['main']
            Tanım = json_data['weather'][0]['description']
            Sıcaklık = json_data['main']['temp']
            BASINÇ = json_data['main']['pressure']
            NEM = json_data['main']['humidity']
            RÜZGAR = json_data['wind']['speed']


            S.config(text=f"{Sıcaklık}°C")
            T.config(text=f"{Durum} | GİBİ HİSSETTİRİYOR {Sıcaklık}°c")
            R.config(text=f"{RÜZGAR} m/s")
            N.config(text=f"{NEM}%")
            B.config(text=f"{BASINÇ} hPa")
        else:
            messagebox.showerror("Hata", "Hava durumu bilgisi alınamadı.")
            print(json_data)

    except Exception as e:
        messagebox.showerror("Hata", f"Ha ocurrido un error. {str(e)}")
        print(e)





1
Search_image = PhotoImage(file="Copy of search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=90, y=40)
textfield.focus()

Search_icon = PhotoImage(file="Copy of search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)






Logo_image = PhotoImage(file="Copy of logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)
Frame_image = PhotoImage(file="Copy of box.png")
Frame_myimage = Label(image=Frame_image)
Frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=40, y=130)

label1 = Label(root, text="RÜZGAR", font=("Helvetica", 15, 'bold'), fg="White", bg="#1ab5fe")
label1.place(x=120, y=400)

label2 = Label(root, text="NEM", font=("Helvetica", 15, 'bold'), fg="White", bg="#1ab5fe")
label2.place(x=280, y=400)

label3 = Label(root, text="AÇIKLAMA", font=("Helvetica", 15, 'bold'), fg="White", bg="#1ab5fe")
label3.place(x=410, y=400)

label4 = Label(root, text="BASINÇ", font=("Helvetica", 15, 'bold'), fg="White", bg="#1ab5fe")
label4.place(x=650, y=400)

S = Label(font=("arial", 70, "bold"), fg="#ee666d")
S.place(x=400, y=150)
D = Label(font=("arial", 15, 'bold'))
D.place(x=400, y=250)

R = Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
R.place(x=120, y=430)
N = Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
N.place(x=280, y=430)
T = Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
T.place(x=350, y=430)
B = Label(text="...", font=("arial", 13, "bold"), bg="#1ab5ef")
B.place(x=670, y=430)




root.mainloop() # KONTAK
