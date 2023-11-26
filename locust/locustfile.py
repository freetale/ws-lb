from locust import User, HttpUser, task, between
import websocket
import time

class QuickstartUser(User):
    wait_time = between(0.1, 0.5)
    
    @task
    def hello_world(self):

        ws = websocket.WebSocket()
        ts = time.time()
        try:
            ws.connect(self.host)
            response_time =  time.time() - ts
            self.environment.events.request.fire(
                    request_type="Connect",
                    name="name",
                    response_time=response_time,
                    response_length=0,
                    exception=None,
                    context=self.context(),
                )
        except Exception as e:
            response_time =  time.time() - ts
            self.environment.events.request.fire(
                request_type="Connect",
                name="name",
                response_time=response_time,
                response_length=0,
                exception=e,
                context=self.context(),
            )
            return

        ts = time.time()
        try:
            text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean non posuere sem. Nullam commodo nulla in pulvinar condimentum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed euismod enim quis tincidunt aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed tempus dui quis sagittis euismod. Integer aliquam viverra sapien, non convallis mauris vehicula nec. Sed ultrices, urna id gravida luctus, quam tortor dignissim odio, ut pellentesque lorem purus vitae libero. Nam non lectus vel diam viverra vehicula ut sit amet dolor. Fusce non scelerisque quam. Aliquam a dapibus mauris. 
             Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce tempor ante leo, quis porttitor turpis tristique non. Sed at erat mauris. Nam tellus tortor, pellentesque scelerisque tempus eu, aliquet eu quam. Vivamus nec velit vel lorem pellentesque facilisis quis nec justo. Fusce vestibulum pellentesque nibh, nec porttitor lorem aliquam vel. Nulla finibus nisl ac ullamcorper lobortis. Donec condimentum tristique mauris sed egestas. Duis quis diam euismod, tristique magna vel, placerat purus. Vestibulum enim arcu, auctor in fringilla eu, congue sed est. Nunc bibendum ullamcorper metus, non sollicitudin neque scelerisque vel. Praesent nec lectus non lectus accumsan maximus. Aliquam et fringilla magna. 
            """

            for i in range(100):
                ts = time.time()
                ws.send(text)
                body = ws.recv()
                response_time =  time.time() - ts
                
                # self.environment.events.request.fire(
                #     request_type="SendMessage",
                #     name="name",
                #     response_time=response_time,
                #     response_length=len(body),
                #     exception=None,
                #     context=self.context(),
                # )
                time.sleep(0.1)
        except Exception as e:
            response_time =  time.time() - ts
            self.environment.events.request.fire(
                request_type="SendMessage",
                name="name",
                response_time=response_time,
                response_length=0,
                exception=e,
                context=self.context(),
            )

        ts = time.time()
        try:
            ws.close()
            response_time =  time.time() - ts
            self.environment.events.request.fire(
                    request_type="Close",
                    name="name",
                    response_time=response_time,
                    response_length=0,
                    exception=None,
                    context=self.context(),
                )
        except Exception as e:
            response_time =  time.time() - ts
            self.environment.events.request.fire(
                    request_type="Close",
                    name="name",
                    response_time=response_time,
                    response_length=0,
                    exception=e,
                    context=self.context(),
                )
