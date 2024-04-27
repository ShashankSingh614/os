def look(page_references, head, direction):
  """
  Simulates LOOK page replacement algorithm (non-preemptive).

  Args:
      page_references: List of page references (sector numbers)
      head: Current head position
      direction: Initial head movement direction ("in" or "out")

  Returns:
      A list containing the total head movement and the page access sequence.
  """
  total_movement = 0
  access_sequence = []

  seek_queue = sorted(page_references)  # Sort references for LOOK

  if direction == "in":
    # Move inward first, then stop
    for ref in seek_queue:
      if ref >= head:
        total_movement += abs(ref - head)
        head = ref
        access_sequence.append(ref)
      else:
        break  # Stop at the first request in the opposite direction
  else:
    # Move outward first, then stop (similar logic)
    for ref in seek_queue[::-1]:
      if ref <= head:
        total_movement += abs(ref - head)
        head = ref
        access_sequence.append(ref)
      else:
        break  # Stop at the first request in the opposite direction

  return total_movement, access_sequence

# Example usage (same as SCAN)
total_movement, access_sequence = look(page_references, head, direction)

print(f"Total head movement: {total_movement}")
print(f"Page access sequence: {access_sequence}")
