def load_knowledge_base(filename):
    # Reads the text file to use as context
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except IOError as e:
        print(f"Error loading knowledge base from {filename}: {e}")


def save(filename, content):
    # Saves the generated content to a text file
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError as e:
        print(f"Error saving file {filename}: {e}")
