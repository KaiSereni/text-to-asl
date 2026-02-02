from src.text_to_asl.translate import sentence_to_video
import os

TEXT_FILE_NAME = "sentences_to_translate.txt"

with open(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ), 
        TEXT_FILE_NAME
    )
) as f:
    for line in f:
        sentence_to_video(line)