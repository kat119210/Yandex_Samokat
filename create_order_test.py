import data
import sender_stand_request


def test_new_order():
    response = sender_stand_request.post_new_orders(data.orders_body)
    assert response.status_code == 201   #проверяем, что созданный заказ без ошибок
    track = sender_stand_request.post_new_orders(data.orders_body).json()["track"]
    return track                         #сохраняем номер трека


def test_get_order_by_track_number():
    response = sender_stand_request.get_orders_track(sender_stand_request.order_track_number)
    assert response.status_code == 200   #получение заказа по трек номеру и проверка кода ответа
