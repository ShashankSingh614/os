def lru(page_references, frame_count):
  """
  Simulates LRU page replacement algorithm.

  Args:
      page_references: List of page references (integers)
      frame_count: Number of memory frames (integer)

  Returns:
      A list containing the page faults and the page frames at each step.
  """
  frames = [None] * frame_count
  page_faults = 0
  usage_map = {}  # Track the last used time for each page in memory

  for ref in page_references:
    if ref not in frames:
      page_faults += 1
      # If full, remove the least recently used (oldest in usage_map)
      if len(frames) == frame_count:
        least_recently_used = min(usage_map, key=usage_map.get)
        frames.remove(least_recently_used)
        del usage_map[least_recently_used]
      frames.append(ref)
      usage_map[ref] = len(page_references)  # Update usage time
    else:
      usage_map[ref] = len(page_references)  # Update usage time for accessed page

    print(f"Page frames: {frames}")  # Print frames at each step (optional)

  return page_faults, frames

# Example usage (same as FIFO)
page_faults, frames = lru(page_references, frame_count)

print(f"Total page faults: {page_faults}")
