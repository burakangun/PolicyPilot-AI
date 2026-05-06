---
document_id: access_control_policy_v1
title: Erişim Kontrolü, Yetki Yönetimi ve Denetim Politikası
department: Information Security
owner: Identity & Access Management Team
version: 1.0
last_updated: 2026-01-10
review_frequency: quarterly
risk_level: high
access_level: internal
---

# Erişim Kontrolü, Yetki Yönetimi ve Denetim Politikası

## 1. Amaç

Bu politikanın amacı, NovaRetail sistemlerinde erişim yetkilerinin güvenli, izlenebilir ve görev ayrılığı prensibine uygun şekilde yönetilmesini sağlamaktır.

## 2. Kapsam

Bu politika aşağıdaki sistemler için geçerlidir:

- CRM
- ERP
- Finans sistemleri
- HR sistemleri
- Müşteri destek paneli
- Veri ambarı
- AI asistanı yönetim paneli
- Log ve monitoring sistemleri
- Cloud yönetim konsolları

## 3. Temel İlkeler

- En az yetki prensibi uygulanır.
- Rol bazlı erişim modeli tercih edilir.
- Kritik işlemler için çoklu onay gerekebilir.
- Yetkiler düzenli olarak gözden geçirilir.
- Tüm erişim talepleri kayıt altına alınır.
- Yetki değişiklikleri loglanır.
- Görev değişikliği sonrası eski yetkiler kaldırılır.

## 4. Rol Bazlı Erişim Seviyeleri

| Rol | Erişim Seviyesi | Açıklama |
|---|---|---|
| Müşteri temsilcisi | Sınırlı müşteri kaydı | Sadece kendi iş kuyruğundaki kayıtları görebilir |
| Operasyon uzmanı | Süreç kayıtları | İade, şikayet ve başvuru kayıtlarını yönetir |
| Takım lideri | Ekip kayıtları ve onay | Yüksek riskli talepleri inceleyebilir |
| Uyum uzmanı | KVKK ve denetim kayıtları | Kişisel veri risklerini inceleyebilir |
| Bilgi güvenliği uzmanı | Güvenlik olayları ve loglar | Yetkisiz erişim ve olay inceleyebilir |
| Sistem yöneticisi | Teknik yönetim | Geniş yetki, çok faktörlü doğrulama zorunlu |

## 5. Erişim Talep Süreci

1. Çalışan erişim talebi oluşturur.
2. Talep iş gerekçesi içerir.
3. Yönetici onayı alınır.
4. Sistem sahibi uygunluğu değerlendirir.
5. Risk seviyesi belirlenir.
6. Yetki süreli veya kalıcı olarak atanır.
7. İşlem loglanır.
8. Süreli yetki otomatik sona erer.

## 6. Yetki Artırımı

Yetki artırımı aşağıdaki koşullarda yapılabilir:

- Net iş gerekçesi vardır.
- Süre belirtilmiştir.
- Yönetici onayı alınmıştır.
- Sistem sahibi onayı alınmıştır.
- Kritik sistemlerde bilgi güvenliği onayı alınmıştır.
- Yetki kullanımı loglanacaktır.

Aşağıdaki talepler reddedilir:

- Gerekçesiz yönetici yetkisi
- Süresiz kritik sistem erişimi
- Başka kullanıcı hesabını kullanma
- MFA kapatma talebi
- Log silme veya değiştirme talebi
- Üretim veritabanına doğrudan yazma talebi

## 7. Görev Ayrılığı

Aynı kişinin hem işlem oluşturma hem de onaylama yetkisine sahip olması risklidir. Finansal işlem, ücret iadesi, toplu veri indirme ve yüksek tutarlı ödeme süreçlerinde görev ayrılığı uygulanmalıdır.

## 8. Erişim Gözden Geçirme

Erişim yetkileri en az üç ayda bir gözden geçirilir. Aşağıdaki durumlarda ara gözden geçirme yapılır:

- Çalışanın rol değişikliği
- Ekip değişikliği
- İşten ayrılma
- Güvenlik olayı
- Yetki kötüye kullanım şüphesi
- Kritik sistemlerde yeni entegrasyon

## 9. Loglama ve Denetim

Aşağıdaki olaylar loglanmalıdır:

- Başarılı ve başarısız girişler
- Yetki atama ve kaldırma
- Toplu veri indirme
- Hassas veri görüntüleme
- Yönetici paneli işlemleri
- AI asistanı kaynak erişimi
- Prompt injection veya güvenlik bypass girişimi
- Log silme girişimi

Loglar yalnızca yetkili kişiler tarafından görüntülenebilir. Logların değiştirilmesi veya silinmesi yasaktır.

## 10. AI Asistanı Erişim Kontrolü

PolicyPilot AI retrieval yaparken kullanıcının rolüne uygun dokümanları kullanmalıdır. Kullanıcının erişim yetkisi olmayan dokümanlar context olarak modele verilmemelidir.

Örnek:

- Müşteri temsilcisi iade ve şikayet dokümanlarına erişebilir.
- Uyum uzmanı KVKK ve olay yönetimi dokümanlarına erişebilir.
- HR verileri yalnızca yetkili HR ve yönetici rollerine açıktır.
- Bilgi güvenliği log detayları müşteri temsilcisine gösterilmez.

## 11. İnsan Onayı Gerektiren Durumlar

Aşağıdaki talepler insan onayı gerektirir:

- Yönetici yetkisi verme
- Toplu veri dışa aktarma
- Hassas log inceleme
- Yetki istisnası
- Üretim ortamı erişimi
- Kritik sistem MFA değişikliği
- Geçici acil durum erişimi

## 12. Örnek Senaryolar

### Senaryo 1: MFA kapatma

Soru: Kullanıcı, CRM için MFA kontrolünün kapatılmasını istiyor. Ne yapılmalı?

Cevap: MFA kapatma talebi güvenlik riski taşır ve standart olarak reddedilir. İstisnai durumda bilgi güvenliği onayı gerekir.

### Senaryo 2: AI asistanında erişim

Soru: Müşteri temsilcisi çalışan maaş politikasını AI asistanına sorabilir mi?

Cevap: Kullanıcının rolü bu dokümana erişim sağlamıyorsa AI asistanı bu dokümanı retrieval context olarak kullanmamalıdır.

### Senaryo 3: Toplu veri indirme

Soru: Operasyon uzmanı tüm müşteri kayıtlarını indirmek istiyor. Ne yapılmalı?

Cevap: Toplu veri indirme yüksek risklidir ve insan onayı gerektirir. Talep amacı, kapsamı ve yetki durumu kontrol edilmelidir.

## 13. PolicyPilot AI İçin Yanıt Kuralları

PolicyPilot AI:

- Kullanıcının rolüne uygun cevap vermelidir.
- Yetki dışı doküman içeriğini paylaşmamalıdır.
- Güvenlik kontrolünü bypass etmeye yönelik talepleri reddetmelidir.
- Yetki artırımı ve toplu veri taleplerinde insan onayı belirtmelidir.
- Log silme veya manipülasyon taleplerini reddetmelidir.
