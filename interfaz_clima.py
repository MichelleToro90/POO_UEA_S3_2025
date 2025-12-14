# gui.py

import tkinter as tk
from tkinter import messagebox
from clima import ClimaDiario, ClimaSemanal

class AplicacionClima:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Clima Semanal")
        self.semana = ClimaSemanal()

        # Entradas
        tk.Label(root, text="Temperatura (°C)").grid(row=0, column=0)
        tk.Label(root, text="Humedad (%)").grid(row=0, column=1)
        tk.Label(root, text="Precipitación (mm)").grid(row=0, column=2)

        self.entrada_temp = tk.Entry(root, width=10)
        self.entrada_hum = tk.Entry(root, width=10)
        self.entrada_prec = tk.Entry(root, width=10)

        self.entrada_temp.grid(row=1, column=0)
        self.entrada_hum.grid(row=1, column=1)
        self.entrada_prec.grid(row=1, column=2)

        # Botones
        tk.Button(root, text="Agregar Día", command=self.agregar_dia).grid(row=1, column=3, padx=5)
        tk.Button(root, text="Calcular Promedio", command=self.mostrar_promedio).grid(row=1, column=4, padx=5)

        # Tabla de días
        self.tabla_frame = tk.Frame(root)
        self.tabla_frame.grid(row=2, column=0, columnspan=5, pady=10)

        self.headers = ["Día", "Temperatura (°C)", "Humedad (%)", "Precipitación (mm)"]
        for col, header in enumerate(self.headers):
            tk.Label(self.tabla_frame, text=header, relief="ridge", width=20).grid(row=0, column=col)

        self.filas_tabla = []

        # Área de promedios
        self.resultado_promedio = tk.Text(root, height=5, width=80)
        self.resultado_promedio.grid(row=3, column=0, columnspan=5, pady=10)

    def agregar_dia(self):
        try:
            temp_str = self.entrada_temp.get().strip().replace(',', '.')
            hum_str = self.entrada_hum.get().strip().replace(',', '.')
            prec_str = self.entrada_prec.get().strip().replace(',', '.')

            # Validar que no estén vacíos
            if not temp_str or not hum_str or not prec_str:
                raise ValueError("Campos vacíos")

            temp = float(temp_str)
            hum = float(hum_str)
            prec = float(prec_str)

            dia = ClimaDiario(temp, hum, prec)
            self.semana.agregar_dia(dia)
            self.actualizar_tabla()

            self.entrada_temp.delete(0, tk.END)
            self.entrada_hum.delete(0, tk.END)
            self.entrada_prec.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos (pueden usar punto o coma decimal)")

    def actualizar_tabla(self):
        for fila in self.filas_tabla:
            for widget in fila:
                widget.destroy()
        self.filas_tabla.clear()

        for i, temp, hum, prec in self.semana.lista_dias():
            fila_widgets = []
            for col, val in enumerate([i, temp, hum, prec]):
                lbl = tk.Label(self.tabla_frame, text=val, relief="ridge", width=20)
                lbl.grid(row=i, column=col)
                fila_widgets.append(lbl)
            self.filas_tabla.append(fila_widgets)

    def mostrar_promedio(self):
        self.resultado_promedio.delete(1.0, tk.END)
        promedios = self.semana.promedio_semanal()
        if promedios:
            self.resultado_promedio.insert(tk.END, "Promedio semanal:\n")
            self.resultado_promedio.insert(tk.END, f"Temperatura promedio: {promedios['Temperatura']:.2f}°C\n")
            self.resultado_promedio.insert(tk.END, f"Humedad promedio: {promedios['Humedad']:.2f}%\n")
            self.resultado_promedio.insert(tk.END, f"Precipitación promedio: {promedios['Precipitación']:.2f}mm\n")
        else:
            self.resultado_promedio.insert(tk.END, "No hay datos para calcular promedio.\n")
