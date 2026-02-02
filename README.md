# Text to ASL Python translator
Translates any text to a video of that text in ASL.

## This project is unique.
Projects like [sign.mt](https://sign.mt/) have created something similar, except sign.mt doesn't take into account the differing gramatical syntax that ASL uses. As far as I know, this is the first open-source project that convert text to video ASL with correct grammatical syntax. Essentially, this is the first working Google Translate for ASL.

## Quickstart
1. **Install the package**

`pip install git+https://github.com/KaiSereni/text-to-asl#egg=text_to_asl`

2. **API Keys**

Create a [Google Gemini API](https://aistudio.google.com/api-keys) token and add it to a `GEMINI_KEY` property in your .env file
```env
GEMINI_KEY=yourkeyhere
```

3. Use the package

Check out [translations.py](tests/translations.py) in the `tests` directory for an example usage
    

## How it works
Takes text as input -> Google Gemini converts the text's syntactical structure to that of ASL -> If there are any homonyns (words with multiple definitions/signs), Google Gemini clarifies which definition to use -> each sign is downloaded as a video from the SignASL database -> the videos are stitched together with MoviePy -> Saves output video

## Example
Input: `What time is it`</br>
Output: </br>
![What_time_is_it](https://github.com/user-attachments/assets/be1cc90b-1dd7-438e-838c-45c55f94d812)



Contributions welcome
