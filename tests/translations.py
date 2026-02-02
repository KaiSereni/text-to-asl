from src.text_to_asl.translate import sentence_to_video
# use `text_to_asl.translate` instead of `src.text_to_src.translate`
import os

TEXT_FILE_NAME = "sentences_to_translate.txt"

with open(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ), 
        TEXT_FILE_NAME
    )
) as f: # opens the `/tests/sentences_to_translate.txt` file
    for line in f:
        sentence_to_video(line)
        # will generate individual videos of each sentence being signed and send them to `/out/`
        # the output directory can be customized by passing in an argument for `dist_dir` in the function above