import time


def stream_text(text, delay=0.05):
    for word in text.split():
        yield word + " "
        time.sleep(delay)
