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
    def __init__(self, model_name: str = "Qwen/Qwen2.5-72B-Instruct"):
        self.model_name = model_name
        self.token = os.getenv("HF_TOKEN")
        self.client = InferenceClient(token=self.token)

    def generate_answer(self, query: str, context_chunks: List[str]) -> str:
        if not self.token:
            return "Error: HF_TOKEN is missing. Please add your Hugging Face token to the .env file."

        context_text = "\n\n---\n\n".join(context_chunks)

        system_prompt = (
            "Sen PolicyPilot-AI adinda bir yardimci asistansin. "
            "SADECE sana verilen politika dokumanlarina dayanarak cevap ver. "
            "Her zaman Turkce cevap ver. "
            "Cevabini kisa ve ozetleyerek ver. "
            "Eger cevap dokumanlarda yoksa 'Bu bilgi mevcut dokumanlarda bulunamadi.' de. "
            "Asla uydurma bilgi verme. "
            "Sadece tek bir cevap ver, ek soru uretme veya devam etme."
        )

        user_prompt = f"DOKUMANLAR:\n{context_text}\n\nKULLANICI SORUSU:\n{query}"

        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
            response = self.client.chat_completion(
                messages, model=self.model_name, max_tokens=300, temperature=0.2
            )
            answer = response.choices[0].message.content.strip()

            stop_markers = ["USER QUESTION:", "KULLANICI SORUSU:", "[/USER]", "[/INST]", "USER:", "DOKUMANLAR:"]
            for marker in stop_markers:
                if marker in answer:
                    answer = answer.split(marker)[0].strip()

            return answer
        except Exception as e:
            return f"Error generating answer: {str(e)}"
