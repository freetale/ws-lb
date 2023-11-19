from locust import User, HttpUser, task, between
import websocket
import time
import asyncio

class QuickstartUser(User):
    @task
    def hello_world(self):
        ts = time.time()
        try:
            text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean non posuere sem. Nullam commodo nulla in pulvinar condimentum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed euismod enim quis tincidunt aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed tempus dui quis sagittis euismod. Integer aliquam viverra sapien, non convallis mauris vehicula nec. Sed ultrices, urna id gravida luctus, quam tortor dignissim odio, ut pellentesque lorem purus vitae libero. Nam non lectus vel diam viverra vehicula ut sit amet dolor. Fusce non scelerisque quam. Aliquam a dapibus mauris. 
             Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce tempor ante leo, quis porttitor turpis tristique non. Sed at erat mauris. Nam tellus tortor, pellentesque scelerisque tempus eu, aliquet eu quam. Vivamus nec velit vel lorem pellentesque facilisis quis nec justo. Fusce vestibulum pellentesque nibh, nec porttitor lorem aliquam vel. Nulla finibus nisl ac ullamcorper lobortis. Donec condimentum tristique mauris sed egestas. Duis quis diam euismod, tristique magna vel, placerat purus. Vestibulum enim arcu, auctor in fringilla eu, congue sed est. Nunc bibendum ullamcorper metus, non sollicitudin neque scelerisque vel. Praesent nec lectus non lectus accumsan maximus. Aliquam et fringilla magna. 
            """
            self.ws.send(text)
            print("send")
            body = asyncio.run(asyncio.wait_for(self.ws.recv(), timeout = 1.0))
            print("body")
            response_time =  time.time() - ts
            
            self.environment.events.request.fire(
                request_type="WSS",
                name="name",
                response_time=response_time,
                response_length=len(body),
                exception=None,
                context=self.context(),
            )
        except TimeoutError as e:
            response_time =  time.time() - ts
            self.environment.events.request.fire(
                request_type="WSS",
                name="name",
                response_time=response_time,
                response_length=0,
                exception="TimeoutError",
                context=self.context(),
            )
        # except exceptions.ConnectionClosed:
        #     response_time =  time.time() - ts
        #     self.environment.events.request.fire(
        #         request_type="WSS",
        #         name="name",
        #         response_time=response_time,
        #         response_length=0,
        #         exception="ConnectionClosed",
        #         context=self.context(),
        #     )
    
    def on_start(self):
        ws = websocket.WebSocket()
        ws.connect(self.host)
        self.ws = ws


    def on_stop(self):
        self.ws.close()


# import time
# import json
# from locust import task
# from locust_plugins.users.socketio import SocketIOUser


# class MySocketIOUser(User):
#     @task
#     def my_task(self):
#         self.my_value = None

#         self.connect("ws://host.docker.internal:9001")

#         # example of subscribe
#         self.send('42["subscribe",{"url":"/sport/matches/11995208/draws","sendInitialUpdate": true}]')

#         # wait until I get a push message to on_message
#         while not self.my_value:
#             time.sleep(0.1)

#         # wait for additional pushes, while occasionally sending heartbeats, like a real client would
#         self.sleep_with_heartbeat(10)

#     def on_message(self, message):
#         self.my_value = json.loads(message)["my_value"]

#     if __name__ == "__main__":
#         host = "http://example.com"