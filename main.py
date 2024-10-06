import socket
import customtkinter as ctk

def get_ip_addresses(domain):
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[2]
        return ip_addresses
    except socket.gaierror:
        return ["Domain bulunamadı veya geçersiz."]

def check_dns():
    domain = entry.get() 
    ip_addresses = get_ip_addresses(domain)
    result_label.configure(text=f"{domain} için IP adresleri: {', '.join(ip_addresses)}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk() 
app.title("DNS Sorgulama Aracı")
app.geometry("500x300")
app.resizable(False, False)

label = ctk.CTkLabel(app, text="DNS Sorgulama Aracı", font=("Arial", 20))
label.pack(pady=20)

entry = ctk.CTkEntry(app, width=300, placeholder_text="DNS adresini girin (örneğin: youtube.com)")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="IP Adreslerini Sorgula", command=check_dns)
button.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=20)

app.mainloop()
