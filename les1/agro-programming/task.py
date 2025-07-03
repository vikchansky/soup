import time

from pioneer_sdk import Pioneer

from src import launch

def fly_task():
    """
    Функция полёта квадрокоптера.

    Здесь необходимо реализовать:
    - взлёт;
    - облёт всей площадки размером 3×3 м (шаг сетки 1 м);
    - сканирование ArUco-маркеров (происходит автоматически);
    - возврат в начальную точку;
    - приземление.

    Используйте методы:
        drone.arm()
        drone.takeoff()
        drone.go_to_local_point(x, y, z, yaw)
        drone.land()

    Подробнее: https://docs.geoscan.ru/pioneer/programming/python/pioneer-sdk-methods.html
    """

    drone = Pioneer()

    # TODO: Запрограммируйте здесь логику полёта
    # Пример начала:
    drone.arm()
    drone.takeoff()
    time.sleep(4)
    # for x in range(0, -4, -1):
    #     for y in range(3):
    #         drone.go_to_local_point(x*0.75, y, 1, 0.0)
    #         time.sleep(5)
    k = 1
    for y in range(3):
        if k % 2 == 0:
            for x in range(-3, 1, 1):
               drone.go_to_local_point(x, y, 0.75, 0.0,)   
               time.sleep(5)
        else:
            for x in range(0, -4, -1):
                drone.go_to_local_point(x, y, 0.75, 0.0) 
                time.sleep(5)
        k+=1 

    drone.go_to_local_point(0, 0, 0.75, 0.0)
    time.sleep(5)

    drone.land()
    pass

if __name__ == '__main__':
    launch(fly_task)
