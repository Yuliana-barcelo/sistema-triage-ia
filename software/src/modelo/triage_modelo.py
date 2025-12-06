# -----------------------------------------------------------  # Separador visual del archivo
# triage_modelo.py  # Nombre del archivo
# Carga el modelo de IA desde el archivo .pkl y permite        # Explica qué hace este módulo
# predecir la prioridad a partir de los síntomas.              # Parte 2 de la descripción
# -----------------------------------------------------------  # Separador visual

import os         # Importa 'os' para manejar rutas
import pickle     # Importa pickle para cargar archivos .pkl


class TriageModelo:  # Define la clase que maneja el modelo IA

    def __init__(self):  # Constructor, carga el modelo al crear la clase
        """  # Inicio del docstring
        Constructor de la clase.  # Breve explicación
        Aquí se carga el modelo ya entrenado desde el archivo .pkl.  # Qué hace
        Este archivo se genera usando entrenar.py.  # Relación con el script de entrenamiento
        """  # Fin del docstring

        ruta_modelo = os.path.join("modelos_entrenados", "modelo_trained.pkl")  
        # Construye la ruta completa al archivo .pkl

        with open(ruta_modelo, "rb") as f:  # Abre el archivo .pkl en modo lectura binaria
            self.modelo = pickle.load(f)    # Carga el pipeline (vector + modelo) dentro de self.modelo

        # En este momento self.modelo ya está listo para usar con .predict()  # Aclaración útil


    def predecir(self, texto):  # Método que recibe texto y devuelve prioridad
        """  # Inicio docstring
        Recibe un texto con los síntomas del paciente y devuelve  # Qué hace el método
        la prioridad predicha por el modelo.                      # Continuación
        Parámetros:                                               # Bloque de parámetros
            texto (str): Texto con síntomas                       # Parámetro recibido
        Retorna:                                                  # Bloque de retorno
            str: BAJA / MEDIA / CRITICA                           # Valores posibles
        """  # Fin del docstring

        resultado = self.modelo.predict([texto])[0]  # Llama al modelo, predice y toma el primer resultado

        return resultado  # Devuelve la clasificación final
