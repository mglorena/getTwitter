import tweepy

# Configurar las credenciales de la API de Twitter
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
#Modificando para poder tener permiso, las claves fueron regeneradas

# Autenticar con las credenciales de la API de Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Crear una instancia del objeto API
api = tweepy.API(auth)

# ID del tweet al que deseas obtener los comentarios o respuestas
tweet_id = "1669681078506868737"

# Obtener los comentarios o respuestas al tweet
comments = api.get_status(tweet_id, tweet_mode='extended').replies()

# Imprimir los comentarios
for comment in comments:
    print(comment.full_text)
