Para poder utilizar el proyecto de manera local seguir los siguientes pasos

1. Crear un entorno virtual para python
> python -m venv .env
2. entrar en el entorno virtual
> Linux: source .env/bin/activate

> Windows: .\.env\Scripts\activate
3. Ejecutar dependiendo del Sistema Operativo:
> pip install -r requirements_windows.txt

> pip install -r requirements_linux.txt

Las imagenes se descargan de :
> https://drive.google.com/drive/u/0/folders/1LMlGW5jOBNKLEDapLm1r3lJmldcM1r_n

Se guardan en la carpeta *images* que esta en la raiz del proyecto

Obs: Tener en cuenta que si se hace en colab se tendra que importar adicionalmente
- from google.colab import files
- from IPython.display import Image

Tambien que si se hace en vscode ejecutar
> ctrl+shift+p 

y escribir : **python select interpreter** y utilizar el del .env que creamos previamente  