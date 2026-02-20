with open('source.txt', 'r') as source_file:
  with open('destination.txt','w') as destination_file:
    for line in source_file:
      destination_file.write(line)