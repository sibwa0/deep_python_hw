import socket
import selectors
import asyncio
import aiohttp

from utils import PORT


class Server:
    def __init__(self, urls, num_workers):  #, num_top_words) -> None:
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.bind(("localhost", PORT))
        self.server_sock.listen(5)

        self._num_workers = num_workers
        self._urls = urls
        # self._num_top_words = num_top_words

        self.selector = selectors.DefaultSelector()

        self.selector.register(self.server_sock, selectors.EVENT_READ, self.accept_conn)

    def accept_conn(self, server_sock):
        client_sock, addr = server_sock.accept()
        print('Connect', addr)
        self.selector.register(client_sock, selectors.EVENT_READ, self.respond)

    def respond(self, client_sock):
        data = client_sock.recv(4096)

        if data:
            # logic
            # client_sock.send(data.decode().upper().encode())
            await batch_fetch(self._urls, self._num_workers)
        else:
            print("close client")
            self.selector.unregister(client_sock)
            client_sock.close()

    def event_loop(self):
        while True:
            events = self.selector.select()  # (key, events_mask)

            for key, _ in events:
                # key: NamedTuple(fileobj, events, data)
                callback = key.data
                callback(key.fileobj)


# @staticmethod
async def fetch(session, q):
    while True:
        url = await q.get()
        # global counter
        # counter += 1

        try:
            async with session.get(url) as resp:
                data = await resp.read()
                # assert resp.status == 200
        finally:
            q.task_done()
        

async def batch_fetch(urls, workers):
    q = asyncio.Queue()
    for url in urls:
        await q.put(url)

    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(fetch(session, q))
            for _ in range(workers)
        ]
        await q.join()
        
        for w in workers:
            w.cancel()


if __name__ == '__main__':
    serv = Server()
    serv.event_loop()
