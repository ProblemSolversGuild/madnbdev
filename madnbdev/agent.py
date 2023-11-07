# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_API_Integration.ipynb.

# %% auto 0
__all__ = ['model_engine', 'Role', 'create_message', 'Speaker']

# %% ../nbs/02_API_Integration.ipynb 3
import datetime
import os
import openai
from fastcore.basics import store_attr
from fastcore.test import test_eq

# %% ../nbs/02_API_Integration.ipynb 4
openai.api_key = os.environ['OPENAI_API_KEY']
model_engine = "gpt-3.5-turbo"

# %% ../nbs/02_API_Integration.ipynb 5
from enum import Enum

# %% ../nbs/02_API_Integration.ipynb 6
class Role(Enum):
    "This corresponds to the roles that openai allows for the ChatGPT API"
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    FUNCTION = "function"

# %% ../nbs/02_API_Integration.ipynb 8
def create_message(role_type:Role, # Whether this message is the system, user, or assistant talking
                   content:str # A string that can be used 
                  ):
    return {"role":role_type.value, "content": content}

# %% ../nbs/02_API_Integration.ipynb 21
class Speaker:
    "A speaker is somebody that will talk about things!"
    def __init__(self, name:str, backstory:str=None, mannerisms:str=None, relationships:dict=None, model_engine="gpt-3.5-turbo"): # Test
        store_attr()
        self.messages=[]
        self.setup_backstory()
        self.setup_mannerisms()
        self.setup_universe()

    def setup_universe(self):
        # self.messages.append(create_message(Role.SYSTEM, f'you are one of a handful of members in an improv group in front of a live audience.'))
        self.messages.append(create_message(Role.SYSTEM, f'Your message should be no more than a paragraph'))
        self.messages.append(create_message(Role.SYSTEM, f'Responses should like like this YOUR_NAME: Response to the previous messages.'))
        self.messages.append(create_message(Role.SYSTEM, f'If needed you can do actions by putting them in asterisks'))
        self.messages.append(create_message(Role.SYSTEM, f'Use markdown to make the output look pretty'))
        self.messages.append(create_message(Role.SYSTEM, f'You can only write your own viewpoint of the story. Never write the other persons response'))
    
    def setup_backstory(self):
        if self.backstory is None:
            self.messages.append(create_message(Role.SYSTEM, f'Your name is {self.name}. Choose a random backstory and make sure to tell me the backstory at the top of the next message'))
        else:
            self.messages.append(create_message(Role.SYSTEM, f'Your name is {self.name} and here is your backstory: {self.backstory}'))

    def setup_mannerisms(self):
        if self.mannerisms is None:
            self.messages.append(create_message(Role.SYSTEM, f'Choose some random mannerisms and make sure to tell me what the mannerisms are at the top of the next message'))
        else:
            self.messages.append(create_message(Role.SYSTEM, f'Here are some of your mannerisms: {self.mannerisms}'))

    def setup_scene(self, scene:str):
        self.messages.append(create_message(Role.SYSTEM, scene))
        return "**SCENE PLOT: "+scene+"**"
    
    def listen_to_input(self,inp):
        self.messages.append(create_message(Role.USER, inp))

    def talk(self, max_tokens:int=300):
        completion = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=self.messages,
            max_tokens=max_tokens
        )
        self.messages.append(create_message(Role.ASSISTANT, completion.choices[0].message.content))
        return completion.choices[0].message.content
