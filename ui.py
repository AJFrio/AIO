import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
from main import ComputerUseAgent

def main():
    # Read API key from file
    with open("key.txt", "r") as f:
        api_key = f.read().strip()
        
    agent = ComputerUseAgent(api_key)
    
    # Create the Tkinter GUI
    root = tk.Tk()
    root.title("Computer Use Agent")

    # Set window size
    root.geometry("700x500")

    # Instruction Label
    instruction_label = tk.Label(root, text="Enter your instructions:")
    instruction_label.pack(pady=5)

    # Text input field
    input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
    input_text.pack(pady=5)

    # Send button
    send_button = tk.Button(root, text="Send", command=lambda: threading.Thread(target=send_instructions).start())
    send_button.pack(pady=5)

    # Output label
    output_label = tk.Label(root, text="Agent's response:")
    output_label.pack(pady=5)

    # Output text field
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, state='disabled')
    output_text.pack(pady=5)

    def send_instructions():
        user_input = input_text.get("1.0", tk.END).strip()
        if user_input:
            # Disable the input field and button while processing
            input_text.config(state='disabled')
            send_button.config(state='disabled')

            result = agent.run_agent_loop(user_input)

            # Display the result
            output_text.config(state='normal')
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result)
            output_text.config(state='disabled')

            # Re-enable the input field and button
            input_text.config(state='normal')
            send_button.config(state='normal')
        else:
            messagebox.showwarning("Input Required", "Please enter some instructions.")

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()

