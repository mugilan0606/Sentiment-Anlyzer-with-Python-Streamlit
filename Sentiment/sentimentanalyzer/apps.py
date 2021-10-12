from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class SentimentanalyzerConfig(AppConfig):
    path=os.path.join(settings.MODELS,'models.p')

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentimentanalyzer'

    with open(path, 'rb') as pickled:
        data=pickle.load(pickled)
    mn=data['mn']
    cv=data['cv']
