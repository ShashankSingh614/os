def sjf(processes):
  """
  This function simulates the Shortest Job First scheduling algorithm.

  Args:
      processes: A list of dictionaries where each dictionary represents a process
                 with keys 'process_id' (int), 'burst_time' (int), and optionally 'arrival_time' (int).
                 If 'arrival_time' is not provided, it defaults to 0.

  Returns:
      A dictionary containing average waiting time and average turn around time.
  """
  # Sort processes by burst time (ascending order)
  processes.sort(key=lambda process: process['burst_time'])

  total_waiting_time = 0
  total_turnaround_time = 0
  completion_time = 0

  for process in processes:
    burst_time = process['burst_time']
    arrival_time = process.get('arrival_time', 0)
    completion_time += burst_time

    # Waiting time for the current process
    waiting_time = completion_time - arrival_time - burst_time

    # Turn around time for the current process
    turnaround_time = completion_time - arrival_time

    total_waiting_time += waiting_time
    total_turnaround_time += turnaround_time

  # Calculate average waiting time and average turn around time
  avg_waiting_time = total_waiting_time / len(processes)
  avg_turnaround_time = total_turnaround_time / len(processes)

  return {
      "average_waiting_time": avg_waiting_time,
      "average_turnaround_time": avg_turnaround_time
  }

# Example usage
processes = [
    {"process_id": 1, "burst_time": 5},
    {"process_id": 2, "burst_time": 2},
    {"process_id": 3, "burst_time": 3},
]

results = sjf(processes)
print(f"Average Waiting Time: {results['average_waiting_time']}")
print(f"Average Turnaround Time: {results['average_turnaround_time']}")
