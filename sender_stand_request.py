import configuration
import requests
import data
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS, #подставляем полный url
                         json=body)   #создание заказа


order_track_number = post_new_orders(data.orders_body).json()["track"]   #сохранение номера трека заказа

def get_orders_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK,
                        params={"t": track})  #Выполнение запроса на получения заказа по треку заказа


