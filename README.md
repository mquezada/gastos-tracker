# gastos-tracker

Ejecutar gastos.py a gusto.

## Usar con SQLAlchemy

Si ya estuvo usando la version anterior con archivos CSV, ahora esta versión usa SQLAlchemy. Primero instalar SQLAlchemy (usando `pip` o `easy_install`), y crear la base de datos:

```bash
python create_database.py
```

Luego importar la información existente en CSV a la base de datos (asume que los archivos están en el directorio `records`):

```bash
python migrate_csv.py
```

## Virtualenv

Para no hacer el proceso más lento, si se está usando virtualenv se puede usar el script `gastos` para no tener que activar/desactivar el virtualenv al momento de ejecutar el script principal. Primero, hay que agregar el directorio del virtualenv correspondiente al script:

```bash
#!/bin/bash

VIRTUALENV_PATH=''


source "$VIRTUALENV_PATH/bin/activate"
$VIRTUALENV_PATH/bin/python gastos.py
# source "$VIRTUALENV_PATH/bin/deactivate"
```

```bash
chmod +x gastos
```

Y luego usar el script `gastos` en vez de `gastos.py`
