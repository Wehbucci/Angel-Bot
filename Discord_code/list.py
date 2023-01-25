blacklist = []

#the code reads from BlackList.txt and enters each word in a list to be used later on
with open('Blacklist.txt', 'r') as file:
    file_contents = file.readlines()

for line in file_contents:
    blacklist.append(line[:-1])
