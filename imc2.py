import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.geometry("400x400")
ventana.title("Calculadora de IMC")

etiqueta1 = tk.Label(text="Ingresar altura en m:")
etiqueta1.pack()

eAltura = tk.Entry()
eAltura.pack()


etiqueta2 = tk.Label(text="Ingresar peso en kg:")
etiqueta2.pack()

ePeso = tk.Entry()
ePeso.pack()

def calcularIMC():
    altura = float(eAltura.get())
    peso = int(ePeso.get())
    imc = peso / (altura**2)

    if(imc <18.5):
        mensaje = f"IMC: {imc:.2f}  Bajo peso"
    elif(imc >=18.5 and imc <25):
        mensaje = f"IMC: {imc:.2f}  Peso normal"
    elif(imc >=25 and imc <30):
        mensaje = f"IMC: {imc:.2f}  Sobrepeso"
    else:
        mensaje = f"IMC: {imc:.2f} Obesidad"

    messagebox.showinfo("Calculador IMC", mensaje)

    
    
btnCalcular = tk.Button(text="Calcular IMC", command=calcularIMC)
btnCalcular.pack()

ventana.mainloop()
