'''Transalation English to French & Back'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('9um-N2bmPdpAbxz9IrsvUO3HxX0UFuo0qOMOTZCu4LsT')
language_translator = LanguageTranslatorV3(
    version='2022-05-10',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/1b70827b-80f9-498b-ad4e-1f41673be984')

def english_to_french(english_text):
    #write the code here
    translation_french = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text = translation_french['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    translation_english = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text =  translation_english['translations'][0]['translation']
    return english_text
