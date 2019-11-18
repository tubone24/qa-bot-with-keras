import glob
import codecs

file_list= glob.glob("../data/raw/*.txt")

with codecs.open("../data/interim/qa_list.txt", "w", "utf-8") as f:
    count = 0
    for file in file_list:
        with codecs.open(file, "r", "utf-8") as f2:
            for line in f2.readlines():
                count += 1
                f.write(line)
        print("count: {}".format(int(count / 4)))
