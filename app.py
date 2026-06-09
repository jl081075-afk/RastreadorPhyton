from flask import Flask, render_template, request

app = Flask("_name_")

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    correo = request.form["correo"]
    latitud = request.form["latitud"]
    longitud = request.form["longitud"]

    with open("datos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"Nombre: {nombre} | "
            f"Correo: {correo} | "
            f"Latitud: {latitud} | "
            f"Longitud: {longitud}\n"
        )

    return "Datos recibidos correctamente"

if "_name_" == "_main_":
    app.run(debug=True)
