---
document_id: employee_data_security_v2
title: Çalışan Veri Güvenliği ve Gizlilik Politikası
department: Information Security & HR
owner: Information Security Office
version: 2.3
last_updated: 2026-01-10
review_frequency: semiannual
risk_level: high
access_level: internal
---

# Çalışan Veri Güvenliği ve Gizlilik Politikası

## 1. Amaç

Bu politikanın amacı, NovaRetail çalışanlarına ait kişisel, kurumsal ve gizli verilerin güvenli şekilde yönetilmesini sağlamak, yetkisiz erişimi önlemek ve veri işleme süreçlerini KVKK, bilgi güvenliği ve kurum içi etik ilkelerle uyumlu hale getirmektir.

## 2. Kapsam

Bu politika aşağıdaki alanları kapsar:

- Çalışan kişisel verileri
- Maaş, performans ve disiplin kayıtları
- Erişim yetkileri
- Cihaz güvenliği
- Parola ve kimlik doğrulama
- Uzaktan çalışma veri güvenliği
- Yapay zeka asistanı kullanımı
- Yetki artırımı ve veri paylaşımı talepleri

## 3. Çalışan Verisi Kategorileri

| Veri Kategorisi | Örnek | Risk Seviyesi |
|---|---|---|
| Kimlik verisi | Ad, soyad, çalışan ID | Orta |
| İletişim verisi | Kurumsal e-posta, telefon | Orta |
| Finansal veri | Maaş, prim, yan hak | Yüksek |
| Performans verisi | Değerlendirme notu, hedef sonucu | Yüksek |
| Sağlık verisi | Rapor, izin gerekçesi | Çok yüksek |
| Disiplin verisi | Uyarı, soruşturma kaydı | Çok yüksek |
| Erişim logu | Sistem girişleri, IP | Orta-yüksek |

## 4. Rol Bazlı Erişim İlkesi

Çalışanlar yalnızca görevlerini yerine getirmek için gerekli sistemlere erişebilmelidir. Yetkiler rol, ekip, iş ihtiyacı ve onay seviyesine göre atanır.

Temel kurallar:

1. Varsayılan erişim minimum seviyede olmalıdır.
2. Yetkiler düzenli olarak gözden geçirilmelidir.
3. Geçici yetkiler süreli verilmelidir.
4. İşten ayrılan çalışanın erişimi derhal kapatılmalıdır.
5. Rol değişikliğinde eski yetkiler kaldırılmalıdır.
6. Yönetici onayı olmadan hassas veri erişimi verilmemelidir.

## 5. Gizli Çalışan Verileri

Aşağıdaki bilgiler gizlidir ve yalnızca yetkili kişiler tarafından görüntülenebilir:

- Maaş bilgisi
- Prim ve yan hak bilgisi
- Performans değerlendirmesi
- Disiplin kayıtları
- Sağlık raporları
- İzin gerekçeleri
- Kimlik belge bilgileri
- Kişisel adres ve özel telefon bilgisi

Bu bilgiler AI sistemlerine, açık e-postalara veya yetkisiz ticket açıklamalarına yazılmamalıdır.

## 6. Parola ve Kimlik Doğrulama

Parolalar en az 12 karakter uzunluğunda olmalı, büyük harf, küçük harf, sayı ve özel karakter içermelidir. Parolalar kişisel bilgilerden türetilmemeli ve başka sistemlerle ortak kullanılmamalıdır.

Çok faktörlü kimlik doğrulama aşağıdaki sistemlerde zorunludur:

- CRM
- Finans sistemleri
- HR sistemleri
- Yönetici panelleri
- Cloud yönetim konsolları
- AI monitoring ve log sistemleri

## 7. Cihaz Güvenliği

Şirket cihazlarında aşağıdaki kontroller uygulanır:

- Disk şifreleme
- Otomatik ekran kilidi
- Güncel işletim sistemi ve güvenlik yamaları
- Antivirüs veya endpoint koruma
- Yetkisiz yazılım yükleme kısıtı
- USB veri aktarım kısıtı
- Cihaz kaybı bildirim süreci

