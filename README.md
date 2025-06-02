# Regluagent HSÍ 🤾‍♂️

Þetta app les úr PDF-skrá með reglugerð HSÍ um handknattleiksmót og svarar spurningum á íslensku. 
Notendur geta spurt um leikreglur, viðurlög, aldursflokka o.fl.

🚀 Keyrt með: Streamlit + GPT-4 eða GPT-3.5 + PDF reglugerð

## Notkun
1. Spyrðu spurningu um reglugerðina
2. Appið notar OpenAI API til að svara út frá PDF skjalinu

## Keyrsla (staðbundið)
```bash
pip install -r requirements.txt
streamlit run hsi_agent_app.py
```

## Hýsing
Hægt er að hýsa appið á [streamlit.io/cloud](https://streamlit.io/cloud) 
og skilgreina API-lykil sem Secret (`OPENAI_API_KEY`)
