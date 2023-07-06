from collections import (
    deque, 
    Counter, 
    namedtuple, 
    defaultdict
)

# 1 namedtuple - 3D 座標
print("=" * 20)
point_3d = namedtuple('point_xyz', ['x', 'y', 'z'])
point_a = point_3d(1, 2, 3)
point_b = point_3d(7, 9, 8)
# a = (1, 2, 3)  b = (7, 9, 8)
print(point_a, point_b)
# ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)**0.5
distance_of_ab = \
    ((point_a.x - point_b.x)**2 + \
     (point_a.y - point_b.y)**2 + \
     (point_a.z - point_b.z)**2) ** 0.5

print(distance_of_ab)

# 2 Counter
print("=" * 20)
news = '''
When Muhsinah Morris stepped onto the central quad of the Morehouse College campus in Atlanta, Georgia, she cried.

“We hadn’t been on campus for almost a year,” she recalls. “It was amazing. You hear the birds chirping and everything.”

It was 2021, and Morehouse, like many other schools and universities during the Covid-19 pandemic, had been closed since lockdowns began in March 2020.

In fact, it was still closed. Morris wasn’t really standing in the quad — she was standing in Morehouse’s “Metaversity” digital twin.

Morehouse College is the world’s first Metaversity, an interactive, virtual learning space based on real or imagined environments.

“(It) became our solution to increase attendance rates, reduce student recidivism, and make sure that they continue to persist in their majors,” says Morris, Morehouse’s Metaversity director, who at the time was academic program director. “We wanted our students to be more engaged than just sitting in another Zoom classroom.”
'''

news = news.lower()
news = news.replace('\n', ' ')
news = news.split()
word_counter = Counter(news)
# print(word_counter)
print(word_counter.most_common(5))
# char_counter = Counter("This is a test for python collection counter .")
# print(char_counter)

# 3 double-end queue
print("=" * 20)
deque_a = deque()  # l = list()
deque_a.append('A')
deque_a.extend(['1', '2', '3'])
deque_a.pop()
print(deque_a)
deque_a.appendleft("Z")
deque_a.extendleft(['4', '5', '6'])
deque_a.popleft()
print(deque_a)
deque_a = deque_a + deque('3')
print(deque_a)
deque_a.rotate()
print(deque_a)
deque_b = deque([1, 2, 3], maxlen=5)
deque_b.append(4)
deque_b.append(5)
deque_b.append(6)
print(deque_b)
deque_b.appendleft(7)
print(deque_b)


# 4 defaultdict
print("=" * 20)
normal_dict = {
    1:"A",
    2:"B"
}
print("Get with default value: ", normal_dict.get(3, 'C')) # (每次拿都要設定預設值) 拿3這個key的時候, 如果拿不到, 就得到C
print("Get without default value", normal_dict.get(3))

# normal_dict[3] = 'C'
normal_dict.setdefault(3, 'C') # 預設某個key的value
print("Aftwer dict set default value by key", normal_dict[3])
print(normal_dict)

dd = defaultdict(list)
dd.update(normal_dict) # dd 把 normal_dict 的內容一起合併進來
print(dd)
print(f"****{dd[5]}****")