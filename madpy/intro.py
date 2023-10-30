# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_introduction.ipynb.

# %% auto 0
__all__ = ['arrange_talk']

# %% ../nbs/00_introduction.ipynb 14
import datetime

# %% ../nbs/00_introduction.ipynb 16
def arrange_talk(speaker:str, # The name of the speaker
                 title:str, # The title of the talk that will be given
                 talk_date:datetime.date=datetime.date.today() # The date that the speaker will be giving the talk
                ) -> str: # The output is a string that gives a human readable output of the information provided
    return f"{speaker} will be talking about {title} on {talk_date}"
