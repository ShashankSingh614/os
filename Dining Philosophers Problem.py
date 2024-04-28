import threading
import time
import random

# Define the number of philosophers and forks
num_philosophers = 5

# Define semaphores for the chopsticks
chopsticks = [threading.Semaphore(1) for _ in range(num_philosophers)]

# Define the philosopher thread function
def philosopher(index):
    while True:
        print(f"Philosopher {index} is thinking...")
        time.sleep(random.randint(1, 5))  # Think for a random amount of time
        
        left_chopstick = index
        right_chopstick = (index + 1) % num_philosophers
        
        # Attempt to pick up the chopsticks
        print(f"Philosopher {index} is hungry and trying to pick up chopsticks...")
        chopsticks[left_chopstick].acquire()  # Wait for left chopstick
        chopsticks[right_chopstick].acquire()  # Wait for right chopstick
        
        print(f"Philosopher {index} picked up chopsticks and is eating...")
        time.sleep(random.randint(1, 5))  # Eat for a random amount of time
        
        # Release the chopsticks
        chopsticks[left_chopstick].release()  # Put down left chopstick
        chopsticks[right_chopstick].release()  # Put down right chopstick
        
        print(f"Philosopher {index} finished eating and put down chopsticks. Back to thinking...")
        time.sleep(random.randint(1, 5))  # Think again

# Create a thread for each philosopher
philosopher_threads = []
for i in range(num_philosophers):
    philosopher_threads.append(threading.Thread(target=philosopher, args=(i,)))

# Start the philosopher threads
for thread in philosopher_threads:
    thread.start()

# Wait for the philosopher threads to complete
for thread in philosopher_threads:
    thread.join()

