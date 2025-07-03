import time
import logging
import cv2
from pioneer_sdk import Camera


# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def init_aruco_detector():
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    aruco_params = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)
    return detector


def scan_aruco_process():
    detector = init_aruco_detector()
    camera = Camera()

    try:
        logging.info("Ожидание запуска камеры...")
        time.sleep(2)

        logging.info("Запуск процесса сканирования ArUco-маркеров")

        while True:
            frame = camera.get_cv_frame()

            if frame is None or frame.size == 0:
                logging.warning("Получен пустой кадр, продолжаем...")
                continue

            corners, ids, _ = detector.detectMarkers(frame)

            if ids is not None:
                for marker_id in ids.flatten():
                    logging.info(f"Обнаружен ArUco-маркер с ID: {marker_id}")

                cv2.aruco.drawDetectedMarkers(frame, corners, ids)
                cv2.imshow("Обнаружение ArUco", frame)

            if cv2.waitKey(1) == 27:  # ESC
                logging.info("Нажата клавиша ESC — завершение работы")
                break

    except Exception as e:
        logging.exception("Ошибка во время выполнения scan_aruco_process:")
    finally:
        cv2.destroyAllWindows()
        logging.info("Окна OpenCV закрыты, процесс завершён")
