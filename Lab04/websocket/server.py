import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()  
    def open(self):
        """Hàm được gọi khi một client kết nối"""
        WebSocketServer.clients.add(self)
        print("New client connected!")

    def on_close(self):
        """Hàm được gọi khi một client đóng kết nối"""
        WebSocketServer.clients.remove(self)
        print("Client disconnected!")

    @classmethod
    def send_message(cls, message: str):
        """Gửi tin nhắn tới tất cả các client"""
        print(f"Sending message '{message}' to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)

def main():
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],  
        websocket_ping_interval=10,  
        websocket_ping_timeout=30    
    )
    app.listen(8888)  
    print("WebSocket server is running on ws://localhost:8888/websocket/")

    word_selector = RandomWordSelector(["apple", "banana", "orange", "melon", "grape"])

    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )
    periodic_callback.start()

    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
