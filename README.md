# SmartSvar

**SmartSvar** er et verktøy som hjelper deg med å skrive meldinger når du er usikker på hva du skal svare. Prosjektet består av en nettside med tilpassede svarforslag basert på mottaker, tone og lengde.

---

## Funksjoner

- Lim inn meldingen du har fått.
- Velg hvem meldingen er fra (kjæreste, venn, forelder osv.).
- Velg tonen i svaret (romantisk, morsomt, seriøst, formelt osv.).
- Velg lengden på svaret (kort, middels eller lang).
- Generer et forslag til svar.
- Få flere alternative forslag om ønskelig.

---

## Teknologi brukt

- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Database:** MariaDB
- **Miljø:** `.env` for sensitive variabler som databasebruker og passord

---

## Komme i gang

```bash
git clone <repository-url>
cd smartsvar
pip install -r requirements.txt
echo USER=brukernavn >> .env
echo PASSWORD=passord >> .env
python app.py
```

Åpne nettleseren og gå til:

```
http://127.0.0.1:5000/
```

## Database

- Prosjektet bruker MariaDB. Tabellen prompts lagrer meldingene og forslagene. Databasekoblingen finnes i database.py.

## Bruk

- Start nettsiden.

- Skriv meldingen du har mottatt.

- Velg hvem du skriver til, tone og lengde.

- Klikk på "Generer svar" for å få forslag.

# Design

Se vårt design i Figma her: [SmartSvar Design](https://www.figma.com/design/pP94rviMLn1bzxgkIvEYAa/Untitled?node-id=0-1&t=aMrNqeQt2NEbvUWQ-1).
