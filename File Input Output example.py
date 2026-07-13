def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    name = "example.txt"
    text = "Hello, world!"
    
    write_file(name, text)
    print("File written.")
    
    data = read_file(name)
    print("File content:", data)
