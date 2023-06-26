import tweepy

# Configurar las credenciales de la API de Twitter
consumer_key = "b1xEAoHh451I1qlOeiEC1p1ne"
consumer_secret = "huB96moyJ6Dj8Jj2IfDwWdrIYS8ovdfIyoEdpCy65ajjC5Cv4Q"
access_token = "15394306-38dsRVZ12evrNbYiimUsS1JXNoR9EtBEsvye6MxC2"
access_token_secret = "r42oRgPgJekVBVQsJOvFKPN9vRd7NPNdSJjwXEYRDtd5p"
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
#fbSG8ltZno-u0rVXEjnNlsQAniHZx6R71U2uMh_Kp0eiQBvISO