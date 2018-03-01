# Luis Navarro
# Exercise number 5
# Formatting from Mohamed Noor from the forum (https://learnonline.gmit.ie/mod/forum/discuss.php?d=14986)

with open ("data/iris.csv") as a:
  for line in a:
    line = line.replace(',', ' ')
    line = line.rstrip()
    print(line[:11], line[12:16].strip())
