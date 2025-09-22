# Sistema basico de facturacion

Proyecto escolar sobre un sistema básico de facturación (hecho en python) que cumple con las siguientes funcionalidades:

- Pantalla de Login y Register
- CRUD de clientes
- CRUD de Productos
- Emisión y lectura de facturas

### 1) Clonar repositorio

```bash
https://github.com/alejoNoB20/Sistema-basico-de-facturacion.git
```

### 2) Instalar dependecias

```bash
python3 -m venv venv
source venv/Script/activate (Linux)
venv\Script\activate (Windows)
pip install -r requeriments.txt
```

### 3) Levantar servidor local

```bash
python src/app.py
```

## Rutas de navegación

- #### /crearDB (registra automaticamente una cuenta admin)
  Cuenta Admin -> Mail: admin@admin.com Contraseña: admin
- #### /login
- #### /logut
- #### /register
  POST:

```bash
{
    nombre: str
    mail: str
    contraseña: str
}
```

- #### /dashboard
- #### /notFound404
- #### /clients
- #### /clients/add
  POST:

```bash
{
    nombre: str
    direccion: str
    email: str
    telefono: int
}
```

- #### /clients/delete/<<int:id>>
- #### /clients/update/<<int:id>>
- #### /products
- #### /products/add
  POST:

```bash
{
    descripcion: str
    precio: float
    stock: int
}
```

- #### /products/delete/<<int:id>>
- #### /products/update/<<int:id>>
- #### /invoices
- #### /invoices/add
- #### /invoices/add_product
  POST:

```bash
{
    cliente: int
    producto: int
    cantidad: int
}
```

- #### /invoices/delete_product/<<int:index>>
- #### /invoices/create
- #### /invoices/cancel
- #### /invoices/details/<<int:id>>
