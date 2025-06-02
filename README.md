# Regluagent HSÍ (LangChain útgáfa)

Þetta Streamlit app notar FAISS + OpenAI til að svara spurningum úr PDF reglugerð HSÍ.

## 🔧 Keyrsla í fyrsta sinn (staðbundið)

```bash
pip install -r requirements.txt
python generate_index.py       # Býr til FAISS gagnagrunn
streamlit run hsi_agent_langchain.py
```

## 📁 Skrár

- `hsi_agent_langchain.py`: Streamlit forritið
- `generate_index.py`: Skrá sem býr til `hsi_faiss_index/` úr PDF skránni
- `Reglugerd-HSI-um-Handknattleiksmot-vor-2025.pdf`: PDF reglugerð
- `requirements.txt`: Pakkar sem þarf

## 💡 Notkun í Streamlit Cloud

1. Bættu þessum skrám við GitHub repo
2. Deploy appið með `hsi_agent_langchain.py` sem main file
3. Geymslan byggir sjálfkrafa `hsi_faiss_index` ef hún er ekki til
