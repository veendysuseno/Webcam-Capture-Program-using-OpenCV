import cv2
import numpy as np
import os

# Membuat direktori 'images' jika belum ada
if not os.path.exists('images'):
    os.makedirs('images')

# Mengaktifkan kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

# Inisialisasi variabel untuk menghitung jumlah gambar yang disimpan
image_count = 0

while True:
    # Membaca frame dari kamera
    ret, image = cap.read()

    if ret:
        # Menampilkan gambar dari kamera di jendela baru
        cv2.imshow("image", image)

    # Menunggu input tombol dari pengguna
    key = cv2.waitKey(1) & 0xFF

    # Jika tombol 's' ditekan, simpan gambar dan ambil gambar baru
    if key == ord('s'):
        # Menyimpan gambar ke direktori 'images'
        image_filename = f'images/image_{image_count}.jpg'
        if cv2.imwrite(image_filename, image):
            print(f"Gambar disimpan: {image_filename}")
            image_count += 1
        else:
            print(f"Error menyimpan gambar: {image_filename}")

    # Jika tombol 'q' ditekan, keluar dari program
    elif key == ord('q'):
        break

# Membersihkan jendela dan mematikan kamera
cv2.destroyAllWindows()
cap.release()
