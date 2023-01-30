from transformers import pipeline

def summarize(text):
    summarizer=pipeline('summarization', model='t5-base')
    summary = summarizer(text, max_length=500, min_length=30,  do_sample=False)[0]['summary_text']
    return summary