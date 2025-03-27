import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.io_loop = io_loop  
        self.connection = None  
        self.connect_and_read()

    def start(self):
        """Khởi động client"""
        print("Client started...")

    def stop(self):
        """Dừng client và vòng lặp IOLoop"""
        print("Stopping client...")
        self.io_loop.stop()

    def connect_and_read(self):
        """Kết nối đến server và thiết lập nhận tin nhắn"""
        print("Connecting to WebSocket server...")
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket/",
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30,
        )

    def maybe_retry_connection(self, future):
        """Thử kết nối lại nếu không thể kết nối"""
        try:
            self.connection = future.result()
            print("Connection established!")
        except Exception as e:
            print(f"Could not reconnect: {e}. Retrying in 3 seconds...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        """Xử lý tin nhắn nhận được từ server"""
        if message is None:
            print("Disconnected from server, reconnecting...")
            self.connect_and_read()
            return
        print(f"Received word from server: {message}")
        self.connection.read_message(callback=self.on_message)

def main():
    io_loop = tornado.ioloop.IOLoop.current()

    client = WebSocketClient(io_loop)

    io_loop.add_callback(client.start)
    io_loop.start()  

if __name__ == "__main__":
    main()
