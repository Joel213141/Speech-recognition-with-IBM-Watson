{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "561e1273",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ibm_watson import SpeechToTextV1\n",
    "from ibm_cloud_sdk_core.authenticators import IAMAuthenticator\n",
    "import json\n",
    "\n",
    "def authenticate_speech_to_text(api_key, url):\n",
    "    authenticator = IAMAuthenticator(api_key)\n",
    "    speech_to_text = SpeechToTextV1(authenticator=authenticator)\n",
    "    speech_to_text.set_service_url(url)\n",
    "    return speech_to_text\n",
    "\n",
    "def recognize_speech(file_path, stt_service):\n",
    "    with open(file_path, 'rb') as audio_file:\n",
    "        speech_recognition_results = stt_service.recognize(\n",
    "            audio=audio_file,\n",
    "            content_type='audio/wav'\n",
    "        ).get_result()\n",
    "        return speech_recognition_results\n",
    "\n",
    "def save_results(results, output_path):\n",
    "    with open(output_path, 'w') as outfile:\n",
    "        json.dump(results, outfile)\n",
    "\n",
    "# Example usage\n",
    "if __name__ == \"__main__\":\n",
    "    stt_service = authenticate_speech_to_text('{APIkey}', '{url}')\n",
    "    results = recognize_speech('path_to_audio_file.wav', stt_service)\n",
    "    save_results(results, 'output.json')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
