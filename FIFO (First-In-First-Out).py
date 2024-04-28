from queue import Queue 
# Function to find page faults using FIFO 
def pageFaults(pages, n, capacity): 
	
	s = set() 	                    # To represent set of current pages. We use an unordered_set so that we quickly check if a page is present in set or not 
	indexes = Queue()  	            # To store the pages in FIFO manner 
	page_faults = 0                 # Start from initial page 

	for i in range(n): 		
		if (len(s) < capacity):                  # Check if the set can hold  more pages 			
			if (pages[i] not in s):              # Insert it into set if not present  already which represents page fault 
				s.add(pages[i]) 			
				page_faults += 1                   # increment page fault 				
				indexes.put(pages[i])              # Push the current page into the queue 

		# If the set is full then need to perform FIFO i.e. remove the first page of the queue from set and queue both and insert the current page 
		else: 	

			if (pages[i] not in s):    			     # Check if current page is not already present in the set 			
				val = indexes.queue[0]                 # Pop the first page from the queue 
				indexes.get() 
				s.remove(val)                          # Remove the indexes page 
				s.add(pages[i])                         # insert the current page 			
				indexes.put(pages[i])                  # push the current page into  the queue 			
				page_faults += 1                        # Increment page faults 

	return page_faults 

# Driver code 
if __name__ == '__main__': 
	# Input page reference string
	pages = list(map(int, input("Enter the page reference string (comma-separated): ").split(',')))
	n = len(pages) 
	# Input capacity (number of pages in memory)
	capacity = int(input("Enter the number of pages in memory: "))
	pageFault = pageFaults(pages, n, capacity)
	print(f"Total page faults: {pageFault}")
	hits = n - pageFault
	print(f"Total hits: {hits}")
