import requests
import tkinter as tk

root = tk.Tk()
root.geometry("400x600") #size of the window by default
root.resizable(0,0) #to make the window size fixed
root.title("Hava Durumu")
city_value = tk.StringVar()

def req():
    api_key = "341277dda1524af9bcb141452241201"

    city_name=city_value.get()

    if city_name == None or city_name == "":
        return
    
    tfield.delete('1.0', tk.END)
    tfield.insert(tk.END,"Lütfen bekleyiniz")

    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city_name}&days=3&aqi=no&alerts=no')

    data = response.json()

    tfield.delete('1.0', tk.END)

    try:
        txt = data["location"]["country"] + " - " + data["location"]["name"] + "\n---------------\n"
        txt = txt + "Bugünün hava durumu:\n"+str(data["current"]["temp_c"]) +" derece - Rüzgar hızı (mph): " + str(data["current"]["wind_mph"]) + "\n---------------\n"
        txt = txt + "Tahminler" + "\n---------------\n"

        for forecast in data["forecast"]["forecastday"]:
            txt = txt + "Tarih: " + forecast["date"] + "\n"
            txt = txt + "Maksimum derece: " + str(forecast["day"]["maxtemp_c"])+ "\n"
            txt = txt + "Minimum derece: " + str(forecast["day"]["mintemp_c"])+ "\n"
            txt = txt + "Ortalama derece: " + str(forecast["day"]["avgtemp_c"])+ "\n---------------\n"

        tfield.insert(tk.END,txt)
    except:
        tfield.insert(tk.END,"Bir hata oluştu. Lütfen şehir ismini kontrol ediniz!")


city_head= tk.Label(root, text = 'Şehir Adı Gir', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = tk.Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
tk.Button(root, command = req, text = "Kontrol Et", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = tk.Label(root, text = "Hava durumu:", font = 'arial 12').pack(pady=10)
 
tfield = tk.Text(root, width=46, height=22)

tfield.pack()

root.mainloop()