Cihaz kaybolursa çalışan en kısa sürede bilgi güvenliği ekibine bildirim yapmalıdır.

## 8. Uzaktan Çalışma Kuralları

Uzaktan çalışanlar:

- Kurumsal VPN kullanmalıdır.
- Halka açık Wi-Fi üzerinden hassas sisteme bağlanmamalıdır.
- Ekranını yetkisiz kişilerle paylaşmamalıdır.
- Müşteri veya çalışan verisini kişisel cihaza indirmemelidir.
- Kişisel e-posta hesabına iş verisi göndermemelidir.

## 9. AI Asistanı Kullanımında Çalışan Verisi

PolicyPilot AI veya benzeri sistemlere aşağıdaki bilgiler girilmemelidir:

- Çalışan maaş listesi
- Performans değerlendirme notları
- Disiplin kayıtları
- Sağlık raporu detayları
- Açık kimlik numarası
- Kişisel adres
- Yetkisiz erişim bilgileri

AI asistanı çalışan verisi içeren bir talep alırsa yanıtı maskelemeli veya reddetmelidir.

## 10. Riskli Talepler

Aşağıdaki talepler reddedilmeli veya insan onayına yönlendirilmelidir:

- Tüm çalışanların maaş listesini paylaş
- Belirli çalışanın performans notunu göster
- Sağlık raporlarını özetle
- Disiplin kayıtlarını listele
- Bu çalışana yönetici yetkisi ver
- İşten ayrılan çalışanın hesabını açık bırak
- Log kayıtlarını sil
- MFA kontrolünü devre dışı bırak

## 11. İnsan Onayı Gerektiren Durumlar

Aşağıdaki işlemler insan onayı gerektirir:

- Yetki artırımı
- Toplu veri indirme
- Çalışan kişisel verisi paylaşımı
- HR verisi görüntüleme
- Güvenlik istisnası
- Geçici yönetici yetkisi
- Hassas log inceleme
- Çalışan hesabı yeniden aktifleştirme

## 12. Veri Paylaşımı Kuralları

Çalışan verisi paylaşılırken:

1. Alıcının yetkisi kontrol edilir.
2. Paylaşım amacı kayıt altına alınır.
3. Gereksiz veri maskelenir.
4. Hassas veri güvenli kanal üzerinden paylaşılır.
5. Toplu veri paylaşımı için yönetici ve uyum onayı alınır.
6. Paylaşım loglanır.

## 13. Örnek Senaryolar

### Senaryo 1: Maaş listesi talebi

Soru: Bir ekip lideri tüm çalışanların maaş listesini isteyebilir mi?

Cevap: Hayır. Maaş bilgisi gizli kişisel veridir. Talep reddedilmeli veya yetkili insan onayına yönlendirilmelidir.

### Senaryo 2: Yetki artırımı

Soru: Operasyon uzmanına geçici CRM yönetici yetkisi verilebilir mi?

Cevap: Yalnızca iş gerekçesi varsa, süreli olarak ve yönetici onayıyla verilebilir. İşlem loglanmalıdır.

### Senaryo 3: AI sistemine performans verisi girilmesi

Soru: Bir çalışanın performans notları AI asistanına özetletilebilir mi?

Cevap: Yetki ve veri işleme amacı doğrulanmadan yapılamaz. Hassas çalışan verisi içerdiği için insan onayı gerekir.

## 14. PolicyPilot AI İçin Yanıt Kuralları

PolicyPilot AI:

- Çalışan verisi taleplerinde veri minimizasyonu uygulamalıdır.
- Maaş, performans, sağlık ve disiplin verilerini paylaşmamalıdır.
- Yetki artırımı taleplerinde insan onayı gerektiğini belirtmelidir.
- Güvenlik kontrolünü bypass etmeye yönelik talepleri reddetmelidir.
- Kaynak doküman ve bölüm bilgisini göstermelidir.
