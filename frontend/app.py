import streamlit as st
import requests

st.set_page_config(
    page_title="PolicyPilot AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
    }
    h1 {
        color: #FFFFFF;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    .stChatMessage {
        border-radius: 12px;
        padding: 10px 15px;
        margin-bottom: 15px;
    }
    .citation-box {
        background-color: #1E2329;
        border-left: 4px solid #58A6FF;
        padding: 12px;
        border-radius: 6px;
        margin-top: 10px;
        font-size: 0.9em;
        color: #C9D1D9;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    section[data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #2D333B;
    }
</style>
""", unsafe_allow_html=True)

API_URL = "http://localhost:8000/api"

def get_documents():
    try:
        response = requests.get(f"{API_URL}/documents")
        if response.status_code == 200:
            return response.json().get("documents", [])
    except Exception:
        pass
    return []

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3024/3024310.png", width=80)
    st.title("PolicyPilot AI")
    st.markdown("*Kurumsal RAG Asistanı*")
    st.divider()
    
    st.subheader("📚 Sistemdeki Dokümanlar")
    docs = get_documents()
    if docs:
        for doc in docs:
            st.markdown(f"- 📄 `{doc}`")
    else:
        st.warning("⚠️ API'ye ulaşılamıyor veya doküman yok. Lütfen Backend'i çalıştırın.")
        
    st.divider()
    st.markdown("💡 **Nasıl Kullanılır?**\nSağ taraftan kurumsal politikalar, IK kuralları ve KVKK süreçleri hakkında dilediğinizi sorabilirsiniz.")
    st.markdown("🎯 *Qwen2.5-7B & ChromaDB destekli.*")

st.title("🛡️ PolicyPilot AI Asistan")
st.markdown("Merhabalar! Şirket politikaları hakkında size nasıl yardımcı olabilirim?")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "citations" in message and message["citations"]:
            with st.expander("🔍 Kullanılan Kaynakları Gör"):
                for cite in message["citations"]:
                    st.markdown(
                        f"<div class='citation-box'>"
                        f"<b>📄 Doküman:</b> {cite['doc']}<br>"
                        f"<b>🧩 Parça Büyüklüğü:</b> {cite['size']} karakter"
                        f"</div>", 
                        unsafe_allow_html=True
                    )

if prompt := st.chat_input("Örn: Çalışanların kişisel verileri nasıl korunuyor?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("Dokümanlar taranıyor ve analiz ediliyor..."):
            try:
                payload = {"query": prompt, "n_results": 3}
                response = requests.post(f"{API_URL}/query", json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("answer", "Cevap üretilemedi.")
                    results = data.get("results", [])
                    
                    message_placeholder.markdown(answer)
                    
                    citations = []
                    if results:
                        with st.expander("🔍 Kullanılan Kaynakları Gör"):
                            for res in results:
                                meta = res.get("metadata", {})
                                doc_name = meta.get("document_name", "Bilinmeyen Doküman")
                                chunk_size = meta.get("chunk_size", 0)
                                
                                st.markdown(
                                    f"<div class='citation-box'>"
                                    f"<b>📄 Doküman:</b> {doc_name}<br>"
                                    f"<b>🧩 Parça Büyüklüğü:</b> {chunk_size} karakter"
                                    f"</div>", 
                                    unsafe_allow_html=True
                                )
                                citations.append({"doc": doc_name, "size": chunk_size})
                                
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": answer, 
                        "citations": citations
                    })
                else:
                    st.error(f"API Hatası: {response.status_code}")
            except Exception as e:
                st.error("🚨 Bağlantı hatası! Lütfen ayrı bir terminalde Backend (FastAPI) sunucusunun çalıştığından emin olun.")
