# main.py                                  # Nombre del archivo
# Inicia la aplicación                     # Descripción del propósito del archivo


# Importamos la interfaz gráfica principal
# VistaUltimate contiene toda la GUI del sistema
from src.vista.vista_ultimate import VistaUltimate


# -----------------------------------------------------------
# Punto de entrada principal del programa
# -----------------------------------------------------------
if __name__ == "__main__":                 # Verifica si se ejecuta este archivo directamente

    app = VistaUltimate()                  # Crea una instancia de la ventana principal (la GUI)

    app.mainloop()                         # Ejecuta el ciclo principal de Tkinter (mantiene la app abierta)
