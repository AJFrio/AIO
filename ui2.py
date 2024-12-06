import TKinterModernThemes as TKMT
from tkinter import messagebox, Text, Entry
import threading
from main import ComputerUseAgent

class App(TKMT.ThemedTKinterFrame):
    def __init__(self):
        # Read API key from file
        with open("key.txt", "r") as f:
            api_key = f.read().split("\n")[0].split("=")[1].strip()
            
        self.agent = ComputerUseAgent(api_key)
        
        # Initialize the themed frame
        super().__init__("AIO", "sun-valley", "dark")
        
        # Create main input frame
        self.input_frame = self.addLabelFrame("INSTRUCTIONS")
        
        # Create a frame for the text input and button
        text_frame = self.input_frame.addFrame("text_container")
        
        # Text input field
        self.input_text = Text(
            text_frame.master,
            wrap="word",
            width=40,
            height=4
        )
        
        # OR Option 2: Using Entry widget (single line only)
        # self.input_text = Entry(
        #     text_frame.master,
        #     width=80
        # )
        
        self.input_text.grid(row=0, column=0, pady=5)
        
        # Send button - using AccentButton for better visibility
        text_frame.AccentButton(
            "SEND",
            lambda: threading.Thread(target=self.send_instructions).start(),
            row=1  # Place it below the text input
        )

        self.run()

    def send_instructions(self):
        user_input = self.input_text.get("1.0", "end-1c").strip()
        if user_input:
            # Disable the input field and button while processing
            self.input_text.config(state='disabled')
            
            result = self.agent.run_agent_loop(user_input)
            
            # Re-enable the input field
            self.input_text.config(state='normal')
        else:
            messagebox.showwarning("Input Required", "Please enter some instructions.")

if __name__ == "__main__":
    App()
