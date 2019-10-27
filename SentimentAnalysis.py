import paralleldots

api_key   = "FKtFmXzzfCOjvOqj1wCq6qNDJGRHqBXdaJ3Ioh1xfls"
text      = "I love cookies"
url      = "https://consequenceofsound.net/wp-content/uploads/2019/07/joker-2019.jpg?quality=80&w=807"


paralleldots.set_api_key( api_key )



# sentiement analysis


print( "\nSentiment" )
NegativeValue=paralleldots.sentiment(text).get("sentiment").get("negative")
NeutralValue=paralleldots.sentiment(text).get("sentiment").get("neutral")
PositiveValue=paralleldots.sentiment(text).get("sentiment").get("positive")

print(f"Negative : {NegativeValue}")
print(f"Neutral : {NeutralValue}")
print(f"Positive : {PositiveValue}")

if NegativeValue<NeutralValue<PositiveValue:
    print("Overall Analysis : Positive")
elif PositiveValue<NeutralValue<NegativeValue:
    print("Overall Analysis : Negative")
else:
    print("Overall Analysis : Neutral")

# emotional analysis
print( "\nFacial Emotion " )

happy=paralleldots.facial_emotion_url( url ).get("facial_emotion")[0].get("score")
fear=paralleldots.facial_emotion_url( url ).get("facial_emotion")[1].get("score")
surprise=paralleldots.facial_emotion_url( url ).get("facial_emotion")[2].get("score")
sad=paralleldots.facial_emotion_url( url ).get("facial_emotion")[3].get("score")
neutral=paralleldots.facial_emotion_url( url ).get("facial_emotion")[4].get("score")
disgust=paralleldots.facial_emotion_url( url ).get("facial_emotion")[5].get("score")
angry=paralleldots.facial_emotion_url( url ).get("facial_emotion")[6].get("score")
print(f"Happy : {happy}\nFear : {fear}\nSurprise : {surprise}\nSad : {sad}\nNeutral : {neutral}\nDisgust : {disgust}\nAngry : {angry}")

