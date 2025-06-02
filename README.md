# Regluagent HSÍ 🤾‍♂️

Þetta app les úr PDF-skrá með reglugerð HSÍ um handknattleiksmót og svarar spurningum á íslensku. 
Notendur geta spurt um leikreglur, viðurlög, aldursflokka o.fl.

🚀 Keyrt með: Streamlit + GPT-4 + PDF reglugerð

## Notkun
1. Spyrðu spurningu um reglugerðina
2. Appið notar GPT-4 til að svara nákvæmlega út frá PDF reglugerðinni

## Keyrsla (staðbundið)
```bash
pip install -r requirements.txt
streamlit run hsi_agent_app.py
```

## Hýsing
Hægt er að hýsa appið ókeypis á [streamlit.io/cloud](https://streamlit.io/cloud) 
og vista API lykil sem secret (`OPENAI_API_KEY`).
