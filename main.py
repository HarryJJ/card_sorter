import time

from card_deck import deck
from card_sorter import BubbleSort, SelectionSort, InsertionSort, MergeSort, QuickSort

# Perform sorting using each sorting algorithm and measure the time
sorting_algorithms = [BubbleSort(), SelectionSort(), InsertionSort(), MergeSort(), QuickSort()]
for algorithm in sorting_algorithms:
    deck.shuffle_deck()
    start_time = time.time()
    sorted_deck = algorithm.sort(deck.deck)
    end_time = time.time()

    print(f"{algorithm.__class__.__name__}:")
    deck.deck = sorted_deck
    deck.print_deck()
    print("Elapsed Time:", end_time - start_time, "seconds\n")
