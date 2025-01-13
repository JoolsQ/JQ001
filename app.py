from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Datos de referencia
costos_m2 = {
    "A": 450448,
    "B": 552537,
    "C": 806083,
    "D": 1000000,
    "E": 1300000
}
porcentajes_etapas = {
    "Esquema básico (idea creativa)": 0.25,
    "Anteproyecto (proyecto técnico)": 0.35,
    "Proyecto constructivo": 0.40
}
mpa_values = {
    "15+ años": 5.25,
    "10+ años": 4.00,
    "5+ años": 3.25,
    "4+ años": 2.75,
    "3+ años": 2.25,
    "1+ años": 1.75,
    "Sin experiencia": 1.00
}

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculadora de Honorarios</title>
    </head>
    <body>
        <h1>Calculadora de Honorarios Arquitectónicos</h1>
        <form action="/calcular" method="post">
            <label for="area">Área del proyecto (m²):</label><br>
            <input type="number" id="area" name="area" required><br><br>

            <label for="categoria">Categoría del trabajo:</label><br>
            <select id="categoria" name="categoria" required>
                <option value="A">Categoría A: Construcciones simples</option>
                <option value="B">Categoría B: Construcciones sencillas</option>
                <option value="C">Categoría C: Construcciones complejas</option>
                <option value="D">Categoría D: Construcciones de alta complejidad</option>
                <option value="E">Categoría E: Viviendas unifamiliares</option>
            </select><br><br>

            <label for="etapa">Etapa del proyecto:</label><br>
            <select id="etapa" name="etapa" required>
                <option value="Esquema básico (idea creativa)">Esquema básico (idea creativa)</option>
                <option value="Anteproyecto (proyecto técnico)">Anteproyecto (proyecto técnico)</option>
                <option value="Proyecto constructivo">Proyecto constructivo</option>
            </select><br><br>

            <label for="experiencia">Nivel de experiencia del arquitecto:</label><br>
            <select id="experiencia" name="experiencia" required>
                <option value="15+ años">15+ años</option>
                <option value="10+ años">10+ años</option>
                <option value="5+ años">5+ años</option>
                <option value="4+ años">4+ años</option>
                <option value="3+ años">3+ años</option>
                <option value="1+ años">1+ años</option>
                <option value="Sin experiencia">Sin experiencia</option>
            </select><br><br>

            <button type="submit">Calcular Honorarios</button>
        </form>
    </body>
    </html>
    '''

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        # Capturar datos del formulario
        area = float(request.form['area'])
        categoria = request.form['categoria']
        etapa = request.form['etapa']
        experiencia = request.form['experiencia']

        # Calcular honorarios
        costo_m2 = costos_m2[categoria]
        porcentaje_etapa = porcentajes_etapas[etapa]
        mpa = mpa_values[experiencia]
        honorarios = costo_m2 * area * porcentaje_etapa * mpa

        # Retornar resultados
        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Resultados</title>
        </head>
        <body>
            <h1>Resultados de Honorarios Arquitectónicos</h1>
            <p><strong>Área del proyecto:</strong> {area} m²</p>
            <p><strong>Categoría seleccionada:</strong> {categoria}</p>
            <p><strong>Etapa seleccionada:</strong> {etapa}</p>
            <p><strong>Nivel de experiencia seleccionado:</strong> {experiencia}</p>
            <p><strong>Honorarios estimados:</strong> ${honorarios:,.2f}</p>
            <a href="/">Volver</a>
        </body>
        </html>
        '''
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
