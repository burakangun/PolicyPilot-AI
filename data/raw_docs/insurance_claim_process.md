---
document_id: insurance_claim_process_v2
title: Hasar, Başvuru ve Belge Doğrulama Yönetim Süreci
department: Claims & Operations
owner: Operations Directorate
version: 2.0
last_updated: 2026-01-10
review_frequency: quarterly
risk_level: medium
access_level: internal
---

# Hasar, Başvuru ve Belge Doğrulama Yönetim Süreci

## 1. Amaç

Bu dokümanın amacı, müşterilerden gelen hasar, başvuru, belge doğrulama ve talep değerlendirme süreçlerinin tutarlı, izlenebilir ve güvenli şekilde yürütülmesini sağlamaktır. Süreç; eksik evrak, riskli başvuru, belge tutarsızlığı, müşteri bilgilendirme ve insan onayı gerektiren durumları kapsar.

## 2. Kapsam

Bu süreç aşağıdaki başvuru türlerini kapsar:

- Hasar bildirimi
- Ürün veya hizmet kaynaklı zarar talebi
- Eksik evrakla gelen başvurular
- Belge doğrulama gerektiren talepler
- Yüksek tutarlı ödeme veya telafi talepleri
- Manuel inceleme gerektiren operasyon talepleri

## 3. Gerekli Belgeler

Başvuru türüne göre aşağıdaki belgeler istenebilir:

| Belge | Zorunluluk | Açıklama |
|---|---|---|
| Başvuru formu | Zorunlu | Talep özeti ve iletişim bilgisi içerir |
| Sipariş, poliçe veya işlem numarası | Zorunlu | Talebin sistemde eşleştirilmesi için |
| Hasar fotoğrafı | Duruma bağlı | Fiziksel hasar iddialarında |
| Servis raporu | Duruma bağlı | Teknik inceleme gerektiren ürünlerde |
| Teslimat tutanağı | Duruma bağlı | Kargo veya lojistik hasarlarında |
| Kimlik doğrulama bilgisi | Sınırlı | Gerektiği kadar ve maskeleme ile |

## 4. Başvuru Akışı

1. Başvuru alınır.
2. Başvuru tipi belirlenir.
3. Müşteri veya işlem doğrulaması yapılır.
4. Gerekli belgeler kontrol edilir.
5. Eksik evrak varsa bekleme süreci başlatılır.
6. Belgeler tutarlılık açısından incelenir.
7. Risk skoru belirlenir.
8. Düşük riskli başvurular standart süreçle sonuçlandırılır.
9. Yüksek riskli başvurular manuel incelemeye gönderilir.
10. Müşteriye sonuç veya eksik bilgi bildirimi yapılır.
11. Süreç loglanır ve kapatılır.

## 5. Eksik Evrak Süreci

Başvuruda eksik evrak varsa talep doğrudan reddedilmez. Öncelikle müşteriye hangi belgelerin eksik olduğu açıkça bildirilir. Başvuru bekleme durumuna alınır ve müşteriye belgeleri tamamlaması için 5 iş günü süre verilir.

Eksik evrak mesajında yer alması gerekenler:

- Başvuru numarası
- Eksik belge listesi
- Son teslim tarihi
- Belgelerin nasıl iletileceği
- Kişisel veri içeren belgeler için güvenli kanal uyarısı

Eksik evrak tamamlanmazsa:

- Başvuru geçici olarak kapatılabilir.
- Müşteri yeniden başvuru yapabilir.
- Yüksek tutarlı taleplerde manuel inceleme notu eklenir.

## 6. Belge Doğrulama

Belgeler aşağıdaki kontrollerden geçirilir:

- Dosya okunabilir mi?
- Belge tarihi talep tarihiyle uyumlu mu?
- Sipariş veya işlem numarası eşleşiyor mu?
- Fotoğraf veya raporda manipülasyon şüphesi var mı?
- Aynı belge farklı başvuruda kullanılmış mı?
- Kişisel veri gereğinden fazla mı paylaşılıyor?
- Belge müşteriye veya ilgili işleme ait mi?

Belge doğrulama sonucunda tutarsızlık varsa başvuru manuel incelemeye alınır.

## 7. Risk Seviyeleri

