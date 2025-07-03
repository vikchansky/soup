from pion import Pion
import time

def main():
    # print("Hello")
    drone = Pion(
        ip = '10.1.100.134',
        mavlink_port = 5656,
        logger = True
        )
    drone.arm()
    drone.takeoff()
    time.sleep(5)
    drone.goto(x=1, y=1, z=2, yaw=0, wait=True)
    drone.land()

if __name__ == "__main__":
    main()
