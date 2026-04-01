import os
from google import genai

# 1. Recupero la chiave segreta dalle impostazioni di GitHub
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API Key non trovata. Assicurati di averla salvata nei REPOSITORY SECRETS come 'GEMINI_API_KEY'.")

# 2. Inizializzo il nuovo client ufficiale Google GenAI
client = genai.Client(api_key=api_key)

# 3. Il Prompt: le istruzioni per l'IA
prompt = """
Scrivi un breve articolo da blog (circa 300 parole) su una curiosità tecnologica o informatica interessante. 
Restituisci l'output ESATTAMENTE in questo formato HTML, senza aggiungere altro testo prima o dopo:

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orvia.it - Notizie Tech</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 20px; color: #333; }
        h1 { color: #0056b3; }
        .data { color: #888; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>[INSERISCI QUI IL TITOLO DELL'ARTICOLO]</h1>
    <p class="data">[INSERISCI LA DATA DI OGGI]</p>
    <div>[INSERISCI QUI IL CORPO DELL'ARTICOLO IN PARAGRAFI HTML <p>]</div>
</body>
</html>
"""

print("Generazione articolo in corso con il nuovo SDK...")

# 4. Chiamo l'IA con la nuova sintassi
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)
html_content = response.text

# Pulisco l'output nel caso Gemini aggiunga i tag markdown
if html_content.startswith("```html"):
    html_content = html_content[7:]
if html_content.endswith("```"):
    html_content = html_content[:-3]

# 5. Salvo il risultato sovrascrivendo il file index.html
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content.strip())

print("File index.html aggiornato con successo!")
