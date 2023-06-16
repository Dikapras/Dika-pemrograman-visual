import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import showinfo

#Inisialisasi
window = tkinter.Tk()
window.configure(bg="sky blue")
icon_img = PhotoImage(file='D:\Dika_Pemrog Visual\Aset\plant.png')
window.iconphoto(False, icon_img)
window.geometry("500x500")
window.resizable(False,False)
window.title("Daftar Lomba IPA")

#Header
header_label = ttk.Label(window, text="Pengisian Formulir", font=(16), background="yellow", foreground="white")
header_label.pack(pady=20)

#Variable dan Function
NAMA_LENGKAP = tkinter.StringVar()
ALAMAT = tkinter.StringVar()
KELAS = tkinter.StringVar()
SEKOLAH = tkinter.StringVar()
EMAIL = tkinter.StringVar()
#Fungsi Tombol
def tombol_click():
 if not NAMA_LENGKAP.get() or not ALAMAT.get() or not KELAS.get() or not SEKOLAH.get() or not EMAIL.get():     
        showinfo(title="Eror!", message="Mohon lengkapi semua form!")
 else:
    pesan = f"Hallo {NAMA_LENGKAP.get()}, Kamu sudah terdaftar!"
    showinfo(title="Selamat",message=pesan)


#Frame input
style = ttk.Style()
style.configure("Custom.TEntry",fiedbackground="#257cff")
input_frame = ttk.Frame(window)

#penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x", expand=True)

#Komponen nama lengkap
nama_depan_label = ttk.Label(input_frame, text="Nama Lengkap:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_LENGKAP,style="Custom.TEntry")
nama_depan_entry.pack(padx=10,fill="x",expand=True)

#Komponen alamat
alamat_label = ttk.Label(input_frame, text="Alamat :")
alamat_label.pack(padx=10,fill="x",expand=True)
alamat_entry = ttk.Entry(input_frame,textvariable=ALAMAT,style="Custom.TEntry")
alamat_entry.pack(padx=10,fill="x",expand=True)

#Komponen kelas
kelas_label = ttk.Label(input_frame, text="Kelas:")
kelas_label.pack(padx=10,fill="x",expand=True)
kelas_entry = ttk.Entry(input_frame,textvariable=KELAS,style="Custom.TEntry")
kelas_entry.pack(padx=10,fill="x",expand=True)
#Komponen sekolah

sekolah_label = ttk.Label(input_frame, text="Sekolah:")
sekolah_label.pack(padx=10,fill="x",expand=True)
sekolah_entry = ttk.Entry(input_frame,textvariable=SEKOLAH,style="Custom.TEntry")
sekolah_entry.pack(padx=10,fill="x",expand=True)

#Komponen email
email_label = ttk.Label(input_frame, text="Email:")
email_label.pack(padx=10,fill="x",expand=True)
email_entry = ttk.Entry(input_frame,textvariable=EMAIL,style="Custom.TEntry")
email_entry.pack(padx=10,fill="x",expand=True)

#Tombol
tombol_daftar = ttk.Button(input_frame, text="Daftar",command=tombol_click)
tombol_daftar.pack(fill="x",expand=True, padx=10,pady=10)


window.mainloop()