from flask import Flask, jsonify

# Creación de la aplicación Flask
app = Flask(__name__)

# Definición de la ruta (/clientes) con un método GET
@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    # Creamos una lista con los datos de varios usuarios
    clientes = [
        {
            "id_cliente": "CLI-2026-894021",
            "informacion_personal": {
                "nombre": "Ana",
                "apellido": "Gómez",
                "fecha_nacimiento": "1992-04-12",
                "pais_residencia": "ES"
            },
            "segmentacion": {
                "tipo_cliente": "Particular", 
                "nivel_ingresos_anual": 45000.00,
                "score_crediticio_interno": 740,
                "puntuacion_riesgo_pld": 0.18
            },
            "estado_cuenta": {
                "activo": True,
                "fecha_alta": "2021-10-15T08:30:00Z",
                "ultima_actividad": "2026-06-15T10:15:24Z"
            },
            "productos_activos": {
                "cuentas_corrientes": 1,
                "tarjetas_credito": 2,
                "prestamos_vigentes": 0,
                "inversiones": True
            }
        },
        {
            "id_cliente": "CLI-2026-123456",
            "informacion_personal": {
                "nombre": "Carlos",
                "apellido": "Ruiz",
                "fecha_nacimiento": "1985-07-22",
                "pais_residencia": "MX"
            },
            "segmentacion": {
                "tipo_cliente": "Empresa", 
                "nivel_ingresos_anual": 120000.00,
                "score_crediticio_interno": 810,
                "puntuacion_riesgo_pld": 0.05
            },
            "estado_cuenta": {
                "activo": True,
                "fecha_alta": "2019-03-10T11:00:00Z",
                "ultima_actividad": "2026-05-20T15:45:00Z"
            },
            "productos_activos": {
                "cuentas_corrientes": 2,
                "tarjetas_credito": 1,
                "prestamos_vigentes": 1,
                "inversiones": False
            }
        }
    ]

    # Devolvemos la lista de clientes y omitimos el código de estado (200 por defecto)
    return jsonify(clientes)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
