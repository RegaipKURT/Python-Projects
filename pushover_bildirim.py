from pushover import Client
import sys
client = Client("client", api_token="api") #client ve api yazan yerlerin değerlerini gir!
a = "Bu bir deneme bildirim mesajıdır. Lütfen cevap vermeyiniz. Bu bildirimi aldıysanız programınız düzgün çalışıyor demektir. \nİyi Günler..."

client.send_message(a, title="Bildirim Başarılı")

print ("Mesaj Gönderildi...",)
sys.exit()
