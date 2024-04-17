import os
from typing_extensions import override
from openai import AssistantEventHandler
import requests

def download_image(url, filename):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open a binary file in write mode
        with open(filename, 'wb') as file:
            file.write(response.content)
        print("Image downloaded and saved as", filename)
    else:
        print("Failed to retrieve image. Status code:", response.status_code)

def write_text_to_file(folder, filename, text_to_write):
    """
    Writes text to a file within a specified folder. Creates the folder if it does not exist.
    
    Args:
    folder (str): The directory to store the file.
    filename (str): The name of the file to create.
    text_to_write (str): The text to write to the file.
    """
    # Ensure the folder exists
    os.makedirs(folder, exist_ok=True)

    if "." not in filename: filename += ".txt"
    
    # Construct the full file path
    file_path = os.path.join(folder, f"{filename}")
    
    # Write the text to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text_to_write)
    print(f"Text has been written to {file_path}")

def number_to_four_digit_string(num):
    digit_string = str(num)
    remaining_length = 4 - len(digit_string)
    return remaining_length * "0" + digit_string

class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 