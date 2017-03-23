import os
import subprocess

inputFormat = input("What format are you inputing?")
outputFormat = input("What format do you want to make?")
inputDirectory = input("What is the path to the input files?")
outputDirectory = input("Where do you want the new files to be placed?")


def traverse(treename, mp3treename):
    extra = '"'
    for item in os.listdir(treename):
        if os.path.isdir(treename+"/"+item):
            os.makedirs(mp3treename+"/"+item)
            traverse(treename+"/"+item, mp3treename+"/"+item)
        else:
            if len(item) >= len(inputFormat) and item[-len(inputFormat):]==inputFormat:
                new = item[:-len(inputFormat)]+outputFormat
                subprocess.call("ffmpeg -i "+extra+treename+"/"+item+extra+" "+extra+mp3treename+"/"+new+extra)

traverse(inputDirectory, outputDirectory)
