import os
import random

# Used to securely store your API key
from google.colab import userdata
import google.generativeai as genai
from google.generativeai import GenerativeModel
from google.generativeai.types.generation_types import GenerateContentResponse

# Or use `os.getenv('GEMINI_API_KEY')` to fetch an environment variable.
GEMINI_API_KEY: str = userdata.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
client: GenerativeModel = genai.GenerativeModel("gemini-1.5-flash")

def print_llm_response(prompt):
    """Prints response from LLM based on the given prompt."""
    llm_response = get_llm_response(prompt)
    print(llm_response)

def get_llm_response(prompt):
    """Generates response from LLM based on the given prompt."""
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion: GenerateContentResponse = client.generate_content(prompt)
        response = completion.text
        return response
    except TypeError as e:
        print("Error:", str(e))

def get_chat_completion(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion: GenerateContentResponse = client.generate_content(prompt)
    response = completion.text
    return response

def get_dog_age(human_age):
    """Returns age in dog years."""
    return human_age / 7

def get_goldfish_age(human_age):
    """Returns age in goldfish years."""
    return human_age / 5

def get_cat_age(human_age):
    if human_age <= 14:
        cat_age = human_age / 7
    else:
        cat_age = 2 + (human_age - 14) / 4
    return cat_age

def get_random_ingredient():
    """Returns a random smoothie ingredient."""
    ingredients = [
        "rainbow kale", "glitter berries", "unicorn tears", "coconut", "starlight honey",
        "lunar lemon", "blueberries", "mermaid mint", "dragon fruit", "pixie dust",
        "butterfly pea flower", "phoenix feather", "chocolate protein powder", "grapes", "hot peppers",
        "fairy floss", "avocado", "wizard's beard", "pineapple", "rosemary"
    ]
    return random.choice(ingredients)

def get_random_number(x, y):
    """Returns a random integer between x and y, inclusive."""
    return random.randint(x, y)

def calculate_llm_cost(characters, price_per_1000_tokens=0.015):
    tokens = characters / 4
    cost = (tokens / 1000) * price_per_1000_tokens
    return f"${cost:.4f}"

def upload_txt_file(file_path, destination_dir):
    """Uploads a .txt file to the specified directory."""
    if not os.path.isfile(file_path):
        return "File does not exist."
    
    if not file_path.endswith('.txt'):
        return "Only .txt files are allowed."
    
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    try:
        destination_path = os.path.join(destination_dir, os.path.basename(file_path))
        os.rename(file_path, destination_path)
        return f"File uploaded successfully to {destination_path}"
    except Exception as e:
        return f"Error uploading file: {str(e)}"


# Define the directory path
directory_path = "/content"

def list_files_in_directory(directory_path):
    """Lists all files in the specified directory."""
    if not os.path.isdir(directory_path):
        return "Directory does not exist."
    
    try:
        files = os.listdir(directory_path)
        return files if files else "No files found in the directory."
    except Exception as e:
        return f"Error listing files: {str(e)}"

# Call the function with the directory path as an argument
files = list_files_in_directory(directory_path)

# Print the result
print(files)
    
# Empty `upload_txt_file` placeholder function to fulfill request
def upload_txt_file():
    """Uploads a .txt file to the specified directory."""
    # Your function logic here
    pass
