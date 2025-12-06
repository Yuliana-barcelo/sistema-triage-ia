# -----------------------------------------------------------  # Separador visual
# entrenar.py                                                # Nombre del archivo
# Entrena el modelo IA con síntomas ampliados y realistas    # Descripción resumida
# -----------------------------------------------------------  # Separador visual

import os                                                    # Importa os para manejo de rutas y creación de carpetas
import pickle                                                # Importa pickle para guardar el modelo en disco
from sklearn.feature_extraction.text import TfidfVectorizer  # Importa TF-IDF para convertir texto a vectores
from sklearn.naive_bayes import MultinomialNB                # Importa Naive Bayes como clasificador simple
from sklearn.pipeline import Pipeline                        # Importa Pipeline para unir pasos de preprocesado y modelo

# -----------------------------------------------------------  # Separador visual de sección
# 1. LISTA DE SÍNTOMAS Y PRIORIDADES REALES                   # Cabecera de datos
# -----------------------------------------------------------  # Separador visual

sintomas = [                                                # Lista de ejemplos de texto (síntomas)
    # =======================================================  # Comentario separador
    # BAJA                                                     # Comentario categoría
    "dolor de cabeza leve",                                   # Síntoma leve → BAJA
    "cefalea leve",                                           # Síntoma leve → BAJA
    "mareo leve",                                             # Síntoma leve → BAJA
    "gripa común",                                            # Síntoma leve → BAJA
    "gripe leve",                                             # Síntoma leve → BAJA
    "resfriado",                                              # Síntoma leve → BAJA
    "tos leve",                                               # Síntoma leve → BAJA
    "congestión nasal",                                       # Síntoma leve → BAJA
    "dolor moderado",                                         # Síntoma moderado → BAJA
    "náuseas leves",                                          # Síntoma leve → BAJA
    "nauseas leves",                                          # Variante sin tilde → BAJA
    "dolor muscular leve",                                    # Síntoma leve → BAJA
    "alergia leve",                                           # Síntoma leve → BAJA
    "picazón en la piel",                                     # Síntoma leve → BAJA
    "estornudos frecuentes",                                  # Síntoma leve → BAJA
    "dolor leve en la espalda",                               # Síntoma leve → BAJA

    # =======================================================  # Separador
    # MEDIA                                                    # Categoría media
    "fiebre alta persistente",                                # Fiebre sostenida → MEDIA
    "temperatura muy alta",                                   # Temperatura elevada → MEDIA
    "vómito persistente",                                     # Vómitos continuos → MEDIA
    "vomito persistente",                                     # Variante sin tilde → MEDIA
    "diarrea fuerte",                                         # Diarrea severa → MEDIA
    "dolor abdominal fuerte",                                 # Dolor abdominal intenso → MEDIA
    "mareo intenso",                                          # Mareo marcado → MEDIA
    "deshidratación moderada",                                # Deshidratación → MEDIA
    "dolor fuerte en el estómago",                            # Dolor estomacal intenso → MEDIA
    "dolor intenso en el cuerpo",                             # Dolor generalizado fuerte → MEDIA
    "debilidad severa",                                       # Debilidad marcada → MEDIA
    "palpitaciones rápidas",                                  # Síntoma cardiovascular → MEDIA

    # =======================================================  # Separador
    # CRÍTICA                                                  # Categoría crítica
    "dificultad para respirar",                               # Dificultad respiratoria → CRÍTICA
    "no puede respirar",                                      # Incapacidad para respirar → CRÍTICA
    "falta de aire severa",                                   # Falta de aire marcada → CRÍTICA
    "dolor fuerte en el pecho",                               # Dolor torácico intenso → CRÍTICA
    "dolor intenso en el pecho",                              # Variante de dolor → CRÍTICA
    "convulsión severa",                                      # Convulsión grave → CRÍTICA
    "pierde la conciencia",                                   # Pérdida de conciencia → CRÍTICA
    "pérdida de conciencia",                                  # Variante con tilde → CRÍTICA
    "desmayo repentino",                                      # Síncope súbito → CRÍTICA
    "hemorragia abundante",                                   # Sangrado abundante → CRÍTICA
    "sangrado fuerte",                                        # Sangrado intenso → CRÍTICA
    "sangrado incontrolable",                                 # Sangrado sin control → CRÍTICA
    "fractura expuesta",                                      # Fractura con hueso expuesto → CRÍTICA
    "parálisis repentina",                                    # Pérdida de función motora → CRÍTICA
    "parálisis en un lado del cuerpo"                         # Síntoma de accidente cerebrovascular → CRÍTICA
]

prioridades = [                                              # Lista paralela de etiquetas (misma longitud que sintomas)
    *["BAJA"] * 16,                                           # Repite "BAJA" 16 veces para la sección BAJA
    *["MEDIA"] * 12,                                          # Repite "MEDIA" 12 veces para la sección MEDIA
    *["CRITICA"] * 15                                         # Repite "CRITICA" 15 veces para la sección CRÍTICA
]

# -----------------------------------------------------------  # Separador visual
# 2. ENTRENAR EL MODELO IA                                    # Cabecera entrenamiento
# -----------------------------------------------------------  # Separador visual

modelo = Pipeline([                                          # Crea pipeline que une vectorizador + clasificador
    ("vector", TfidfVectorizer(ngram_range=(1,2))),          # TF-IDF que considera unigramas y bigramas
    ("clf", MultinomialNB())                                 # Clasificador Naive Bayes multinomial
])

modelo.fit(sintomas, prioridades)                            # Entrena el pipeline con los datos definidos

print("\n✔ Modelo entrenado correctamente con dataset extendido.")  # Mensaje de éxito en consola
print(f"Total de muestras: {len(sintomas)}\n")               # Muestra cuántos ejemplos se usaron

# -----------------------------------------------------------  # Separador visual
# 3. GUARDAR EL MODELO ENTRENADO                              # Cabecera guardado
# -----------------------------------------------------------  # Separador visual

ruta = os.path.join("modelos_entrenados", "modelo_trained.pkl")  # Ruta donde se guardará el archivo .pkl

# Asegurar que existe la carpeta destino
if not os.path.exists("modelos_entrenados"):                   # Si la carpeta no existe
    os.makedirs("modelos_entrenados")                          # la crea para evitar errores al guardar

with open(ruta, "wb") as f:                                    # Abrir archivo en modo escritura binaria
    pickle.dump(modelo, f)                                     # Guardar el pipeline entrenado con pickle

print(f"✔ Modelo guardado en: {ruta}\n")                       # Confirmación del guardado en consola
