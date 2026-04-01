import os
from datetime import datetime
from google import genai

# 1. Recupero la chiave segreta
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key non trovata. Controlla i GitHub Secrets.")

client = genai.Client(api_key=api_key)

# 2. Genero un marcatore temporale univoco spaccato al secondo
timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# 3. Il Prompt corazzato con f-string (nota le parentesi graffe)
prompt = f"""
Scrivi un articolo da blog (circa 300-400 parole) dedicato al mondo dei giochi per bambini. 
Scegli ogni volta un argomento specifico diverso: un gioco all'aperto, un'attività in casa o consigli educativi.
Il tono deve essere caldo, coinvolgente e rassicurante per genitori e nonni.
Oggi è il {timestamp}. Menziona o sfrutta questa giornata.

Restituisci l'output ESATTAMENTE in questo formato HTML, senza aggiungere markdown o altro testo:

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orvia.it - Il Mondo dei Bambini</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; }}
        .container {{ max-width: 800px; margin: 40px auto; background: #ffffff; padding: 30px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); border-top: 5px solid #ff9f43; }}
        h1 {{ color: #ff9f43; font-size: 2.2em; margin-bottom: 5px; line-height: 1.2; }}
        h2 {{ color: #0abde3; margin-top: 30px; }}
        .data {{ color: #888; font-size: 0.9em; font-style: italic; margin-bottom: 20px; display: block; }}
        p {{ font-size: 1.1em; }}
        ul {{ font-size: 1.1em; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>[INSERISCI QUI UN TITOLO CREATIVO]</h1>
        <span class="data">Articolo generato il: {timestamp}</span>
        <div>
            [INSERISCI QUI IL CORPO DELL'ARTICOLO CON I PARAGRAFI]
        </div>
    </div>
    </body>
</html>
"""

print(f"Generazione articolo avviata alle {timestamp}...")

# 4. Chiamata all'IA
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)
html_content = response.text

# 5. Pulizia e Salvataggio
if html_content.startswith("```html"):
    html_content = html_content[7:]
if html_content.endswith("```"):
    html_content = html_content[:-3]

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content.strip())

print("File index.html aggiornato e pronto per il salvataggio!")
