from pushover import Client
import sys
client = Client("uAaiJgBuuy62vG8KYPtsgGgtu291fH", api_token="ae5d2o94ssufeiyy4h8z242124iz9z")
a = "Bu bir deneme bildirim mesajıdır. Lütfen cevap vermeyiniz. Bu bildirimi aldıysanız programınız düzgün çalışıyor demektir. \nİyi Günler..."

client.send_message(a, title="Bildirim Başarılı")

print ("Mesaj Gönderildi...",)
sys.exit()