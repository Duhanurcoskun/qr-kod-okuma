import cv2

 # Kamerayı açma
kamera = cv2.VideoCapture(0)

 # Kamera kontrol
if not kamera.isOpened():
    print("Kamera kapalı!")
    exit()

 # QR kod arama
qr_kod_arama = cv2.QRCodeDetector()

 # Sürekli görüntü alınması
while 1: 
    basarili, goruntu = kamera.read()

    if not basarili:
        print("Görüntü alınamadı!")
        break

 # QR kodu bul ve oku
    qr_icerigi, noktalar, duzlestirilmis = qr_kod_arama.detectAndDecode(goruntu)

 #Yer tespiti
    if noktalar is not None :

    #QR cervesi olusturma
        cv2.polylines(goruntu,
                  [noktalar.astype(int)],
                  True,
                  (0,255,0),
                  2
      )
     
        if qr_icerigi :
            cv2.putText(goruntu,
                        f"Icerik: {qr_icerigi}",
                       (20,80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                         0.8,
                          (0,255,0),
                           2 )
            if qr_icerigi == "GOREV_1":
                mesaj = "GOREV_1 ALGILANDI"
            elif qr_icerigi == "GOREV_2":
                mesaj = "GOREV_2 ALGILANDI"
            elif qr_icerigi == "GOREV_3":
               mesaj = "GOREV_3 ALGILANDI"
            else :
               mesaj = "TANINMAYAN QR"
        else :
            mesaj = "QR OKUNAMADI" 
    else :
        mesaj = "QR ARANIYOR..."

 #Mesaj yazma
    cv2.putText(goruntu,
             mesaj,
             (20,40),
             cv2.FONT_HERSHEY_SIMPLEX,
             0.8,
             (0,255,0),
             2
             )

  #Kamerayı ekranda göster
    cv2.imshow("kameram",goruntu)

 # döngüden çıkma
    if cv2.waitKey(1) & 0xFF == ord("q"):
     break
 # kamerayı serbest bırakma
kamera.release()
cv2.destroyAllWindows()



    
 












    
    







        



