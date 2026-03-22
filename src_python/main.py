#!/usr/bin/env python3

import sys
import os

from project import Project
from project_reader import ProjectReader

import json

def main():
    try:
        input_file = sys.argv[1] 
    except:
        print("Usage: {} <input_file.txt>".format(sys.argv[0]))

    project = Project()
    project_reader = ProjectReader()

    project_reader.read(project, input_file)

    with open("output.json", "w") as file:
        file.write(json.dumps(project.to_dict(), indent=4))
    
    with open("output.json", "r") as file:
        for line in file:
            print(line.rstrip())

if __name__ == "__main__":
    main()

