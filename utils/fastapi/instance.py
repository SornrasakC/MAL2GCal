from utils.fastapi.fast_app import app
import contextlib
import time
import threading
import uvicorn
from uvicorn import Config

class Server(uvicorn.Server):
    def install_signal_handlers(self):
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
        finally:
            self.should_exit = True
            thread.join()

def start_server_thread():
    config = Config(app, host="127.0.0.1", port=80, log_level="error")
    server = Server(config=config)

    return server.run_in_thread()

    with server.run_in_thread():
        # Server is started.
        ...
        while True:
            pass
            # time.sleep(5)
        # Server will be stopped once code put here is completed
        ...

    # Server stopped.
