import qrcode
import os

def generar_qr(data: str, filename: str) -> None:
    """Genera un código QR con los datos dados y lo guarda en filename."""
    img = qrcode.make(data)
    img.save(filename)

def main():
    os.makedirs("qrcodes", exist_ok=True)

    tests = [
        "https://www.example.com/valid/path",      # válido
        "http://invalid-url",                      # inválido (no HTTPS)
        "Hola Mundo",                              # inválido (no URL)
        "https://sub.dominio.com/recurso?param=1", # válido
    ]

    for i, data in enumerate(tests, 1):
        filename = f"qrcodes/qrcode_{i}.png"
        generar_qr(data, filename)
        print(f"Generado {filename} con datos: {data}")

if __name__ == "__main__":
    main()