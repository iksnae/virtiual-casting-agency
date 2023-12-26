import nltk
from data_structures_and_interfaces import NlpEngine
from voice_casting import VoiceCasting

class ScreenplayAnalysis:
    def __init__(self, screenplay):
        self.screenplay = screenplay
        self.nlp_engine = NlpEngine()

    def analyze(self) -> dict:
        # Process the screenplay using NLP techniques
        analysis = self.nlp_engine.process(self.screenplay["text"])
        
        # Generate character analysis
        character_analysis = self.character_analysis()
        
        return {
            "characters": character_analysis,
            "locations": self.location_analysis(),
            "scenes": self.scene_analysis(),
            "dialogues": self.dialogue_analysis()
        }

    def character_analysis(self) -> dict:
        # Extract and analyze characters from the screenplay
        return {
            "characters": [
                {
                    "name": char[0],
                    "roles": self.get_roles(char[1]),
                }
                for char in analysis if char[1] != "NNP"
            ]
        }

    def location_analysis(self) -> dict:
        # Extract and analyze locations from the screenplay
        return {
            "locations": [loc for loc, _type in analysis if "NNP" in _type]
        }

    def scene_analysis(self) -> dict:
        # Extract and analyze scenes from the screenplay
        return {
            "scenes": [scene for scene, _type in analysis if "VB" in _type or "IN" in _type]
        }

    def dialogue_analysis(self) -> dict:
        # Extract and analyze dialogues from the screenplay
        return {
            "dialogues": [
                {
                    "speaker": speaker,
                    "utterance": utterance
                }
                for speaker, _type in analysis if "NNP" in _type or "NNPS" in _type
            ]
        }

    def get_roles(self, part_of_speech: str) -> list[str]:
        # Extract roles for each character based on their part of speech
        roles = []
        if "JJR" in part_of_speech or "RBR" in part_of_speech:
            roles.append("Adjective")
        elif "NNP" in part_of_speech or "NNPS" in part_of_speech:
            roles.append("Proper noun")
        return roles
