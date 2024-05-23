import tkinter as tk
from tkinter import*

def calculate_distance():
    string1 = entry_string1.get()
    string2 = entry_string2.get()
    distance = levenshtein_distance(string1, string2)
    label_result.config(text=f"Edit distance: {distance}")

def levenshtein_distance(s1, s2):
    # Create a matrix to store the edit distances
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize the first row and column of the matrix
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for j in range(len(s2) + 1):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                           dp[i][j - 1] + 1,  # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution

    # Return the bottom-right cell of the matrix
    return dp[-1][-1]

# Create the main application window
root = tk.Tk()
root.title("Minimum Edit Distance Calculator")
root.geometry("400x300")
root.resizable(width=False, height=False)

#Create frame for the elements 
fr1=Frame(width="500", height="300", background="#EBE3D5" )
fr1.pack(fill="both", expand=True)


# Create input fields for the strings
label_string1 = tk.Label(fr1, text="Word 1:" ,font=("Magneto",15), background="#EBE3D5")
label_string1.place(x=50, y=50)
entry_string1 = tk.Entry(fr1, font=20)
entry_string1.place(x=150, y=50)


label_string2 = tk.Label(fr1, text="Word 2:", background="#EBE3D5",font=("Magneto",15))
label_string2.place(x=50, y=130)
entry_string2 = tk.Entry(fr1, font=20)
entry_string2.place(x=150, y=130)



# Create button to calculate the distance()
calculate_button = tk.Button(fr1, text="Calculate Distance", font=10, background="#B0A695",
                             activebackground="#776B5D" ,cursor="hand2", command=calculate_distance)
calculate_button.place(x=170, y=190)

# Create label to display the result
label_result = tk.Label(fr1, text="", background="#EBE3D5",font=("Magneto",15))
label_result.place(x=175, y=230)

# Start the Tkinter event loop
root.mainloop()







