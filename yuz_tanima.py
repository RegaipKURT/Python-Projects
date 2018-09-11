import cv2
face_cascade = cv2.CascadeClassifier(r"C:\opencv\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"C:\opencv\sources\data\haarcascades_cuda\haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #yüzü tanıması için ilk önce grileştirmemiz gerekiyor.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces: #burada yüzü ve gözleri içine almak için dikdörtgenler çiziyoruz.
        cv2.rectangle(frame, (x,y),(x+w ,y+h),(0,0,255),2 )#yüzüiçine alacak dikdörtgen şekil.
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes: #gözleriiçine alacak kareler, yukarıda oluşturduklarımızı kullanabiliriz.
            cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)
    cv2.imshow("Yuz Tanima Programi", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): #q tuşuna bastığımızda döngü sonlanacak
        break

cap.release()
cv2.destroyAllWindows() #while döngüsünden kodların sonuda pencereyi kapatıyoruz