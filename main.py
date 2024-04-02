import tkinter as tk
from tkinter import messagebox
import ntplib
from time import ctime

def sync_time(server="127.0.0.1"):  # Altere este endereço IP para o do seu servidor NTP local
    try:
        client = ntplib.NTPClient()
        response = client.request(server)
        ntp_time = response.tx_time
        from datetime import datetime
        import os
        os.system(f"date -s @{ntp_time}")

        messagebox.showinfo("Sincronização Concluída", f"A hora foi sincronizada com sucesso com {server}.\nNova hora do sistema: {ctime(ntp_time)}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao sincronizar a hora: {e}")

def sync_time_with_interface():
    def sync():
        server = server_entry.get()
        sync_time(server)

    root = tk.Tk()
    root.title("Sincronizar Hora")

    server_label = tk.Label(root, text="Endereço IP do Servidor NTP:")
    server_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    server_entry = tk.Entry(root)
    server_entry.grid(row=0, column=1, padx=10, pady=5)

    sync_button = tk.Button(root, text="Sincronizar", command=sync)
    sync_button.grid(row=1, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    sync_time_with_interface()
