from textblob import TextBlob

print("AI Mood Analyzer")
print("----------------")

text = input("Enter a sentence: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity

if polarity > 0:
    print("Positive Mood 😊")
elif polarity < 0:
    print("Negative Mood 😔")
else:
    print("Neutral Mood 😐")