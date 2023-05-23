from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tienda.html')
def tienda():
    return render_template('tienda.html')

@app.route('/product-details.html', methods=['GET', 'POST'])
def product_details():
    if request.method == 'POST':
        nombre = request.form['nombre']
        imagen = request.form['imagen']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        print(render_template('product-details.html', nombre=nombre, imagen=imagen, precio=precio, descripcion=descripcion))
        return "Compra realizada con éxito"
    else:
        nombre = request.args.get('nombre')
        imagen = request.args.get('imagen')
        precio = request.args.get('precio')
        descripcion = request.args.get('descripcion')
        return render_template('product-details.html', nombre=nombre, imagen=imagen, precio=precio, descripcion=descripcion)

if __name__ == '__main__':
    app.run(debug=True)
