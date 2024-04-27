def fifo(page_references, frame_count):
  """
  Simulates FIFO page replacement algorithm.

  Args:
      page_references: List of page references (integers)
      frame_count: Number of memory frames (integer)

  Returns:
      A list containing the page faults and the page frames at each step.
  """
  frames = [None] * frame_count
  page_faults = 0

  for ref in page_references:
    if ref not in frames:
      page_faults += 1
      # Add to the end (FIFO) and remove the first element if full
      frames.append(ref)
      if len(frames) > frame_count:
        frames.pop(0)
    print(f"Page frames: {frames}")  # Print frames at each step (optional)

  return page_faults, frames

# Example usage
page_references = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 4

page_faults, frames = fifo(page_references, frame_count)

print(f"Total page faults: {page_faults}")
