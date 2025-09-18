# Text to ASL Python translator
Translates any text to a video of that text in ASL.

## This project is unique.
Projects like [sign.mt](https://sign.mt/) have created something similar, except sign.mt doesn't take into account the differing gramatical syntax that ASL uses. As far as I know, this is the first open-source project that convert text to video ASL with correct grammatical syntax. Essentially, this is the first working Google Translate for ASL.

## Quickstart
1. Clone the repo
2. cd into the repo
3. Run `python -m venv .venv`
4. `.venv/Scripts/activate` for Windows or `source .venv/bin/activate` for Mac
5. `pip install -r requirements.txt`
6. Go to `https://aistudio.google.com/` and create a Gemini API key
7. Create a `.env` file in the project root and add the line `GENAI_API_KEY=YOURKEY`
8. Edit the example strings in `sentences_to_translate.txt`
9. Run `python main.py`
10. Video goes to `out/video_title.mp4`

## How it works
Takes text as input -> Google Gemini converts the text's syntactical structure to that of ASL -> If there are any homonyns (words with multiple definitions/signs), Google Gemini clarifies which definition to use -> each sign is downloaded as a video from the SignASL database -> the videos are stitched together with MoviePy -> Saves output video

## Example
Input: `What time is it`</br>
Output: </br>
![What_time_is_it](https://github.com/user-attachments/assets/be1cc90b-1dd7-438e-838c-45c55f94d812)



Contributions welcome
