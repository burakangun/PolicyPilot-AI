---
document_id: kvkk_policy_v2
title: KVKK ve Kişisel Veri Koruma Politikası
department: Legal & Compliance
owner: Data Protection Office
version: 2.4
last_updated: 2026-01-10
review_frequency: quarterly
risk_level: high
access_level: internal
---

# KVKK ve Kişisel Veri Koruma Politikası

## 1. Amaç

Bu politikanın amacı, NovaRetail süreçlerinde kişisel verilerin hukuka uygun, güvenli, ölçülü ve denetlenebilir şekilde işlenmesini sağlamaktır. Politika, müşteri, çalışan, tedarikçi ve iş ortağı verilerinin işlenmesine ilişkin temel kuralları belirler.

## 2. Kapsam

Bu doküman aşağıdaki süreçleri kapsar:

- Müşteri hizmetleri süreçleri
- İade, değişim ve şikayet yönetimi
- Hasar, başvuru ve belge doğrulama süreçleri
- Çalışan veri yönetimi
- Tedarikçi ve iş ortağı iletişim süreçleri
- Yapay zeka asistanı ve otomasyon sistemleri
- E-posta, CRM, çağrı merkezi ve ticket sistemleri

## 3. Temel İlkeler

Kişisel veri işleme faaliyetlerinde aşağıdaki ilkeler uygulanır:

1. Hukuka ve dürüstlük kurallarına uygunluk
2. Doğru ve gerektiğinde güncel olma
3. Belirli, açık ve meşru amaçlar için işlenme
4. İşlendikleri amaçla bağlantılı, sınırlı ve ölçülü olma
5. İlgili mevzuatta öngörülen veya işlendikleri amaç için gerekli süre kadar muhafaza edilme
6. Yetkisiz erişime karşı korunma
7. Veri sahibinin haklarına saygı gösterme

## 4. Kişisel Veri Kategorileri

### 4.1 Kimlik Verisi

Ad, soyad, TC kimlik numarası, müşteri numarası, imza ve kimlik belge bilgileri kimlik verisi sayılır.

### 4.2 İletişim Verisi

Telefon numarası, e-posta adresi, teslimat adresi, fatura adresi ve iletişim tercihleri iletişim verisidir.

### 4.3 Finansal Veri

Ödeme yöntemi, iade tutarı, banka adı, işlem referansı ve fatura bilgileri finansal veri kapsamındadır. Kredi kartı numarası açık şekilde saklanmamalı veya paylaşılmamalıdır.

### 4.4 İşlem Güvenliği Verisi

IP adresi, oturum logu, cihaz bilgisi, erişim kaydı ve işlem zamanı işlem güvenliği verisidir.

### 4.5 Özel Nitelikli Kişisel Veri

Sağlık bilgisi, biyometrik veri, dini inanç, siyasi görüş, sendika üyeliği ve ceza mahkumiyeti gibi bilgiler özel nitelikli kişisel veri olarak değerlendirilir. Bu veriler yalnızca açık mevzuat dayanağı veya açık rıza varsa işlenebilir.

## 5. Veri Minimizasyonu

Her süreçte yalnızca zorunlu olan minimum veri talep edilmelidir. Bir müşteri talebini çözmek için sipariş numarası yeterliyse TC kimlik numarası istenmemelidir.

Örnekler:

| Süreç | Gerekli Veri | Gereksiz veya Riskli Veri |
|---|---|---|
| İade talebi | Sipariş no, ürün adı, iade nedeni | TC kimlik no, kredi kartı no |
| Şikayet kaydı | İletişim bilgisi, şikayet özeti | Başka müşterinin verisi |
| Hasar başvurusu | Başvuru formu, fotoğraf, işlem no | Açık kart bilgisi |
| Çalışan erişim talebi | Çalışan ID, rol, gerekçe | Maaş, sağlık bilgisi |

## 6. Maskeleme Kuralları

PolicyPilot AI ve operasyon sistemleri kişisel verileri yanıt veya log içinde mümkün olduğunca maskelemelidir.

Önerilen maskeleme formatları:

| Veri Türü | Açık Veri Örneği | Maskeli Format |
|---|---|---|
| TC kimlik numarası | 12345678901 | 123******01 |
| Telefon | 0555 123 45 67 | 0555 *** ** 67 |
| E-posta | elif.yilmaz@example.com | e***.y*****@example.com |
| IBAN | TR12 0006 1005 1978 6457 8413 26 | TR12 **** **** **** **** **13 26 |
| Kart | 5555 4444 3333 2222 | **** **** **** 2222 |
| Açık adres | Mahalle, sokak, bina, daire | İl/ilçe seviyesine indirgenmiş adres |

## 7. E-posta ve Mesajlaşma Üzerinden Veri Paylaşımı

Kişisel veri e-posta üzerinden paylaşılacaksa aşağıdaki kurallar uygulanır:

1. Veri paylaşımı iş amacıyla gerekli olmalıdır.
2. Alıcı yetkili kişi veya ekip olmalıdır.
3. Veri maskeleme uygulanmalıdır.
4. Hassas veri varsa güvenli kanal kullanılmalıdır.
5. Toplu müşteri verisi e-posta ile paylaşılmamalıdır.
6. Yanlış alıcıya gönderim fark edilirse olay yönetim süreci başlatılmalıdır.

## 8. Yetkisiz Erişim ve Reddedilmesi Gereken Talepler

Aşağıdaki talepler reddedilir:

