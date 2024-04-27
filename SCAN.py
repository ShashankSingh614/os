def scan(page_references, start, head, direction):
  """
  Simulates SCAN page replacement algorithm (non-preemptive).

  Args:
      page_references: List of page references (sector numbers)
      start: Starting sector of the disk
      head: Current head position
      direction: Initial head movement direction ("in" or "out")

  Returns:
      A list containing the total head movement and the page access sequence.
  """
  total_movement = 0
  access_sequence = []

  seek_queue = sorted(page_references)  # Sort references for SCAN

  if direction == "in":
    # Move inward first, then outward
    for ref in seek_queue:
      if ref >= head:
        total_movement += abs(ref - head)
        head = ref
        access_sequence.append(ref)
    # Move to the other end (assuming fixed-size disk)
    total_movement += abs(start - head)
    head = start
    for ref in seek_queue[::-1]:
      if ref < head:
        total_movement += abs(ref - head)
        head = ref
        access_sequence.append(ref)
  else:
    # Move outward first, then inward (similar logic as above)
    # ... (implement similar logic for outward-first direction)

  return total_movement, access_sequence

# Example usage (assuming fixed-size disk with sectors 0-199)
page_references = [170, 43, 70, 120, 110, 60, 50]
start = 0
head = 100
direction = "in"  # Change to "out" for outward-first SCAN

total_movement, access_sequence = scan(page_references, start, head, direction)

print(f"Total head movement: {total_movement}")
print(f"Page access sequence: {access_sequence}")
