from pyspark import SparkContext
sc = SparkContext("local[*]", "App Name")

def split_line(line):
    strings = line.split(',')
    return (strings[0], strings[1], int(strings[2]), int(strings[3]))

def extract_population(data_point):
    return (data_point[3], 1)

def add_pops(pop_pairA, pop_pairB):
    popA = pop_pairA[0]
    countA = pop_pairA[1]
    popB = pop_pairB[0]
    countB = pop_pairB[1]
    return (popA + popB, countA + countB)

line_set = sc.textFile("./states.csv")
split_lines = line_set.map(split_line)
pop_pairs = split_lines.map(extract_population)
total_pop, total_count = pop_pairs.reduce(add_pops)

print("The average population is:")
print(total_pop/total_count)
