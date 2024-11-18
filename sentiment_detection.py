from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    sentiment = blob.sentiment
    polarity = sentiment.polarity
    
    if polarity > 0:
        sentiment_category = "positive"
    elif polarity < 0:
        sentiment_category = "negative"
    else :
        sentiment_category = "neutral"
        
    return sentiment_category
        
    
    

text = input("Enter your text:-")
result=analyze_sentiment(text)
print(f"sentiment:{result}")