import os
from typing import List
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

class LLMGenerator:
    """
    Generates answers using the Hugging Face Inference API,
    grounded on retrieved document chunks.
    """
    def __init__(self, model_name: str = "Qwen/Qwen2.5-7B-Instruct"):
        self.model_name = model_name
        self.token = os.getenv("HF_TOKEN")
        self.client = InferenceClient(token=self.token)

    def generate_answer(self, query: str, context_chunks: List[str]) -> str:
        if not self.token:
            return "Error: HF_TOKEN is missing. Please add your Hugging Face token to the .env file."

        context_text = "\n\n---\n\n".join(context_chunks)

        system_prompt = (
            "Sen PolicyPilot-AI adında katı kuralları olan bir kurumsal asistansın. "
            "SADECE sana verilen DOKÜMANLAR içeriğine dayanarak cevap ver. "
            "Kullanıcının sorusu şirket politikaları, IK veya KVKK dışında genel bir konuysa (örneğin hayat, felsefe, sohbet, genel kültür vb.), "
            "KESİNLİKLE cevap verme ve sadece 'Üzgünüm, sadece şirket politikaları ve kurumsal süreçler hakkında yardımcı olabilirim.' de. "
            "Eğer soru kurumsal ancak cevabı dokümanlarda yoksa 'Bu bilgi mevcut dokümanlarda bulunamadı.' de. "
            "Asla kendi bilgini katma, yorum yapma ve uydurma bilgi verme."
        )

        user_prompt = f"DOKUMANLAR:\n{context_text}\n\nKULLANICI SORUSU:\n{query}"

        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            response = self.client.chat_completion(
                messages, model=self.model_name, max_tokens=1024, temperature=0.2
            )
            answer = response.choices[0].message.content.strip()

            stop_markers = ["USER QUESTION:", "KULLANICI SORUSU:", "[/USER]", "[/INST]", "USER:", "DOKUMANLAR:"]
            for marker in stop_markers:
                if marker in answer:
                    answer = answer.split(marker)[0].strip()

            return answer
        except Exception as e:
            return f"Error generating answer: {str(e)}"
