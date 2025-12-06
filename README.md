# Sistema de Triage Médico con Inteligencia Artificial

Este proyecto es una aplicación de escritorio que clasifica síntomas médicos en tres niveles de prioridad:

- BAJA  
- MEDIA  
- CRÍTICA  

El sistema usa un modelo de Inteligencia Artificial entrenado con lenguaje natural y una interfaz moderna creada con CustomTkinter.

## Estructura del proyecto

software/
│
├── entrenar.py
├── main.py
│
├── modelos_entrenados/
│     └── modelo_trained.pkl
│
└── src/
      ├── controlador/
      │       └── triage_controlador.py
      ├── modelo/
      │       └── triage_modelo.py
      └── vista/
              └── vista_ultimate.py

## Instalación

1. Instalar dependencias:

pip install -r requirements.txt

markdown
Copiar código

2. Entrenar el modelo:

python -m entrenar

markdown
Copiar código

3. Ejecutar la aplicación:

python -m src.main

markdown
Copiar código

## ¿Cómo funciona?

- Usa TfidfVectorizer para convertir texto en números.
- Usa Multinomial Naive Bayes para clasificar el texto.
- Usa Pickle para guardar y cargar el modelo entrenado.
- La interfaz permite escribir síntomas, clasificarlos y borrar el texto.

## Tecnologías usadas
- Python 3
- CustomTkinter
- Scikit-Learn
- Numpy

## Autor
Yuliana Barceló
