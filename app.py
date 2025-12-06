import gradio as gr
import numpy as np
import matplotlib.pyplot as plt

def sort_and_visualize(input_list):
    unsorted = list(map(int, input_list.split(','))) #convert the input into a list
    n = len(unsorted) #get the length of the unsorted arr
    
    frames = [] #stores the frames for the visuals later

    for x in range(n): #repeat for each item in arr
        firstUnsorted = x #pointer for the first unsorted item
        for y in range(x + 1, n): #check items after the pointer (the unsorted items)
            if unsorted[y] < unsorted[firstUnsorted]: #find the smallest item after the pointer
                firstUnsorted = y #set the firstUnsorted to the found smallest item
        unsorted[x], unsorted[firstUnsorted] = unsorted[firstUnsorted], unsorted[x] #swaps the found smallest item after the pointer with the pointer for the first unsorted item
        
        plt.bar(range(len(unsorted)), unsorted, color='lightgray') #creates the bar chart for the unsorted
        plt.bar(x, unsorted[x], color='cyan', label='Sorted', alpha=0.6) #highlights the first unsorted item / the last item to be sorted
        plt.bar(firstUnsorted, unsorted[firstUnsorted], color='red', label='Current Min', alpha=0.6) #highlights the current smallest unsorted item
        plt.title('Sorting Visualization') #creates the graph title
        plt.xlabel('Index') #creates the x axis lable
        plt.ylabel('Value') #creates the y axis lable
        plt.ylim(0, max(unsorted) + 1) #sets the max height of the y axis
        plt.xticks(range(len(unsorted))) #sets the x axis markings to be the length of the list
        plt.legend() #adds the legend to the chart
        plt.savefig(f'temp_frame_{x}.png') #saves the created graph as a image with a unique name
        frames.append(f'temp_frame_{x}.png') #collects the generated image into a list to be displayed
        plt.clf() #clear everything for the next iteration

    return unsorted, frames #returns sorted arr

iface = gr.Interface( #creates the web-based demo
    fn=sort_and_visualize,
    inputs=gr.Textbox(label="Enter numbers to sort (comma-separated, no spaces)"), #creates the input fields
    outputs=[
        gr.Textbox(label="Sorted List"), #outputs the sorted list
        gr.Gallery(label="Sorting Visualization", show_label=False) #creates the gallery to show the generated graphs
    ],
    title="Sorting Algorithm Visualizer", #creates a title
    description="Enter a list of numbers (comma-separated, no spaces) to see how they are sorted." #creates a description
)

if __name__ == "__main__":
    iface.launch() #launches the interactive demo and gives the user the link to follow