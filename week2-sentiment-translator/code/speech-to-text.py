import azure.cognitiveservices.speech as speechsdk
from config import SPEECH_KEY, SPEECH_REGION    

speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
output_file = "transcribed.txt"
audio_file = "../assets/output.wav"

speech_config.speech_recognition_language="en-US"
text_generator = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=speechsdk.audio.AudioConfig(filename=audio_file))

audio_output = speechsdk.audio.AudioConfig(filename=output_file)
speech_generator = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output)

result = text_generator.recognize_once_async().get()
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognition succeeded.")
    print("Recognized text: {}".format(result.text))    
else:
    print("Speech Recognition canceled: {}".format(result.cancellation_details.reason))
    if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(result.cancellation_details.error_details))
        print("Did you set the speech resource key and region values?")    

with open(output_file, "w") as f:
    f.write(result.text)        

