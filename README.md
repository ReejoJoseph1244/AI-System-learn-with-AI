# AI-System-learn-with-AI

Learn with AI is a AI system made using free ML environment, leveraging language models and ChatGPT APIs to extract insights from YouTube videos, and empowering yourself to learn faster and more efficiently like never before!

Usage : 
1. Get transcript
2. Translate the transcript to 30+ languages
3. Get Summary of the transcript using Hugging-face and ChatGPT.
4. Save 70% of watching the youtube video's.

## WorkFlow
![Workflow Diagram](https://github.com/ReejoJoseph1244/AI-System-learn-with-AI/assets/92742868/5cf33ffc-915e-4043-94f8-debc6f6e2d8c)

## Code Run (Ouput in SageMaker Lab)
1. Install and import all the Libraries required 
```
!pip install python-dotenv
!pip install openai
!pip install youtube_dl
!pip install youtube_transcript_api
!pip install torchaudio
!pip install sentencepiece
!pip install sacremoses
!pip install transformers
```

```
import re
from youtube_transcript_api import YouTubeTranscriptApi
import torch
import torchaudio
import openai
import textwrap
from transformers import pipeline
```

2. Getting the Transcript of the Youtube Video
   ![output1](https://github.com/ReejoJoseph1244/AI-System-learn-with-AI/assets/92742868/370e22e0-8407-4c01-8dd8-6be9a386dde5)   ![output2](https://github.com/ReejoJoseph1244/AI-System-learn-with-AI/assets/92742868/73f61004-4100-4cd4-9fb0-418b31c8435c)

The transcript obtain is of : 5403 Words, 26310 Characters

3. We can get the transcript converted to any language with the help of various ML models available in Hugging-face. remember to change the check point according to your preference language.
    ```
   model_checkpoint = "Helsinki-NLP/opus-mt-en-es"
   translator = pipeline("translation", model=model_checkpoint)
    ```
    ![ouput3](https://github.com/ReejoJoseph1244/AI-System-learn-with-AI/assets/92742868/c3a72fac-63c7-41ea-a1ac-0737b96fa21a)

    
4. Now Lets get the summary of the transcript obtained using Opensource ML models available in Hugging-Face.
   And the Summarized text has only 2259 Words ie Almost 50% summarized.


   ![ouput4](https://github.com/ReejoJoseph1244/AI-System-learn-with-AI/assets/92742868/e4b9cb28-390c-47f1-a661-46a32c37531e)

   


   
