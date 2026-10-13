ventas = [    
  {"producto": "Teclado", "precio": 25, "unidades": 2},    
  {"producto": "Ratón", "precio": 15, "unidades": 3},    
  {"producto": "Monitor", "precio": 180, "unidades": 1},   
  {"producto": "Teclado", "precio": 25, "unidades": 1},    
  {"producto": "Auriculares", "precio": 40, "unidades": 2},    
  {"producto": "Ratón", "precio": 15, "unidades": 4}
]

#recorrer lista y construir conjunto con los nombres de los productos
productos = set()
for venta in ventas:
    productos.add(venta["producto"])
print(productos)

productos_vendidos = productos.union(set([venta["producto"] for venta in ventas]))
print(productos_vendidos)

productos_vendidos = productos.intersection(set([venta["producto"] for venta in ventas]))
print(productos_vendidos)

