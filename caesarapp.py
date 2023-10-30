#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class CaesarApp:
    def __init__(self, master=None):
        # build ui
        toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        toplevel1.configure(
            height=200, pady=10, width=200)
        toplevel1.geometry("640x480")
        toplevel1.title("Caesar Ciphertext")

        def encode():
            p = entry2.get()
            chipertext = ''
            for karakter in p:
                cbaru = chr((ord(karakter)) % 256)
                chipertext += cbaru
            label2.configure(text='HASIL : ' + chipertext)

        label5 = ttk.Label(toplevel1)
        label5.configure(
            background="#f5f5f5",
            font="{Bookman Old Style} 12 {bold}",

            text='PLAINTEXT/CIPHERTEXT :')
        label5.grid(column=0, row=0, sticky="nw")
        entry2 = ttk.Entry(toplevel1)
        entry2.configure(width=105)
        entry2.grid(column=0, pady=10, row=1, sticky="w")

        label1 = ttk.Label(toplevel1)
        label1.configure(
            background="#f5f5f5",
            font="{Bookman Old Style} 12 {bold}",
            text='JUMLAH PERGESERAN :',
        )
        label1.grid(column=0, pady=10, row=2, sticky="w")

        button1 = ttk.Button(toplevel1)
        button1.configure(
            takefocus=False, text='ENCODE CAESAR CIPHER', command=encode)
        button1.grid(column=0, ipadx=50, padx=30, pady=10, row=5, sticky="w")
        button2 = ttk.Button(toplevel1)
        button2.configure(text='DECODE CAESAR CIPHER')
        button2.grid(column=0, ipadx=50, padx=350, pady=10, row=5, sticky="w")
        label2 = ttk.Label(toplevel1)
        label2.configure(
            background="#f5f5f5",
            font="{Bookman Old Style} 12 {bold}",

            text="HASIL :",
        )
        label2.grid(column=0, pady=10, row=6, sticky="w")

        entry1 = ttk.Entry(toplevel1)
        entry1.configure(width=105)
        entry1.grid(column=0, pady=10, row=4, sticky="w")

        # Main widget
        self.mainwindow = toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = CaesarApp()
    app.run()