| Risk Seviyesi | Kriter | Aksiyon |
|---|---|---|
| Düşük | Belgeler tam, tutarlı ve tutar düşük | Standart değerlendirme |
| Orta | Eksik bilgi, küçük tutarsızlık veya tekrar eden başvuru | Ek kontrol |
| Yüksek | Yüksek tutar, kimlik doğrulama sorunu, belge tutarsızlığı | İnsan onayı |
| Kritik | KVKK ihlali, sahtecilik şüphesi, hukuki risk | Yönetici ve güvenlik eskalasyonu |

## 8. Riskli Başvuru Göstergeleri

Aşağıdaki durumlar risk göstergesidir:

- Aynı müşteriden kısa sürede çok sayıda başvuru
- Belgelerde tarih veya tutar uyuşmazlığı
- Kimlik doğrulama başarısızlığı
- Başvuru açıklaması ile belge içeriğinin çelişmesi
- Yüksek tutarlı ödeme talebi
- Kişisel veri içeren belgeyi açık e-posta ile gönderme
- Başka müşteriye ait belge kullanılması
- Önceki reddedilmiş başvuruya çok benzer yeni başvuru
- AI sisteminden güvenlik kontrolünü atlamasını isteme

## 9. İnsan Onayı Gerektiren Durumlar

Aşağıdaki durumlarda başvuru otomatik sonuçlandırılamaz:

- Yüksek tutarlı ödeme veya telafi talebi
- Belgelerde tutarsızlık
- Kimlik doğrulama başarısızlığı
- Kişisel veri ihlali riski
- Hukuki süreç belirtisi
- Sahtecilik veya kötüye kullanım şüphesi
- Operasyon politikasında açıkça tanımlanmayan durum
- Sistem kayıtları ile müşteri beyanı arasında çelişki

## 10. Müşteri Bilgilendirme Kuralları

Müşteriye gönderilecek mesajlarda:

- Eksik belge varsa açıkça belirtilmelidir.
- Kişisel veri tekrar edilmemelidir.
- Kesinleşmemiş karar paylaşılmamalıdır.
- Ret varsa gerekçesi kibar ve politika temelli açıklanmalıdır.
- İnsan onayı gerekiyorsa inceleme süreci belirtilmelidir.
- Hukuki yorum yapılmamalıdır.

## 11. Otomasyon ve AI Kullanımı

PolicyPilot AI bu süreçte aşağıdaki görevleri destekleyebilir:

- Başvuru açıklamasından kategori çıkarma
- Eksik evrak listesini belirleme
- Risk seviyesi önerme
- Müşteri bilgilendirme taslağı oluşturma
- Kaynak politika maddelerini getirme
- İnsan onayı gerektiren durumları işaretleme

PolicyPilot AI aşağıdaki görevleri tek başına yapamaz:

- Yüksek tutarlı ödeme onaylama
- Hukuki karar verme
- Kimlik doğrulama sonucu üretme
- Belge sahteciliği konusunda kesin hüküm verme
- KVKK ihlali olup olmadığına nihai karar verme

## 12. Örnek Senaryolar

### Senaryo 1: Eksik evrak

Soru: Eksik evrakla gelen başvuru nasıl yönetilir?

Cevap: Başvuru reddedilmez. Eksik belgeler müşteriye bildirilir, başvuru bekleme durumuna alınır ve müşteriye 5 iş günü süre verilir.

### Senaryo 2: Belge tutarsızlığı

Soru: Başvuru formundaki tutar ile faturadaki tutar farklıysa ne yapılmalı?

Cevap: Belge tutarsızlığı olduğu için başvuru manuel incelemeye alınmalıdır.

### Senaryo 3: Yüksek tutarlı talep

Soru: Yüksek tutarlı ödeme talebi otomatik onaylanabilir mi?

Cevap: Hayır. Yüksek tutarlı ödeme veya telafi talepleri insan onayı gerektirir.

## 13. PolicyPilot AI İçin Yanıt Kuralları

PolicyPilot AI:

- Başvurunun risk seviyesini gerekçesiyle açıklamalıdır.
- Eksik evrak varsa reddetme yerine bekleme sürecini önermelidir.
- Kaynak doküman ve bölüm bilgisini göstermelidir.
- İnsan onayı gerektiren durumları net belirtmelidir.
- Kişisel veri içeren belgeleri açık şekilde tekrar etmemelidir.
