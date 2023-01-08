import argparse                      # Импорт и создание парсера
parser = argparse.ArgumentParser()


parser.add_argument('ind', type=str) # Добавление аргументов
parser.add_argument('outd', type=str)
args = parser.parse_args()


texts = open(args.ind).readlines()
output1file = args.outd
texts = texts.split(' ')
scores = []
result = []


def distance(str_1, str_2):         # Функция Левенштейна
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


for word1 in range(len(texts) // 2):
    txt1 = open(texts[word1]).read().split(' ')
    txt2 = open(texts[word1 + 1]).read().split(' ')
    for word1, word2 in zip(txt1, txt2):
        word1 = word1.ljust(len(word2), ' ')
        word2 = word2.ljust(len(word1), ' ')
        scores.append(distance(word1, word2))
    result.append(sum(scores) / (len(txt1)))


output1file = open(output1file, 'w+')
output1file.write(str(result))