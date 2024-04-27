from threading import Thread, Semaphore

class Philosopher(Thread):
  def __init__(self, name, left_fork, right_fork):
    super().__init__()
    self.name = name
    self.left_fork = left_fork
    self.right_fork = right_fork

  def run(self):
    while True:
      self.left_fork.acquire()
      print(f"{self.name} picks up left fork")
      self.right_fork.acquire()
      print(f"{self.name} picks up right fork - Eating")
      self.right_fork.release()
      print(f"{self.name} puts down right fork")
      self.left_fork.release()
      print(f"{self.name} puts down left fork - Thinking")

if __name__ == "__main__":
  num_philosophers = 5
  forks = [Semaphore(1) for _ in range(num_philosophers)]

  philosophers = [Philosopher(f"Philosopher {i+1}", forks[i], forks[(i+1) % num_philosophers]) for i in range(num_philosophers)]

  for p in philosophers:
    p.start()
