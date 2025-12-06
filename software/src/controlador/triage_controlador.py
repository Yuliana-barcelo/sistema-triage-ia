# -----------------------------------------------------------  # Cabecera del archivo que describe su propósito
# triage_controlador.py  # Nombre del archivo controlador principal
# Controlador principal del sistema.  # Breve descripción del módulo
# Su función es conectar la interfaz con el modelo IA.  # Qué hace en una frase
# -----------------------------------------------------------  # Línea separadora para leer mejor

from src.modelo.triage_modelo import TriageModelo  # Importa la clase que carga el modelo IA entrenado

class TriageControlador:  # Define la clase controlador que usará la vista

    def __init__(self):  # Constructor de la clase, se ejecuta al crear una instancia
        """  # Inicio del docstring corto del constructor
        Constructor del controlador.  # Explica la intención del constructor
        Cuando se crea esta clase, automáticamente carga  # Indica efecto colateral: carga el modelo
        el modelo de inteligencia artificial que ya está entrenado.  # Aclara qué se carga
        """  # Fin del docstring

        self.modelo = TriageModelo()  # Crea una instancia de TriageModelo y la guarda en self.modelo

    def clasificar_sintomas(self, texto):  # Método público que la vista llamará para clasificar
        """  # Docstring del método
        Recibe los síntomas en formato texto y devuelve la prioridad  # Qué recibe y qué devuelve
        predicha por el modelo IA.  # Método delegado a la IA
        Parámetros:  # Encabezado de parámetros
            texto (str): Síntomas escritos por el usuario.  # Tipo y descripción del parámetro
        Retorna:  # Encabezado de retorno
            str: Categoría de prioridad → BAJA / MEDIA / CRITICA  # Tipo y posibles valores retornados
        """  # Fin del docstring

        prioridad = self.modelo.predecir(texto)  # Llama a predecir() del modelo y guarda la prioridad resultante

        return prioridad  # Devuelve la prioridad al llamador (normalmente la vista)
