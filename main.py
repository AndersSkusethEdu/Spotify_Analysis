import spotipy
from spotipy.oauth2 import SpotifyOAuth
import streamlit as st
import pandas as pd
import os 


CLIENT_ID = os.environ.get ('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIEND_ID')
REDIRECT_URI = 'http://localhost:5000'