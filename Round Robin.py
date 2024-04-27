def round_robin(processes, time_quantum):
  """
  Simulates Round Robin CPU scheduling algorithm.

  Args:
      processes: List of process objects, each with attributes:
          - pid (int): Process ID
          - arrival_time (int): Arrival time
          - burst_time (int): CPU burst time
          - remaining_time (int): Remaining CPU burst time (initialized to burst_time)
          - completion_time (int): Process completion time (initialized to None)
          - turn_around_time (int): Turnaround time (initialized to None)
          - waiting_time (int): Waiting time (initialized to None)
      time_quantum (int): Time quantum for RR scheduling

  Returns:
      A dictionary containing average turnaround time and average waiting time.
  """

  n = len(processes)
  completed_processes = []
  current_time = 0
  total_turnaround_time = 0
  total_waiting_time = 0

  while completed_processes != processes:
    for i in range(n):
      if processes[i] not in completed_processes and processes[i].arrival_time <= current_time:
        if processes[i].remaining_time <= time_quantum:
          # Process completes within current time slice
          current_time += processes[i].remaining_time
          processes[i].completion_time = current_time
          processes[i].turn_around_time = processes[i].completion_time - processes[i].arrival_time
          processes[i].waiting_time = processes[i].turn_around_time - processes[i].burst_time
          total_turnaround_time += processes[i].turn_around_time
          total_waiting_time += processes[i].waiting_time
          completed_processes.append(processes[i])
          processes[i].remaining_time = 0
        else:
          # Process needs more time
          processes[i].remaining_time -= time_quantum
          current_time += time_quantum

  avg_turnaround_time = total_turnaround_time / n
  avg_waiting_time = total_waiting_time / n

  return {"Average Turnaround Time": avg_turnaround_time, "Average Waiting Time": avg_waiting_time}

# Example usage
processes = [
    {"pid": 1, "arrival_time": 0, "burst_time": 8},
    {"pid": 2, "arrival_time": 1, "burst_time": 4},
    {"pid": 3, "arrival_time": 2, "burst_time": 9},
]

time_quantum = 2  # Adjust time quantum as needed

result = round_robin(processes, time_quantum)

print("Average Turnaround Time:", result["Average Turnaround Time"])
print("Average Waiting Time:", result["Average Waiting Time"])
