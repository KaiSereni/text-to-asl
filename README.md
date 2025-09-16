# text-to-asl
Translates any text to a video of that text in ASL.

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

Contributions welcome
