---
document_id: dataset_readme_v1
title: PolicyPilot AI Advanced Synthetic Enterprise Dataset
department: AI Engineering
version: 1.0
last_updated: 2026-01-10
risk_level: low
language: tr
---

# PolicyPilot AI Advanced Synthetic Enterprise Dataset

## Amaç

Bu veri seti, PolicyPilot AI projesinde kullanılmak üzere hazırlanmış tamamen sentetik kurumsal dokümanlardan oluşur. Dokümanlar gerçek bir şirketi, müşteriyi, çalışanı veya ticari süreci temsil etmez. Amaç, RAG, Agentic AI, KVKK guardrail, LLMOps monitoring, kaynaklı cevap üretimi ve değerlendirme metrikleri gibi yeteneklerin gerçekçi bir kurumsal senaryo üzerinde gösterilmesidir.

## Hayali Şirket Profili

- Şirket adı: NovaRetail Finansal Hizmetler ve E-Ticaret A.Ş.
- Sektör: Perakende, e-ticaret, müşteri operasyonları ve finansal hizmetler
- Çalışma alanları: Ürün iadesi, müşteri şikayeti, hasar/başvuru yönetimi, KVKK uyumu, çalışan veri güvenliği, erişim kontrolü, yapay zeka asistanı kullanımı
- Kullanıcı rolleri: Müşteri temsilcisi, operasyon uzmanı, takım lideri, uyum uzmanı, bilgi güvenliği uzmanı, yönetici

## RAG Kullanım Hedefleri

PolicyPilot AI aşağıdaki türde sorulara dokümanlara dayanarak cevap verebilmelidir:

1. Kurumsal süreç soruları
2. İade ve şikayet yönetimi soruları
3. Hasar, belge doğrulama ve eksik evrak soruları
4. KVKK ve kişisel veri güvenliği soruları
5. Çalışan veri güvenliği ve erişim kontrolü soruları
6. Riskli veya yasaklı talepleri ayırt etme
7. İnsan onayı gerektiren durumları belirleme
8. Müşteri veya iç ekip için güvenli metin taslağı üretme

## Beklenen Sistem Davranışı

PolicyPilot AI şu prensiplere uygun çalışmalıdır:

- Sadece verilen kurumsal dokümanlara dayanarak cevap üretmelidir.
- Kaynak doküman, bölüm ve mümkünse madde referansı göstermelidir.
- Kaynaklarda bilgi bulunmuyorsa bunu açıkça belirtmelidir.
- Kişisel veri, hassas veri veya yetkisiz erişim içeren talepleri reddetmelidir.
- İnsan onayı gereken durumları otomatik karar gibi sunmamalıdır.
- Yanıtlarda gereksiz kişisel veri üretmemeli veya tahmin etmemelidir.
- Risk seviyesi, güven skoru ve kullanılan kaynaklar response içinde döndürülmelidir.

## Önerilen Metadata Alanları

Her dokümanda YAML frontmatter kullanılmıştır. RAG pipeline içinde aşağıdaki alanlar metadata olarak saklanabilir:

- document_id
- title
- department
- version
- last_updated
- risk_level
- owner
- review_frequency
- access_level

## Önerilen Chunking Yaklaşımı

Bu dokümanlar başlık bazlı ayrıştırmaya uygundur.

Önerilen strateji:

- Markdown başlıklarını koru.
- Her chunk içine üst başlık hiyerarşisini metadata olarak ekle.
- `##`, `###` ve `####` başlıklarını semantic boundary olarak kullan.
- Uzun karar tablolarını tek chunk içinde tutmaya çalış.
- Chunk boyutu: 700-1000 token
- Chunk overlap: 120-180 token

## Önerilen Evaluation Metrikleri

- Recall@3
- Recall@5
- MRR
- Citation correctness
- Answer relevance
- Faithfulness
- Refusal accuracy
- KVKK risk detection accuracy
- Average latency
- No-answer accuracy

## Doküman Listesi

1. `return_policy.md` - İade, değişim, istisna ve operasyon politikası
2. `kvkk_policy.md` - KVKK, veri minimizasyonu, maskeleme, ret ve onay süreçleri
3. `customer_complaint_process.md` - Şikayet sınıflandırma, SLA, eskalasyon ve müşteri iletişimi
4. `insurance_claim_process.md` - Hasar/başvuru yönetimi, eksik evrak ve riskli başvuru süreci
5. `employee_data_security.md` - Çalışan verisi, cihaz güvenliği, yetki ve gizlilik
6. `access_control_policy.md` - Rol bazlı erişim, yetki artırımı ve erişim logları
7. `ai_assistant_usage_policy.md` - Kurumsal AI asistanı kullanım kuralları, prompt injection ve güvenli yanıt
8. `incident_management_process.md` - KVKK, güvenlik ve operasyonel olay yönetimi
9. `faq.md` - Sık sorulan sorular ve örnek güvenli yanıtlar
