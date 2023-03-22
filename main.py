import random, time
import tabulate


def qsort(a, pivot_fn):
    ## TO DO
  if len(a) < 2:
    return a
    
  else:
    currrent_pos = 0
    for i in range(1, len(a)-1):
      if a[i] <= a[0]:
        currrent_pos += 1
        temp = a[i]
        a[i] = a[currrent_pos]
        a[currrent_pos] = temp
        
    temp = a[0]
    a[0] = a[currrent_pos]
    a[currrent_pos] = temp

    left = qsort(a[0:currrent_pos])
    right = qsort(a[currrent_pos:len(a)-1])

    a = left + a[currrent_pos] + right

    return a    
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = qsort(mylist, random.randint(0,len(mylist)-1))
    qsort_random_pivot = qsort(mylist, len(mylist)-1)
    tim_sort = time_search(qsort, mylist)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
