import multiprocessing
from collections.abc import Callable

from .scan import scan_aruco_process


def launch(fly_task: Callable):
    multiprocessing.set_start_method('spawn')
    scan_proc = multiprocessing.Process(target=scan_aruco_process)
    flight_proc = multiprocessing.Process(target=fly_task)

    flight_proc.start()
    scan_proc.start()

    flight_proc.join()
    scan_proc.terminate()
