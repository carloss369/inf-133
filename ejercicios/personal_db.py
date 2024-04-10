import sqlite3

# Conectar a la base de datos (si no existe, se creará automáticamente)
conn = sqlite3.connect('personal.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla llamada 'personas' con columnas de ejemplo
cursor.execute('''
    CREATE TABLE IF NOT EXISTS personas (
        salarios INTEGER PRIMARY KEY,
        empleados TEXT NOT NULL,
        departamentos INTEGER,
        cargos TEXT
    )
''')


