from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

productos = [
    {'id': 1, 'Nombre': 'Sustituto oseo', 'stock': 1000, 'precio': 35999},
    {'id': 2, 'Nombre': 'Microplacas', 'stock': 965, 'precio': 12999},
    {'id': 3, 'Nombre': 'Cranial Botton Peek', 'stock': 841, 'precio': 9999},
    
]

@app.route('/')
def home():
    return 'Hola! Bienvenido a MicroMedSystem!'

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

@app.route('/procesar_pedido', methods=['POST'])
def procesar_pedido():
    nombre = request.form['nombre']
    productos_pedido = request.json['productos']

    for producto_pedido in productos_pedido:
        producto_id = producto_pedido['id']
        cantidad_pedido = producto_pedido['cantidad']

        for producto in productos:
            if producto['id'] == producto_id:
                if producto['stock'] >= cantidad_pedido:
                    producto['stock'] -= cantidad_pedido
                else:
                    return jsonify({'message': 'Producto agotado'})

    return jsonify({'message': 'Pedido procesado con éxito'})
conn = sqlite3.connect('pedidos_pagina.db')
c = conn.cursor()

c.execute('INSERT INTO pedidos (nombre, direccion, forma_pago) VALUES (?, ?, ?)',
("nombre", "direccion", "sustitutooseo", "microplacas", "cranialbottonpeek", "forma_pago"))

conn.commit()
conn.close()

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

@app.route('/productos/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [producto for producto in productos if producto['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

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