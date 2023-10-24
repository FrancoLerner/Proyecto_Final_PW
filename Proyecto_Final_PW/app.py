from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {'id': 1, 'Nombre': 'Neumatico', 'stock': 100, 'precio': 79.999},
    {'id': 2, 'Nombre': 'Valvula', 'stock': 50, 'precio': 9.999},
    {'id': 3, 'Nombre': 'Pastillas de freno', 'stock': 200, 'precio': 14.999},
    {'id': 4, 'Nombre': 'Bujías', 'stock': 75, 'precio': 15.999},
    {'id': 5, 'Nombre': 'Filtro de aire', 'stock': 120, 'precio': 9.999},
    {'id': 6, 'Nombre': 'Bateria', 'stock': 150, 'precio': 49.999},
    {'id': 7, 'Nombre': 'Llantas', 'stock': 30, 'precio': 99.999},
    {'id': 8, 'Nombre': 'Amortiguadores', 'stock': 25, 'precio': 40.999},
    {'id': 9, 'Nombre': 'Correa de transmisión', 'stock': 60, 'precio': 10.999},
    {'id': 10, 'Nombre': 'Filtros de aceite', 'stock': 80, 'precio': 3.999}
    
]



@app.route('/')
def home():
    return 'Hola! Bienvenido a Diesel Avellaneda!'

@app.route('/productos' , methods = ['GET'])
def productosGet():
    return jsonify({"productos": productos, "status": "ok"})

@app.route('/productos/<int:id>', methods=['GET'])
def productosGetUno(id):
    for producto in productos:
        if producto['id'] == id:
            return jsonify({'producto': producto, 'status': 'ok'})
    return 'Producto no encontrado'

#Ejemplo con QUERY PARAMS

#@app.route('/productos', methods=['GET'])
#def productosGetUnoPorQuery():
 #   id = request.args.get('id', type=int)
  #  salida = []
   # for producto in productos:
    #    if producto['id'] == id:
     #       salida.append(producto)
    #return jsonify({"productos": salida, "status": "ok"})


@app.route('/productos', methods=['POST'])
def productosPost():
    body = request.json
    Nombre = body["Nombre"]
    id = body["id"]
    precio = body["precio"]
    stock = body["stock"]
    ProductoAlta = {"Nombre": Nombre, "id": id, "precio": precio, "stock": stock}
    productos.append(ProductoAlta)
    return jsonify ({"producto": ProductoAlta, "status": 'ok'})

@app.route('/productos/<int:id>/<op>/<int:cantidad>', methods=['PUT'])
def productoPutUpdatePorPathString(id, op, cantidad):
    for producto in productos:
        if producto['id'] == id:
            if op == 'venta':
                producto['stock'] = max(0, producto['stock'] - cantidad)
            elif op == 'compra':
                producto['stock'] += cantidad
            return jsonify({'producto': producto, 'status': 'ok'})
    return 'Producto no encontrado', 404


@app.route('/productos', methods=['PUT'])
def productoPutUpdatePorBody():
    body = request.json
    id = body.get('id')
    stock = body.get('stock')
    precio = body.get('precio')

    if id is not None and stock is not None and precio is not None:
        for producto in productos:
            if producto['id'] == id:
                producto['stock'] = stock
                producto['precio'] = precio
                return jsonify({'producto': producto, 'status': 'ok'})
        return 'Producto no encontrado', 404
    else:
        return 'Datos incompletos', 400
    
@app.route('/productos/<int:id>', methods=['DELETE'])
def productoDelete(id):
    for producto in productos:
        if producto['id'] == id:
            productos.remove(producto)
            return jsonify({'status': 'ok'})
    return 'Producto no encontrado', 404



if __name__== '__main__':
    app.run(debug=True, port=5500)