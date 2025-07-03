from pion import Pion,Spion
import time


def main():
    dron = Pion(
        ip='10.1.100.134',
        mavlink_port=5656,
        logger=True
    )

    # dron.arm()
    # dron.takeoff()
    # time.sleep(4)
    # start = 0
    # n = 2 
    # m =2
    # for y in range(start,m):
    #     dron.goto(start, y, 1, 0.0, wait=True)
    #     time.sleep(4)
    # for x in range(start-1,-n,-1):
    #     dron.goto(x, m-1, 1, 0.0, wait=True)
    #     time.sleep(4)
    # for y in range(m-2,start,-1):
    #     dron.goto(-n+1, y, 1, 0.0, wait=True)
    #     time.sleep(4)
    # for x in range (-n+1,start+1):
    #     dron.goto(-n+1, start+1, 1, 0.0, wait=True)
    #     time.sleep(4)

    dron.land()
    dron.stop()




if __name__ == "__main__":
    main()
