from screenplay_analysis import ScreenplayAnalysis
import boto3

class VoiceCasting:
    def __init__(self, aws_access_key="your-aws-access-key", aws_secret_key="your-aws-secret-key"):
        self.screenplay_analysis = ScreenplayAnalysis()
        self.polly = boto3.client("polly", region_name="us-west-2", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    
    def cast(self, screenplay):
        analysis = self.screenplay_analysis.analyze()
        dialogues = analysis["dialogues"]
        
        voice_casts = []
        for dialogue in dialogues:
            speaker = dialogue["speaker"]
            utterance = dialogue["utterance"]
            response = self.polly.synthesize_speech(Engine="standard", OutputFormat="mp3", Text=utterance)
            voice_casts.append((speaker, response['AudioStream']))
        
        return voice_casts
