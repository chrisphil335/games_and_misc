

def file_content(file):
    try:
        with open(file, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("The file does not exist.")
        content = ""
    return content


def test_file_content():
    print("Testing with an existing file:")
    print(file_content("test_file.txt"))
    print("Testing with a non-existent file:")
    print(file_content("missing_file.txt"))


def write_to_file(file, content):
    try:
        with open(file, "w") as f:
            f.write(content)
    except FileNotFoundError:
        print(f"The file {file} was not found.")
    except PermissionError:
        print(f"You do not have permission to write to {file}.")
    except Exception as e:
        print(f"An error occured {e}")


def test_write_to_file():
    print("Testing with an existing file:")
    write_to_file("test_file.txt", "This is a test file.")
    with open("test_file.txt", "r") as f:
        print(f.read())
    print("Testing writing to a non-existent directory")
    write_to_file("non-existent_directory/test_file.txt", "This test should fail")


def append_to_file(file, content):
    with open(file, "a") as file:
        file.write(content)


def test_all_functions():
    test_file_content()
    test_write_to_file()


def main():
    test_all_functions()


if __name__ == "__main__":
    main()