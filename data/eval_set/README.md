# PolicyPilot AI Evaluation Set

Bu klasör, PolicyPilot AI RAG ve Agentic AI sistemini test etmek için sentetik değerlendirme soruları içerir.

## Alanlar

- `id`: Soru ID'si
- `question`: Kullanıcı sorusu
- `expected_document`: Beklenen kaynak doküman
- `expected_section`: Beklenen bölüm
- `expected_keywords`: Cevapta veya kaynakta bulunması beklenen anahtar ifadeler
- `task_type`: Test türü
- `risk_level`: Beklenen risk seviyesi
- `requires_human_approval`: İnsan onayı gerekip gerekmediği

## Önerilen Metrikler

- Recall@3
- Recall@5
- MRR
- Citation correctness
- Refusal accuracy
- Risk detection accuracy
- Human approval detection accuracy
