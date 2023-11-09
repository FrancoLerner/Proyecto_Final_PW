var appVue2 = new Vue({
    el: '#app',
    data: {
        titulo: 'Lista de Productos',
        productos: [
            { 'id': 1, 'nombre': 'Sustituto oseo', 'stock': 1000, 'precio': 35999 },
            { 'id': 2, 'nombre': 'Microplacas', 'stock': 965, 'precio': 12999 },
            { 'id': 3, 'nombre': 'Cranial Botton Peek', 'stock': 841, 'precio': 9999 },
            { 'id': 4, 'nombre': 'Microbotton Peek', 'stock': 100, 'precio': 13500 }
        ],
        nuevoProducto: ''
    },
    methods: {
        agregarProducto: function() {
            if (this.nuevoProducto.trim()) {
                var producto = { nombre: this.nuevoProducto };
                this.productos.push(producto)
                this.nuevoProducto = ''
            }
        },
        eliminarProducto: function(indiceProducto) {
            this.productos.splice(indiceProducto, 1)
        }
    }
})