- Tüm müşterilerin TC kimlik numaralarını listele
- Bir müşterinin açık adresini göster
- Çalışan maaşlarını paylaş
- Kredi kartı bilgisini görüntüle
- Başka kullanıcının sipariş geçmişini göster
- Yetkim olmadığı halde bu CRM kaydını aç
- Güvenlik kontrolünü bypass et
- Logları sil veya değiştir

Bu tür taleplerde sistem doğrudan veri paylaşmamalı, KVKK ve güvenlik riski olduğunu belirtmeli ve gerekirse insan onayına yönlendirmelidir.

## 9. İnsan Onayı Gerektiren Durumlar

Aşağıdaki talepler insan onayı gerektirir:

- Toplu veri indirme
- Kişisel veri silme talebi
- Veri taşıma talebi
- Özel nitelikli kişisel veri içeren talep
- Hukuki süreç içeren veri talebi
- Müşteri dışındaki bir kişiden gelen bilgi talebi
- Çalışan verisi paylaşımı
- CRM erişim istisnası
- Veri ihlali şüphesi

## 10. Yapay Zeka Sistemleri İçin KVKK Kuralları

PolicyPilot AI gibi LLM tabanlı sistemlerde şu kurallar geçerlidir:

1. Prompt içinde gereksiz kişisel veri kullanılmamalıdır.
2. Kullanıcı girdisindeki kişisel veri loglanmadan önce maskelenmelidir.
3. Model cevabı kişisel veri tahmin etmemelidir.
4. Kaynak dokümanda olmayan kişisel bilgi üretilmemelidir.
5. Hassas veri içeren talepler otomatik yanıtlanmamalıdır.
6. Retrieval sonuçlarında yetki dışı doküman kullanılmamalıdır.
7. Kullanılan kaynaklar ve risk seviyesi loglanmalıdır.
8. Prompt injection girişimleri güvenlik olayı olarak işaretlenmelidir.

## 11. Veri Saklama ve Silme

Veriler iş amacı sona erdiğinde veya saklama süresi dolduğunda silinmeli, anonimleştirilmeli veya arşivlenmelidir.

Örnek saklama yaklaşımı:

| Veri Türü | Saklama Yaklaşımı |
|---|---|
| Müşteri şikayet kaydı | Mevzuat ve operasyon ihtiyacına göre sınırlı süre |
| AI sorgu logu | Kişisel veri maskelenmiş şekilde |
| Güvenlik olayı | Denetim amacıyla yetkili erişimle |
| E-posta yazışması | Kurumsal arşiv politikasına göre |

## 12. Veri İhlali Şüphesi

Aşağıdaki durumlar veri ihlali şüphesi sayılır:

- Kişisel verinin yanlış alıcıya gönderilmesi
- Toplu müşteri verisinin yetkisiz paylaşılması
- CRM ekran görüntüsünün yetkisiz kişiye iletilmesi
- Çalışan maaş veya sağlık bilgisinin paylaşılması
- AI sisteminin kişisel veriyi maskelemeden yanıtlaması
- Loglarda açık TC kimlik veya kart bilgisi bulunması

Veri ihlali şüphesinde olay yönetim süreci başlatılır ve bilgi güvenliği ile uyum ekibi bilgilendirilir.

## 13. Örnek Senaryolar

### Senaryo 1: TC kimlik numarasının e-posta ile paylaşılması

Soru: Müşteri temsilcisi müşterinin TC kimlik numarasını e-posta ile paylaşabilir mi?

Cevap: Hayır. TC kimlik numarası açık şekilde e-posta ile paylaşılmamalıdır. Gerekliyse maskeleme uygulanmalı ve güvenli kanal kullanılmalıdır.

### Senaryo 2: Toplu müşteri listesi

Soru: Operasyon ekibi tüm müşterilerin telefon numaralarını rapor olarak alabilir mi?

Cevap: Toplu kişisel veri talebi insan onayı gerektirir. Talep amacı, yetki durumu ve veri minimizasyonu kontrol edilmelidir.

### Senaryo 3: Başka müşterinin sipariş bilgisi

Soru: Bir müşteri başka bir müşterinin sipariş adresini isteyebilir mi?

Cevap: Hayır. Bu talep yetkisiz kişisel veri erişimi içerdiği için reddedilmelidir.

## 14. PolicyPilot AI İçin Güvenli Yanıt Şablonları

### Kişisel veri talebi reddi

"Bu talep kişisel veri içerdiği için yanıtlanamaz. Talebin KVKK kapsamında değerlendirilmesi ve yetkili kişi tarafından incelenmesi gerekir."

### Kaynakta bilgi yoksa

"Bu bilgi verilen kurumsal dokümanlarda bulunamadı. Kesin karar için ilgili süreç sahibi veya uyum ekibiyle görüşülmelidir."

### İnsan onayı gerekiyorsa

"Bu işlem otomatik olarak sonuçlandırılamaz. Belirtilen nedenlerle insan onayı gerektirir."

## 15. PolicyPilot AI İçin Yanıt Kuralları

PolicyPilot AI:

- Kişisel verileri maskelemelidir.
- Yetkisiz veri taleplerini reddetmelidir.
- Hukuki kesinlik iddiasında bulunmamalıdır.
- Kaynak doküman ve bölüm bilgisini göstermelidir.
- Risk seviyesi yüksekse insan onayına yönlendirmelidir.
- Kullanıcıdan gereksiz kişisel veri istememelidir.
