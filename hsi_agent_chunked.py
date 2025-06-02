import streamlit as st
import fitz  # PyMuPDF
import os
from openai import OpenAI
from openai import OpenAIError
import textwrap

# 📘 PDF lestur og skipting í bita
def lesa_pdf_i_butum(path, max_chars=1500):
    doc = fitz.open(path)
    texti = "\n".join([page.get_text() for page in doc])
    return textwrap.wrap(texti, width=max_chars, break_long_words=False, break_on_hyphens=False)

# 🔍 Finna líklegasta bút út frá spurningu
def finna_videigandi_but(spurning, butar):
    client = OpenAI()
    samanburdur = []
    for i, butur in enumerate(butar):
        prompt = f"Hversu vel tengist eftirfarandi textabútur spurningunni \"{spurning}\"?\n\nTexti:\n{butur}\n\nGefðu svar á kvarðanum 0-10."
        try:
            sv = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0
            )
            svar = sv.choices[0].message.content.strip()
            score = int([int(s) for s in svar if s.isdigit()][0])
            samanburdur.append((score, i))
        except:
            samanburdur.append((0, i))
    samanburdur.sort(reverse=True)
    bestu_butar = [butar[i] for _, i in samanburdur[:2]]
    return "\n\n".join(bestu_butar)

# 🤖 Svara með GPT út frá viðeigandi texta
def svara_spurningu(spurning, viðeigandi_texti):
    client = OpenAI()
    prompt = f"""
    Þú ert regluvörður í handknattleik. Hér er hluti úr reglugerð HSÍ sem gæti átt við spurninguna. 
    Svaraðu skýrt, nákvæmlega og nefndu grein ef við á.

    Reglugerðartexti:
    {viðeigandi_texti}

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
    except OpenAIError as e:
        return f"Villa: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="HSÍ Regluagent – nákvæmari útgáfa", page_icon="📘")
st.title("📘 Regluagent HSÍ – nákvæmari útgáfa")
st.markdown("Spurðu út frá reglugerð HSÍ – og fáðu betra svar.")

@st.cache_data
def hlaða_butum():
    return lesa_pdf_i_butum("Reglugerd-HSI-um-Handknattleiksmot-vor-2025.pdf")

butar = hlaða_butum()

spurning = st.text_input("💬 Spurning:")

if st.button("Senda") and spurning:
    vid_texti = finna_videigandi_but(spurning, butar)
    svar = svara_spurningu(spurning, vid_texti)
    st.markdown("---")
    st.markdown(f"**Svar:**\n\n{svar}")
