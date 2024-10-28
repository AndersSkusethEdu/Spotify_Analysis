# Spotify Track Analyse
Dette prosjektet lar deg analysere dine toppsanger på Spotify og visualisere features ved hjelp av Streamlit.

## Requirements
Python 3.7 eller høyere
Spotify Developer-konto


## Opprett og aktiver et virtuelt miljø:
python -m venv venv
source venv/bin/activate  # På Windows bruk `venv\Scripts\activate`

## Installer nødvendige pakker:
pip install -r requirements.txt

## Opprett en .env-fil i rotkatalogen og legg til dine Spotify API-legitimasjoner:
CLIENT_ID=ditt_spotify_client_id
CLIENT_SECRET=ditt_spotify_client_secret
Du kan få disse legitimasjonene ved å opprette en app på Spotify Developer Dashboard.

## Hovedbiblioteker brukt
spotipy: Python-bibliotek for Spotify Web API.
streamlit: Rammeverk for å lage interaktive webapplikasjoner.
pandas: Bibliotek for datamanipulering og analyse.
dotenv: Bibliotek for å laste miljøvariabler fra en .env-fil.

## Funksjoner
Topp Sanger Analyse-> Henter dine toppsanger fra Spotify.
Visualisering av Lydfunksjoner-> Viser et stolpediagram over lydfunksjoner som dansbarhet, energi og valens for dine toppsanger.

README produsert av CoPilot. 
