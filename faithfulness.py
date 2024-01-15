"""

    The function takes two major parameters:
    - ref_data: The reference text or ground truth.
    - generated_data: The generated text to be evaluated.

    The function returns a faithfulness score between 0 and 1, where 1 indicates high faithfulness.
    """

from difflib import SequenceMatcher

def evaulate_quality(ref_data, generated_data):
    f_score = SequenceMatcher(None, ref_data, generated_data).ratio()

    return f_score

if __name__ == "__main__":
    # Example usage
    reference = "Ayodhya temple Pran Pratishtha to be done on 22nd Jan 2023"
    generated = "Ayodhya temple Pran Pratishtha to be done on 22nd Jan 2023"

    score = evaulate_quality(reference, generated)
    print(f"Faithfulness Score: {score}")


