# 3. Il Prompt: le istruzioni per l'IA
prompt = """
Scrivi un articolo da blog (circa 300-400 parole) dedicato al mondo dei giochi per bambini. 
Scegli ogni volta un argomento specifico diverso: potrebbe essere un gioco tradizionale all'aperto da riscoprire, un'attività creativa o educativa da fare in casa nei giorni di pioggia, o una riflessione sull'importanza del gioco per lo sviluppo cognitivo e motorio.
Il tono di voce deve essere caldo, coinvolgente, rassicurante e molto utile per genitori, nonni o educatori.
Restituisci l'output ESATTAMENTE in questo formato HTML, senza aggiungere altro testo o tag markdown prima o dopo:

<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Orvia.it - Il Mondo dei Bambini</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; background-color: #f4f7f6; color: #333; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 40px auto; background: #ffffff; padding: 30px; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.05); border-top: 5px solid #ff9f43; }
        h1 { color: #ff9f43; font-size: 2.2em; margin-bottom: 5px; line-height: 1.2; }
        h2 { color: #0abde3; margin-top: 30px; }
        .data { color: #888; font-size: 0.9em; font-style: italic; margin-bottom: 20px; display: block; }
        p { font-size: 1.1em; }
        ul { font-size: 1.1em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>[INSERISCI QUI UN TITOLO CREATIVO E ACCATTIVANTE]</h1>
        <span class="data">Pubblicato il: [INSERISCI LA DATA DI OGGI]</span>
        <div>
            [INSERISCI QUI IL CORPO DELL'ARTICOLO IN PARAGRAFI HTML <p>. Usa i tag <h2> per dividere in paragrafi e <ul> per eventuali liste di materiali o regole del gioco]
        </div>
    </div>
</body>
</html>
"""
