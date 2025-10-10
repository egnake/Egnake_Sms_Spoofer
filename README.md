# Etik-SMS-Sender — Twilio ile Temiz SMS Gönderimi
**Hazırlayan:** Ege Parlak  
**Kısa:** Bu repo Twilio kullanarak eğitim ve izinli test amaçlı SMS gönderimini gösterir. *İzinsiz kullanım yasaktır.*

---

## Özet
Basit, öğretici ve etik bir Twilio SMS gönderici iskeleti. Amaç: güvenli anahtar yönetimi, günlükleme, rate-limit ve toplu izinli gönderim örnekleri sunmak. Bu repo **spoofing**, spam veya başka bir şekilde kötüye kullanım için kullanılmamalıdır.

---

## HUKUKİ UYARI — ÖNEMLİ (OKU!)
- Bu proje yalnızca **eğitim ve yazılı izin alınmış test** amaçlıdır.  
- Repo içindeki hiçbir içerik, izinsiz SMS gönderimi veya kötüye kullanım için yasal sorumluluğu ortadan kaldırmaz.  
- Hazırlayan veya bu repo bakımcıları, kullanıcıların bu materyali kötü amaçla kullanmasından doğan yasal sorumluluklar için sorumluluk kabul etmez.  
- Eğer bu proje ile ilgili yasal koruma, kullanım sınırları veya özel hukuki tavsiye istiyorsan, **konusunda uzman bir avukata** danışmalısın. Disclaimers (feragatnameler) tek başına yasaları veya cezai sorumluluğu kaldırmaz.

---

## Kullanım Koşulları (Kısa)
- Bu yazılımı yalnızca hedefin yazılı iznini aldığın durumlarda kullan.  
- Toplu mesaj göndermeden önce hedeflerin açık rızasını belgele.  
- Herhangi bir kötüye kullanım tespiti durumunda projeyi kullanmayı derhal bırak.

---

## Özellikler
- Ortam değişkenleriyle konfigürasyon (SID, TOKEN, PHONE).  
- Tekli ve toplu gönderim örnekleri.  
- Basit günlükleme (events.log).  
- Opsiyonel rate-limit (gönderimler arası gecikme).  
- `.gitignore`, `requirements.txt`, MIT lisansı örneği.

---

## Kurulum
1. Repo'yu klonla:
   ```bash
   git clone https://github.com/<kullanici>/<repo>.git
   cd <repo>
