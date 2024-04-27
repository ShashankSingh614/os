def is_safe_state(processes, available, max_need, allocation):
  """
  Simulates safety check in Banker's Algorithm.

  Args:
      processes: List of process names (strings)
      available: List of available resources (integers)
      max_need: Matrix of maximum resource needs (integers)
      allocation: Matrix of allocated resources (integers)

  Returns:
      True if the system is in a safe state, False otherwise.
  """
  n = len(processes)
  need = [[max_need[i][j] - allocation[i][j] for j in range(len(available))] for i in range(n)]

  finish = [False] * n
  work = available.copy()

  safe_seq = []
  for _ in range(n):
    found = False
    for i in range(n):
      if not finish[i] and all(need[i][j] <= work[j] for j in range(len(available))):
        for j in range(len(available)):
          work[j] += allocation[i][j]
        finish[i] = True
        safe_seq.append(processes[i])
        found = True
        break

    if not found:
      return False

  return True, safe_seq

# Example usage (adjust resource types and values as needed)
processes = ["P1", "P2", "P3"]
available = [3, 2, 1]
max_need = [
  [7, 5, 3],
  [4, 2, 2],
  [6, 1, 2]
]
allocation = [
  [0, 1, 0],
  [2, 0, 0],
  [1, 1, 2]
]

is_safe, safe_seq = is_safe_state(processes, available, max_need, allocation)

if is_safe:
  print("System is in a safe state. Safe sequence:", safe_seq)
else:
  print("System is in an unsafe state.")
