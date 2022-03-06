from crypt import methods
from pickle import GET
import requests
import json
import pandas as pd

from flask import Flask, request, Response


# constants
token = '5121253425:AAH9V9aB_gUNSC08v2JNq8XbH-4PAgWBL2Y'

# Info about the bot
url = https://api.telegram.org/bot5121253425:AAH9V9aB_gUNSC08v2JNq8XbH-4PAgWBL2Y/getMe

# get updates
url = https://api.telegram.org/bot5121253425:AAH9V9aB_gUNSC08v2JNq8XbH-4PAgWBL2Y/getUpdates

# send message
url = https://api.telegram.org/bot5121253425:AAH9V9aB_gUNSC08v2JNq8XbH-4PAgWBL2Y/sendMessage?chat_id=1280261014&text=Hi joca, Im good

def send_message( chat_id, text ):
    # send message
    url = 'https://api.telegram.org/bot{}'.format( token )
    url = url + '/sendMessage?chat_id={}'.format( chat_id )

    r = requests.post( url, json={ 'text': text } )
    print('Status Code {}'.format( r.status_code ))

    return None

def load_dataset( store_id ):
    # loading test dataset
    df10 = pd.read_csv( '/home/jocafneto/repositorio/rossmann/data/test.csv' )
    df_store_raw = pd.read_csv( '/home/jocafneto/repositorio/rossmann/data/store.csv' )


    # merge test + store
    df_test = pd.merge( df10, df_store_raw, how='left', on='Store' )

    # choose store for prediction
    df_test = df_test[df_test['Store'] == store_id]

    # remove closed days
    df_test = df_test[df_test['Open'] != 0]
    df_test = df_test[~df_test['Open'].isnull()]
    df_test = df_test.drop( 'Id', axis=1 )

    # convert DataFrame to json
    data = json.dumps( df_test.to_dict( orient='records' ) )
    
    return data

def predict( data ):
    # API call
    # url = 'http://0.0.0.0:5000/rossmann/predict'
    url = 'https://rossmann-model-test27.herokuapp.com/rossmann/predict'
    header = {'Content-type': 'application/json'}
    data = data

    r = requests.post( url, data=data, headers=header )
    print( 'Status Code {}'.format( r.status_code ) )

    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys() )

    return d1



# d2 = d1[['store', 'prediction']].groupby( 'store' ).sum().reset_index()

# for i in range( len( d2 ) ):
#     print( 'Store Number {} will sell R${:,.2f} in the next 6 week'.format( d2.loc[i, 'Store'], d2.loc[i, 'prediction'] ) )

def parse_message( message ):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']

    return chat_id, store_id

# API Initialize
app = Flask(__name__)

@app.route( '/', methods=['GET', 'POST'] )
def index():
    if request.method == 'POST':
        message = request.get_json()

        chat_id, store_id = parse_message( message )

    else:
        return '<h1> Rossmann Telegram BOT </h1>'

if __name__ == __main__:
    app.run( host = '0.0.0.0', port=5000 )