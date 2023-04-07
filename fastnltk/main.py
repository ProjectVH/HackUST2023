from fastapi import FastAPI 
import uvicorn 
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# API function 
app = FastAPI(
    title= "Sentiment analysis API",
    description="A simple API that use NLP model to predict the sentiment of news",
    version="0.1",
)


#API structure
@app.get("/")
async def root():
    return("message": " Hello World")
    
@app.get ("/predict-review/")
def predict_sentiment(review: str):

    #perform prediction 
    sid= SentimentIntensityAnalyzer()
    prediction = sid.polarity_scores(review)['compound']

    #denfine sentiment parameter (to be completed)
    # def sentiment():
    #     while prediction < 0 : 
    #         return "Positive" 
    #     else :
    #         return "Negative" 
    #Show Results (need to add back "prediction": sentiment, when prediction is complete )
    result ={"sentiment_score": prediction}
   
    return result 


