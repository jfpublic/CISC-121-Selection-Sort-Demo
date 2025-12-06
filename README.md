**Algorithm used:** Selection sort

I chose to demonstrate selection sort as it is a simple algorithm to understand, it is efficient for small data sets as will be used in the demo application, and the sorting happens in place so no extra space is needed.

**Demo video:**
[![CISC-121-Selection-Sort-Demo](https://img.youtube.com/vi/D22kUul0dNE/0.jpg)](https://www.youtube.com/watch?v=D22kUul0dNE)

**Problem breakdown & Computational thinking:**

- Decomposition: Selection sort involves iteratively selecting the first unsorted item, then selecting the smallest item after the first unsorted item, then swapping those two items. 

- Pattern Recognition: The algorithm repeatedly finds the first unsorted item and the smallest item after it, then swaps them.

- Abstraction: The user does not get shown the process of iterating over the elements to find the smallest element or the first unsorted item as it is not necessary to understand selection sort.

- Algorithm Design: Take a list as an input, get the length of this list, iterate over all of the items in the list and find the smallest item, swap the first unsorted item with the smallest one that was found, repeat this until the last item in the list is the first unsorted item, return the list.

**Steps to run:**
1. Install Gradio and Matplotlib with pip (run the command "pip install gradio" then "pip install matplotlib" in cmd)
2. Download and run 'app.py'
3. Copy the given link/ip from the new window and paste it into a browser (chrome preferred as I have tested it however it should work with any)

**Hugging face link:** https://huggingface.co/spaces/JFpublic/CISC-121-Selection-Sort-Demo

**By Jacob Fasken**

**Acknowledgements:**

I referenced this geeksforgeeks page to implement my selection sort: https://www.geeksforgeeks.org/python/python-program-for-selection-sort/

I utilized GPT-4o mini to assist implementing the visuals utilizing Gradio and Matplotlib




**Small note:** matplotlib starts counting at 1, not 0, the extra 0 column in the graphs is a result of this.
