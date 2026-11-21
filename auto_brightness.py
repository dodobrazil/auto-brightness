# Sorun: Kullanıcılar bilgisayar ekran parlaklığını ortam ışığına göre manuel ayarlamak zorunda kalıyor.
# Çözüm: Webcam'den alınan ışık seviyesine göre otomatik ekran parlaklığı ayarlayan bir Python scripti.

import cv2
import screen_brightness_control as sbc

def ortam_isigi_olc():
    """Webcam'den ortam ışığı seviyesini ölçer."""
    kamera = cv2.VideoCapture(0)
    ret, kare = kamera.read()
    kamera.release()
    if ret:
        gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
        ortalama_isik = gri.mean()
        return ortalama_isik
    else:
        return None

def parlaklik_ayarla(isik_seviyesi):
    """Işık seviyesine göre ekran parlaklığını ayarlar."""
    if isik_seviyesi is not None:
        yeni_parlaklik = max(10, min(100, int(isik_seviyesi / 2)))
        sbc.set_brightness(yeni_parlaklik)
        print(f"Parlaklık {yeni_parlaklik}% olarak ayarlandı.")
    else:
        print("Işık seviyesi ölçülemedi.")

# Işık seviyesini ölçüp parlaklığı ayarla
isik_seviyesi = ortam_isigi_olc()
parlaklik_ayarla(isik_seviyesi)
