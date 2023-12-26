import os
from screenplay_analysis import ScreenplayAnalysis
from voice_casting import VoiceCasting

class Main:
    def __init__(self, screenplay):
        self.screenplay = screenplay
        self.screenplay_analysis = ScreenplayAnalysis(self.screenplay)
        self.voice_casting = VoiceCasting()

    def main(self):
        analysis = self.screenplay_analysis.analyze(self.screenplay)
        voice_casts = self.voice_casting.cast(self.screenplay, analysis)
        return voice_casts

if __name__ == "__main__":
    # Set default values for AWS access key and secret key
    AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY", "your-aws-access-key")
    AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY", "your-aws-secret-key")
    
    # Initialize Main class with sample screenplay data
    main = Main({
        "text": "Once upon a time in a small village, there lived a boy named Jack and his sister Jill. One day, they decided to climb up the hill behind their house. As they reached the top of the hill, Jill saw something shiny on the ground. She ran towards it and picked it up. To her surprise, it was a magic lamp!"
    })
    
    # Call main function to process screenplay data
    voice_casts = main.main()
    
    # Print voice casts generated for characters in the screenplay
    print(f"Voice Casts:\n{voice_casts}")
