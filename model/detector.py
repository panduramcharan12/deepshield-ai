import random

def detect_deepfake(image_path):

    prediction = random.choice([
        "Real",
        "Fake"
    ])

    confidence = round(
        random.uniform(80, 99),
        2
    )

    return prediction, confidence
