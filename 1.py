#функция считает число каждого символа в строчке

# если у нас N букв сложность O(N^2) or O(N**2)

#set - множество - типо данных, который содержит в себе набор уникальных элементов, неупорядочный для питона
import time
def counter(s):# если у нас N букв сложность O(N^2) or O(N**2)
    for let in (s):
        count = 0
        for sub_let in (s):# число букв в целом
            if let == sub_let:
                count += 1
start=time.time()
for i in range(1000000):
    counter('queue')
end = time.time()
print(end-start)

def counter(s):#O(N**2) N число уникальных букв , самый быстрый метод работы программы
    for let in set(s):
        count = 0
        for sub_let in (s):# число букв в целом
            if let == sub_let:
                count += 1
        #print(let, count)
start=time.time()
for i in range(1000000):
    counter('queue')
end = time.time()
print(end-start)


def counter(s):#O(N)
    let_counter ={}
    for let in s:
        let_counter[let] =let_counter.get(let,0)+ 1
    #print(let_counter)
counter("aueua")
star=time.time()
for i in range(1000000):
    counter('queuq')
end = time.time()
print(end-start)

