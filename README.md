# Proyecto 4: Reconocimiento y Validación de Códigos QR

## Descripción
Este proyecto implementa el reconocimiento y validación de códigos QR tal como se especifica en el documento proporcionado.

## Requisitos en macOS
- Python 3.8 o superior
- pip (gestor de paquetes)

### Instalación de dependencias
```bash
# (Opcional) crear y activar un entorno virtual
python3 -m venv env
source env/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar librerías necesarias
pip install qrcode opencv-python pyzbar pillow

# Generar qrs de prueba
python3 generate_qr.py

#Validar qrs
- Escaneo y validacion desde imagenes
python3 scan_validate.py --dir qrcodes

- Escaneo y validacion desde la camara
python3 scan_validate.py --camera
