# import gradio as gr
import os

# Used to securely store your API key
from google.colab import userdata

import random


import google.generativeai as genai
# Or use `os.getenv('GEMINI_API_KEY')` to fetch an environment variable.
GEMINI_API_KEY : str = userdata.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

from google.generativeai import GenerativeModel
from google.generativeai.types.generation_types import GenerateContentResponse


client : GenerativeModel = genai.GenerativeModel("gemini-1.5-flash")




def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    llm_response = get_llm_response(prompt)
    print(llm_response)


def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
    a string.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion  : GenerateContentResponse = client.generate_content(prompt)
        response = completion.text
        return response
    except TypeError as e:
        print("Error:", str(e))


def get_chat_completion(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion : GenerateContentResponse = client.generate_content(prompt)
    response = completion.text
    return response


# def open_chatbot():
#     """This function opens a Gradio chatbot window that is connected to OpenAI's GPT3.5 model."""
#     gr.close_all()
#     gr.ChatInterface(fn=get_chat_completion).launch(quiet=True)

def get_dog_age(human_age):
    """This function takes one parameter: a person's age as an integer and returns their age if
    they were a dog, which is their age divided by 7. """
    return human_age / 7

def get_goldfish_age(human_age):
    """This function takes one parameter: a person's age as an integer and returns their age if
    they were a dog, which is their age divided by 5. """
    return human_age / 5

def get_cat_age(human_age):
    if human_age <= 14:
        # For the first 14 human years, we consider the age as if it's within the first two cat years.
        cat_age = human_age / 7
    else:
        # For human ages beyond 14 years:
        cat_age = 2 + (human_age - 14) / 4
    return cat_age

def get_random_ingredient():
    """
    Returns a random ingredient from a list of 20 smoothie ingredients.
    
    The ingredients are a bit wacky but not gross, making for an interesting smoothie combination.
    
    Returns:
        str: A randomly selected smoothie ingredient.
    """
    ingredients = [
        "rainbow kale", "glitter berries", "unicorn tears", "coconut", "starlight honey",
        "lunar lemon", "blueberries", "mermaid mint", "dragon fruit", "pixie dust",
        "butterfly pea flower", "phoenix feather", "chocolate protein powder", "grapes", "hot peppers",
        "fairy floss", "avocado", "wizard's beard", "pineapple", "rosemary"
    ]
    
    return random.choice(ingredients)

def get_random_number(x, y):
    """
        Returns a random integer between x and y, inclusive.
        
        Args:
            x (int): The lower bound (inclusive) of the random number range.
            y (int): The upper bound (inclusive) of the random number range.
        
        Returns:
            int: A randomly generated integer between x and y, inclusive.

        """
    return random.randint(x, y)

def calculate_llm_cost(characters, price_per_1000_tokens=0.015):
    tokens = characters / 4
    cost = (tokens / 1000) * price_per_1000_tokens
    return f"${cost:.4f}"
    def upload_txt_file(file_path, destination_dir):
    """Uploads a .txt file to the specified directory.
    
    Args:
        file_path (str): The path to the .txt file to upload.
        destination_dir (str): The directory to upload the file to.

    Returns:
        str: The path to the uploaded file if successful, or an error message.
    """
    if not os.path.isfile(file_path):
        return "File does not exist."
    
    if not file_path.endswith('.txt'):
        return "Only .txt files are allowed."
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    try:
        # Copy the file to the destination directory
        destination_path = os.path.join(destination_dir, os.path.basename(file_path))
        os.rename(file_path, destination_path)
        return f"File uploaded successfully to {destination_path}"
    except Exception as e:
        return f"Error uploading file: {str(e)}"


# Function to list all files in a directory
def list_files_in_directory(directory_path):
    """Lists all files in the specified directory.
    
    Args:
        directory_path (str): The path to the directory to list files from.
    
    Returns:
        list: A list of file names in the directory.
    """
    if not os.path.isdir(directory_path):
        return "Directory does not exist."
    
    try:
        files = os.listdir(directory_path)
        return files if files else "No files found in the directory."
    except Exception as e:
        return f"Error listing files: {str(e)}"