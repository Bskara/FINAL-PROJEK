from tkinter import *
from pathlib import Path
def Create():
    namafile = isi_lbl.get() + ".txt"
    text = isi_teks.get("1.0", END)
    with open(namafile,'w') as f:
        f.write(text)
    isi_teks.delete('1.0', END)
    Read()

def Append():
    namafile = isi_lbl.get() + ".txt"
    text = isi_teks.get("1.0", END)
    with open(namafile,'a') as f:
        f.write(text)
    isi_teks.delete('1.0', END)
    Read()

def Read():
    isi_tampil.delete('1.0', END)
    namafile = isi_lbl.get() + ".txt"
    with open(namafile, 'r') as f:
        text = f.read()
    isi_tampil.insert("1.0", text)

def Update():
    namafile = isi_lbl.get() + ".txt"
    searchtxt = isi_search.get()
    updt = isi_updt.get()
    with open(namafile, mode='r') as f:
        data = f.read()
        data = data.replace(searchtxt, updt)
    with open(namafile, mode='w') as f:
        f.write(data)
    isi_search.delete('0', END)
    isi_updt.delete('0', END)
    Read()

def Delete():
    namafile = isi_lbl.get() + ".txt"
    file_path = Path(namafile)
    file_path.unlink()
    isi_del.delete('0', END)
    isi_tampil.delete('1.0', END)
    isi_lbl.delete('0', END)
    

root = Tk()
root.geometry('1000x450')
root.title('FINAL PROJECT')
nama_fl = StringVar()
search_isi = StringVar()
update_isi = StringVar()
delete_isi = StringVar()
tampilan = StringVar()
teks_isian = StringVar()
lbl_file = Label(root, text='Nama file:', font= ('Times New Roman', 10, 'normal'), justify=LEFT, anchor='w')
isi_lbl = Entry(root, textvariable=nama_fl, font=("Times New Roman", 10, 'normal'))
lbl_teks = Label(root, text='Teks: ', font= ('Times New Roman', 10, 'normal'), justify=LEFT)
isi_teks = Text(root, height=10, width=60, font=('Times New Roman', 10, 'normal'))
create_butt=Button(root,text='Create', command=lambda: Create())
append_butt=Button(root,text='Append', command=lambda: Append())
lbl_search = Label(root, text='Search text: ', font= ('Times New Roman', 10, 'normal'))
lbl_updt = Label(root, text='Update text: ', font= ('Times New Roman', 10, 'normal'))
isi_search = Entry(root, textvariable=search_isi, font=("Times New Roman", 10, 'normal'))
isi_updt = Entry(root, textvariable=update_isi, font=("Times New Roman", 10, 'normal'))
update_butt = Button(root, text='Update', command=lambda: Update())
del_file = Label(root, text='File: ', font= ('Times New Roman', 10, 'normal'))
isi_del = Entry(root, textvariable=delete_isi, font=("Times New Roman", 10, 'normal'))
del_butt = Button(root, text='Delete', command=lambda: Delete())
lbl_tampil = Label(root, text='Tampil: ', font= ('Times New Roman', 10, 'normal'))
isi_tampil = Text(root, height=10, width=60, font=('Times New Roman', 10, 'normal'))
tampil_butt = Button(root, text='Read',command=lambda: Read())

lbl_file.place(x=10, y=10)
isi_lbl.place(x=85,y=10)
lbl_teks.place(x=10, y=40)
isi_teks.place(x=10, y=65)
lbl_search.place(x=10, y=225)
isi_search.place(x=10,y=250)
lbl_updt.place(x=165, y=225)
isi_updt.place(x=165, y=250)
update_butt.place(x=310,y=245)
del_file.place(x=10,y=275)
isi_del.place(x=10,y=300)
del_butt.place(x=150, y=296)
create_butt.place(x=400, y=65)
append_butt.place(x=400, y=103)
lbl_tampil.place(x=480,y=40)
isi_tampil.place(x=480,y=65)
tampil_butt.place(x=850,y=65)

root.mainloop()
