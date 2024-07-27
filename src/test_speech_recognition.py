{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ce53c31",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from speech_to_text_api import authenticate_speech_to_text, recognize_speech, save_results\n",
    "\n",
    "def process_directory(directory_path, stt_service):\n",
    "    for filename in os.listdir(directory_path):\n",
    "        if filename.endswith(\".wav\"):\n",
    "            file_path = os.path.join(directory_path, filename)\n",
    "            results = recognize_speech(file_path, stt_service)\n",
    "            save_results(results, f\"results/{filename}.json\")\n",
    "\n",
    "# Example usage\n",
    "if __name__ == \"__main__\":\n",
    "    stt_service = authenticate_speech_to_text('{APIkey}', '{url}')\n",
    "    process_directory('data/SpeechtoTextData', stt_service)"
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
