from typing import Literal

CHITCHAT_PHRASES = [
    "selam", "merhaba", "hey", "hi", "hello", "nasılsın", "naber", "ne haber",
    "günaydın", "iyi günler", "iyi akşamlar", "iyi geceler", "iyi çalışmalar",
    "kolay gelsin", "hayırlı işler", "ne yapıyorsun", "napıyorsun", "kimsin", 
    "sen kimsin", "teşekkür", "sağ ol", "sağol", "eyvallah", "tşk", "teşekkürler",
    "tamam", "anladım", "harika", "ok", "okay", "peki", "olur",
    "görüşürüz", "bay bay", "hoşça kal", "kendine iyi bak", "slm", "merhabalar",
    "yardım", "yardımcı ol", "yardım et"
]
# Daha sonra chitchat algılayıcı için bir model eğiteceğim.

IntentType = Literal["POLICY_QUERY", "CHITCHAT"]


def detect_intent(query: str) -> IntentType:
    """
    Returns:
        "CHITCHAT"    -> Sohbet mesajı, veritabanına gitmeye gerek yok.
        "POLICY_QUERY" -> Kurumsal soru, tam RAG pipeline'ı çalıştır.
    """
    normalized = query.lower().strip()
    
    for phrase in CHITCHAT_PHRASES:
        if phrase in normalized:
            return "CHITCHAT"
    
    if len(normalized.split()) <= 3 and not any(
        kw in normalized for kw in ["ne", "nasıl", "neden", "hangi", "kim", "ne zaman"]
    ):
        return "CHITCHAT"
    
    return "POLICY_QUERY"


CHITCHAT_RESPONSE = (
    "Merhaba! Ben **PolicyPilot AI** — şirketinizin kurumsal politika asistanıyım. 🛡️\n\n"
    "Aşağıdaki konularda size yardımcı olabilirim:\n"
    "- 📋 **Şirket Politikaları** (Erişim Kontrolü, Çalışan Güvenliği)\n"
    "- 🔒 **KVKK ve Veri Gizliliği** Kuralları\n"
    "- 📦 **İade, Şikayet ve Sigorta** Süreçleri\n"
    "- 🤖 **AI Asistan Kullanım Politikası**\n\n"
    "Hangi konuda bilgi almak istersiniz?"
)
