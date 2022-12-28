import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service):
  value = []

  def exposed_insert(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_search(self, data):
    if data in self.value:
      return 1
    return 0

  def exposed_value(self):
    return self.value

if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT)
  server.start()

