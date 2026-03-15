from src import select_file, read_file

menu_path = select_file.select_file()
result = read_file.read_file(menu_path)

print(result)