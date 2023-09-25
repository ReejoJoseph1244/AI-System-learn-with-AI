#installing libraries

!pip install python-dotenv
!pip install openai
!pip install youtube_dl
!pip install youtube_transcript_api
!pip install torchaudio
!pip install sentencepiece
!pip install sacremoses
!pip install transformers

#importing dependencies

import re
from youtube_transcript_api import YouTubeTranscriptApi
import torch
import torchaudio
import openai
import textwrap
from transformers import pipeline, AutoTokenizer


# Specify the YouTube video URL
youtube_url = "https://www.youtube.com/watch?v=b9rs8yzpGYk"



def get_Transcript(youtube_url):
    # Extract the video ID from the URL using regular expressions
    match = re.search(r"v=([A-Za-z0-9_-]+)", youtube_url)
    if match:
        video_id = match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")
    
    # Get the transcript from YouTube
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Concatenate the transcript into a single string
    transcript_text=""
    for segment in transcript:
        transcript_text += segment["text"] + " "
    return transcript_text


    
# Replace this with your own checkpoint
model_checkpoint = "Helsinki-NLP/opus-mt-en-es"



def translate_Transcript(transcript_text,model_checkpoint):
    translator = pipeline("translation", model=model_checkpoint)
    # Define the maximum sequence length
    max_length = 512
    
    # Split the input text into smaller segments
    segments = [transcript_text[i:i+max_length] for i in range(0, len(transcript_text), max_length)]
    
    # Translate each segment and concatenate the results
    translated_text = ""
    for segment in segments:
        result = translator(segment)
        translated_text += result[0]['translation_text']
        
    return translated_text
    


def generate_Summary(transcript_text):
    # Instantiate the tokenizer and the summarization pipeline
    tokenizer = AutoTokenizer.from_pretrained('stevhliu/my_awesome_billsum_model')
    summarizer = pipeline("summarization", model='stevhliu/my_awesome_billsum_model', tokenizer=tokenizer)
    
    # Define chunk size in number of words
    chunk_size = 200 # you may need to adjust this value depending on the average length of your words
    
    # Split the text into chunks
    words = transcript_text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    
    # Summarize each chunk
    summaries = []
    for chunk in chunks:
        # Summarize the chunk
        summary = summarizer(chunk, max_length=100, min_length=30, do_sample=False)
        
        # Extract the summary text
        summary_text = summary[0]['summary_text']
        
        # Add the summary to our list of summaries
        summaries.append(summary_text)
        
    # Join the summaries back together into a single summary
    final_summary = ' '.join(summaries)
    
    return final_summary


transcript_text=get_Transcript(youtube_url)
print(transcript_text)

translated_text = translate_Transcript(transcript_text,model_checkpoint)
print(translated_text)

summary=generate_Summary(transcript_text)
print(summary)
