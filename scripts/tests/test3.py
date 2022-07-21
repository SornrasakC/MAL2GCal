from utils.fastapi.instance import start_server_thread

import time

with start_server_thread():
    while True:
        print('do stuff 2')
        time.sleep(3)