# -----------------------------------------------------------  # Encabezado decorativo
# vista_ultimate.py                                            # Nombre del archivo
# Interfaz gráfica del sistema de triage médico                # Descripción corta
# con CustomTkinter, botón BORRAR y diseño claro.              # Nota importante
# -----------------------------------------------------------  # Cierre superior

import customtkinter as ctk                             # Importa librería GUI moderna
from src.controlador.triage_controlador import TriageControlador   # Controlador IA


class VistaUltimate(ctk.CTk):                           # Clase principal que hereda ventana CTk

    def __init__(self):                                 # Constructor de la interfaz
        super().__init__()                              # Inicializa la ventana base CTk

        self.title("Sistema de Triage Médico")           # Título superior
        self.geometry("600x520")                        # Tamaño fijo
        self.resizable(False, False)                    # Bloquea cambios de tamaño

        ctk.set_appearance_mode("light")                # Modo claro
        ctk.set_default_color_theme("blue")             # Tema azul/turquesa

        self.controlador = TriageControlador()          # Instancia del controlador IA

        self._crear_componentes()                       # Construye todos los widgets


    def _crear_componentes(self):                       # Método que crea la interfaz

        self.lbl_titulo = ctk.CTkLabel(                 # Label del título grande
            self,
            text="Sistema de Triage Médico",
            font=("Arial", 26, "bold"),
            text_color="#006b76"                        # Turquesa oscuro elegante
        )
        self.lbl_titulo.pack(pady=15)                   # Espaciado vertical

        self.lbl_sub = ctk.CTkLabel(                    # Subtítulo de instrucciones
            self,
            text="Escriba los síntomas del paciente:",
            font=("Arial", 16)
        )
        self.lbl_sub.pack(pady=10)                      # Espacio inferior

        self.txt_sintomas = ctk.CTkTextbox(             # Área para escribir síntomas
            self,
            width=480,
            height=150,
            corner_radius=10,
            border_width=1,
            border_color="#00b0b5"                      # Borde turquesa
        )
        self.txt_sintomas.pack()                        # Muestra el widget

        self.btn_clasificar = ctk.CTkButton(            # Botón principal para clasificar
            self,
            text="Clasificar Prioridad",
            font=("Arial", 15, "bold"),
            height=45,
            width=200,
            corner_radius=8,
            fg_color="#0097a7",                         # Turquesa intenso
            command=self.clasificar                     # Acción al presionar
        )
        self.btn_clasificar.pack(pady=10)               # Espaciado del botón

        self.btn_borrar = ctk.CTkButton(                # Botón de limpieza
            self,
            text="Borrar",
            font=("Arial", 14),
            width=120,
            height=35,
            fg_color="#00a8b5",
            text_color="white",
            command=self.borrar_texto                    # Llama función para limpiar
        )
        self.btn_borrar.pack(pady=5)                    # Espaciado pequeño

        self.frame_resultado = ctk.CTkFrame(            # Marco contenedor del resultado
            self,
            width=500,
            height=120,
            corner_radius=12
        )
        self.frame_resultado.pack(pady=10)              # Espacio alrededor del marco

        self.lbl_resultado = ctk.CTkLabel(              # Texto donde aparece el resultado
            self.frame_resultado,
            text="Resultado: ---",
            font=("Arial", 18, "bold"),
            text_color="#004d4d"                        # Turquesa oscuro
        )
        self.lbl_resultado.pack(pady=25)                # Espaciado interno


    def borrar_texto(self):                             # Función del botón BORRAR
        """Limpia el cuadro y resetea el resultado."""  # Comentario descriptivo
        self.txt_sintomas.delete("1.0", "end")          # Limpia todo el texto
        self.lbl_resultado.configure(                   # Restaura mensaje del resultado
            text="Resultado: ---",
            text_color="#004d4d"
        )


    def clasificar(self):                               # Función del botón CLASIFICAR

        sintomas = self.txt_sintomas.get("1.0", "end").strip()  # Toma lo escrito en el cuadro

        if sintomas == "":                              # Si está vacío:
            self.lbl_resultado.configure(
                text="⚠ Debe ingresar síntomas.",
                text_color="red"
            )
            return                                       # Sale de la función

        prioridad = self.controlador.clasificar_sintomas(sintomas)  # IA determina prioridad

        colores = {                                     # Diccionario de colores por prioridad
            "CRITICA": "red",                           # Crítica → rojo
            "MEDIA": "#cc7700",                         # Media → naranja
            "BAJA": "green"                             # Baja → verde
        }

        self.lbl_resultado.configure(                   # Actualiza el texto final
            text=f"Prioridad: {prioridad}",
            text_color=colores.get(prioridad, "gray")   # Si no está → gris
        )
