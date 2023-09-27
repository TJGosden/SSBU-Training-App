import os

class File:
    def __init__(self):
        self.lineIndex = 0

    def search_list(self, fileName):
        fileIncrease = open(File.get_file_path(fileName), "r")
        trainingList = []
        with fileIncrease as filedata:
            inputFilelines = filedata.readlines()
            self.lineIndex = 1
            with open(File.get_file_path(fileName), 'w') as filedata:
                for textline in inputFilelines:
                    filedata.write(textline)
                    self.lineIndex += 1
                    trainingList += [textline]
            filedata.close()
        fileIncrease.close()
        return trainingList


    #Get the file path in which fileName is stored.
    def get_file_path(fileName):
        # Get the current directory (where the script is located)
        script_directory = os.path.dirname(os.path.abspath(__file__))
        # Name of the file you're searching for
        target_file_name = fileName

        # Construct the full path to the target file
        target_file_path = os.path.join(script_directory, target_file_name)
        #Create the folder "obs-countdown" if it doesn't already exist.
        if not os.path.exists(target_file_path):
            print(".txt File not found in the script directory.")
        #print(".txt found")
        return target_file_path

    def add_to_file(text, fileName):
        fileIncrease = open(File.get_file_path(fileName), "a")
        with fileIncrease as f:
            f.write("\n" + text)
        fileIncrease.close()

    def remove_from_file(self, itemIndex, fileName):
        file = open(File.get_file_path(fileName), "r")
        with file as filedata:
            inputFilelines = filedata.readlines()
            lineindex = 1
            with open(File.get_file_path(fileName), 'w') as filedata:
                for textline in inputFilelines:
                    if (textline != ""):
                        if (lineindex != int(itemIndex) + 1):
                            filedata.write(textline)
                    lineindex += 1
            filedata.close()
        file.close()
