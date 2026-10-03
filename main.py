from nicegui import ui
import os

# ---------------------------------------------
# CALCULADORA DE INDICE DE MASA CORPORAL (IMC)
# Proyecto: Calculadora_yazz
# Versión compatible con Render - 103 líneas
# ---------------------------------------------

def calculoIMC():
    """
    Función principal para calcular el IMC
    """
    try:
        # 1. Obtener datos del usuario
        # Convertimos los valores a float
        peso_num = float(peso.value)
        altura_num = float(altura.value)

        # 2. Validar datos
        # Verificamos que no sean 0 o negativos
        if peso_num <= 0 or altura_num <= 0:
            resultado.text = "Ingresa valores mayores a 0"
            mensaje.text = ""
            return

        # 3. Calcular IMC
        # Fórmula: peso / (altura * altura)
        imc = peso_num / (altura_num ** 2)

        # Mostramos el resultado con 2 decimales
        resultado.text = f'Tu IMC es: {imc:.2f}'

        # 4. Mostrar mensaje según el IMC
        # Clasificación del IMC
        if imc < 18.5:
            mensaje_texto = "Actualmente estás bajo de peso"
        elif imc < 25:
            mensaje_texto = "Tu peso es normal"
        elif imc < 30:
            mensaje_texto = "Tienes sobrepeso"
        else:
            mensaje_texto = "Tienes obesidad"

        # Asignamos el mensaje final
        mensaje.text = mensaje_texto

    except:
        # En caso de error
        resultado.text = "Ingresa números válidos"
        mensaje.text = ""

def limpiar():
    """
    Función para limpiar los campos
    """
    # Limpiamos los inputs
    peso.value = ''
    altura.value = ''

    # Reiniciamos los textos
    resultado.text = 'Resultado: 0'
    mensaje.text = ''

# ---------------------------------------------
# INTERFAZ GRÁFICA CON NICEGUI
# ---------------------------------------------

# Contenedor principal centrado
with ui.column().classes('w-full h-screen items-center justify-center'):

    # Tarjeta principal
    with ui.card().style('width:400px; background-color:#00233B;').classes('items-center gap-4'):

        # Título
        ui.label('INDICE DE MASA CORPORAL').style('color:white; font-size:22px; font-weight:bold')

        # Icono
        ui.icon('monitor_weight', size='80px').props('color=white')

        # Campos de entrada
        peso = ui.input('Ingresa tu peso en Kg').props('dark outlined').style('width:350px')
        altura = ui.input('Ingresa tu estatura en metros').props('dark outlined').style('width:350px')

        # Fila de botones
        with ui.row().classes('w-full justify-center no-wrap').style('gap:16px'):
            # Botón calcular
            ui.button('Calcular', icon='calculate', color='green', on_click=calculoIMC).style('color:white; width:140px')
            # Botón limpiar
            ui.button('LIMPIAR', icon='delete', color='red', on_click=limpiar).style('color:white; width:140px')

        # Resultados
        resultado = ui.label('Resultado: 0').style('color:white; font-size:20px; font-weight:bold')
        mensaje = ui.label('').style('color:#FFEB3B; font-size:18px')

# ---------------------------------------------
# EJECUCIÓN DEL SERVIDOR
# Necesario para Render
# ---------------------------------------------
ui.run(
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 8080))
)