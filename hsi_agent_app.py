import streamlit as st
import fitz  # PyMuPDF
import os
from openai import OpenAI
from openai import RateLimitError, AuthenticationError, APIConnectionError, OpenAIError

# 🌍 API viðskiptavinur
client = OpenAI()

def lesa_pdf_texta(path):
    doc = fitz.open(path)
    return "\n".join([page.get_text() for page in doc])

@st.cache_data(show_spinner=False)
def hlaða_skjal():
    return lesa_pdf_texta("Reglugerd-HSI-um-Handknattleiksmot-vor-2025.pdf")

def svara_spurningu(texti, spurning):
    prompt = f"""
    Þú ert regluvörður í handknattleik. Ég mun gefa þér reglugerð HSÍ og þú svarar spurningum íslenskra notenda nákvæmlega 
    eftir reglugerðinni og nefnir númer greinar ef ætla má.

    Reglugerð:
    {texti[:4000]}...

    Spurning: {spurning}

    Svar: 
    """
    try:
        sv = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return sv.choices[0].message.content.strip()

    except RateLimitError:
        return "⚠️ Villuupplýsingar: OpenAI takmarkaði aðgang. Gakktu úr skugga um að API-lykillinn sé virkur og með heimild (greiðslumáta)."
    except AuthenticationError:
        return "❌ Villa: API lykillinn virðist vera ógildur eða ekki rétt skilgreindur í Streamlit Secrets."
    except APIConnectionError:
        return "🔌 Tengivilla: Get ekki tengst OpenAI. Reyndu aftur síðar."
    except OpenAIError as e:
        return f"⚠️ Óvænt villa frá OpenAI: {str(e)}"

# 🏠 Streamlit UI
st.set_page_config(page_title="HSÍ Regluagent", page_icon="⚽")
st.title("📄 Regluagent HSÍ")
st.markdown("Spurðu um reglugerð HSÍ um handknattleiksmót vor 2025.")

texti = hlaða_skjal()

spurning = st.text_input("💬 Hver er spurningin þín?")

if st.button("Senda") and spurning:
    med_svari = svara_spurningu(texti, spurning)
    st.markdown("---")
    st.markdown(f"**Svar:**\n\n{med_svari}")
