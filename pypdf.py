#Library
import tkinter as Tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PyPDF2 import PdfFileMerger
from pathlib import Path
from datetime import datetime
import os
import sys

#Default Env
data = datetime.today().strftime('%d-%m-%Y')
hora = datetime.today().strftime('%H:%M:%S').replace(':','-')
merger = PdfFileMerger()
salvar = 'C:/data/PymPdfGerados/'

#Create default folder
if Path(r'c:/data/PymPdfGerados').exists():
    pass
else:
    os.mkdir(r'c:/data/PymPdfGerados')

#Functions
def reinicia_programa():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def merge_pdf(arquivos):
    if __name__ == '__main__':
        for arquivo in arquivos:
            merger.append(arquivo)

        with open(f'{salvar}PymPdf-{data}-{hora}.pdf', 'wb') as pdf:
            merger.write(pdf)

        showinfo(
            title='PymPdf',
            message='Arquivo Gerado com Sucesso'
            )
        reinicia_programa()

def selecionar_files():
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All Files', '*.*')
    )
    filenames = fd.askopenfilenames(
        title='Selecione os Arquivos',
        initialdir=salvar,
        filetypes=filetypes)
    if len(filenames) >= 2:
        merge_pdf(filenames)
    else:
        showinfo(
            title='PymPdf',
            message='Selecionar no minimo 2 arquivos'
        )

#GUI interface
root=Tk.Tk()
root.title('PymPdf')
root.resizable(False, False)
largura = 450
altura = 150
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenmmheight()
posix = largura_tela/2 - largura/2
posiy = altura_tela/2 - altura/2
root.geometry('%dx%d+%d+%d' % (largura,altura,posix,posiy))
linha1 = Tk.Label(text='Instruções').pack()
linha2 = Tk.Label(text='Todos os arquivos devem estar na mesma pasta!').pack()
linha3 = Tk.Label(text='Clique em Selecionar arquivos, selecione todos os arquivos e clique em open').pack()
linha4 = Tk.Label(text='Os arquivos serão salvos em c:\data\PymPdfGerados').pack()

selecionar_button = ttk.Button(
    root,
    text="Selecionar Arquivos",
    command=selecionar_files
    )
selecionar_button.pack(side='left', expand=True)

root.mainloop()
