import json






class Files:
    def __init__(self, file_name):
        self.file_name = file_name

    def file_output(self):
        with open(self.file_name, 'r+') as file:
            file_content = json.load(file)

        return file_content

