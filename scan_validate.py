import cv2
from pyzbar import pyzbar
import re
import argparse
import os

def validar_contenido(data: str) -> bool:
    """Comprueba que data sea una URL HTTPS válida."""
    pattern = re.compile(r"^https:\/\/(www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}\/?.*$")
    return bool(pattern.match(data))

def decodificar_imagen(img) -> list[tuple[str,bool]]:
    """Retorna lista de (texto, válido?) de todos los QR detectados en img."""
    barcodes = pyzbar.decode(img)
    return [(b.data.decode("utf-8"), validar_contenido(b.data.decode("utf-8"))) for b in barcodes]

def procesar_imagenes(directorio: str) -> None:
    for fname in os.listdir(directorio):
        path = os.path.join(directorio, fname)
        img = cv2.imread(path)
        if img is None:
            continue
        resultados = decodificar_imagen(img)
        print(f"Archivo: {fname}")
        if resultados:
            for data, valid in resultados:
                estado = "VÁLIDO" if valid else "INVÁLIDO"
                print(f"  {data} -> {estado}")
        else:
            print("  No se detectó un código QR.")

def procesar_camara() -> None:
    cap = cv2.VideoCapture(0)
    print("Presiona 'q' para salir.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        for data, valid in decodificar_imagen(frame):
            estado = "VÁLIDO" if valid else "INVÁLIDO"
            color = (0,255,0) if valid else (0,0,255)
            cv2.putText(frame, f"{data} -> {estado}", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        cv2.imshow("Escaneo QR", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="Escaneo y validación de códigos QR")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--dir", help="Directorio de imágenes con códigos QR")
    group.add_argument("--camera", action="store_true",
                       help="Usar cámara para escanear en tiempo real")
    args = parser.parse_args()

    if args.dir:
        procesar_imagenes(args.dir)
    elif args.camera:
        procesar_camara()

if __name__ == "__main__":
    main()
