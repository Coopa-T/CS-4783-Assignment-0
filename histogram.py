#Assignment 0, Question 1
import matplotlib.pyplot as plt

file = open("test.txt", "r+")
test_str = "The quick brown fox jumps over a lazy dog"
res = {}

for lines in file.read():
    res[lines] = res.get(lines, 0) + 1

print("Count is: \n" + str(res))
plt.hist(res, len(res), density=True)
plt.show()
file.close()
