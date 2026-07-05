class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.items = []

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        h = hash(key)
        index = h % self.size
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.items.append((key, value, h, index))

    def display(self):
        print("Ключ Хэш  Индекс  Корзина")
        print("-" * 60)
        for key, value, h, idx in self.items:
            bucket_contents = self.table[idx]
            keys_in_bucket = [k for k, v in bucket_contents]
            print(f"{key:<10} {h:<20} {idx:<7} {keys_in_bucket}")

ht = HashTable(5)

ht.set("cat", "кот")
ht.set("dog", "собака")
ht.set("apple", "яблоко")
ht.set("banana", "банан")
ht.set("table", "стол")
ht.set("python", "питон")

ht.display()
