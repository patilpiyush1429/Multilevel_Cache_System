class CacheLevel:
    def __init__(self, size, eviction_policy):
        self.size = size
        self.eviction_policy = eviction_policy
        self.cache = {}
        self.access_order = []

    def get(self, key):
        if key in self.cache:
            if self.eviction_policy == 'LRU':
                self.access_order.remove(key)
                self.access_order.append(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            if self.eviction_policy == 'LRU':
                self.access_order.remove(key)
        elif len(self.cache) >= self.size:
            self.evict()

        self.cache[key] = value
        if self.eviction_policy == 'LRU':
            self.access_order.append(key)

    def evict(self):
        if self.eviction_policy == 'LRU':
            lru_key = self.access_order.pop(0)  # Evict least recently used
            del self.cache[lru_key]
        elif self.eviction_policy == 'LFU':
            lfu_key = min(self.cache, key=lambda k: self.cache[k][1])  # Find least frequently used
            del self.cache[lfu_key]

    def display(self):
        print(self.cache)


class MultilevelCache:
    def __init__(self):
        self.cache_levels = []

    def addCacheLevel(self, size, eviction_policy):
        self.cache_levels.append(CacheLevel(size, eviction_policy))

    def removeCacheLevel(self, level):
        if 0 <= level < len(self.cache_levels):
            self.cache_levels.pop(level)
            print(f"Cache level {level + 1} removed.")
        else:
            print("Invalid level number.")

    def get(self, key):
        for cache in self.cache_levels:
            value = cache.get(key)
            if value:
                return value
        return None

    def put(self, key, value):
        if self.cache_levels:
            self.cache_levels[0].put(key, value)

    def displayCache(self):
        for i, cache in enumerate(self.cache_levels):
            print(f"Cache Level L{i + 1}:")
            cache.display()


def main():
    cache_system = MultilevelCache()

    while True:
        print("\n1. Add Cache Level")
        print("2. Insert Key-Value Pair")
        print("3. Get Value by Key")
        print("4. Remove Cache Level")
        print("5. Display Cache")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            size = int(input("Enter cache size: "))
            eviction_policy = input("Enter eviction policy (LRU or LFU): ")
            cache_system.addCacheLevel(size, eviction_policy)
            print(f"Added cache level with size {size} and policy {eviction_policy}.")

        elif choice == '2':
            key = input("Enter key: ")
            value = input("Enter value: ")
            cache_system.put(key, value)
            print(f"Inserted key-value pair ({key}, {value}) into L1.")

        elif choice == '3':
            key = input("Enter key to retrieve: ")
            result = cache_system.get(key)
            if result:
                print(f"Value found: {result}")
            else:
                print("Cache miss! Value not found.")

        elif choice == '4':
            level = int(input("Enter cache level to remove (1 for L1, 2 for L2, ...): ")) - 1
            cache_system.removeCacheLevel(level)

        elif choice == '5':
            cache_system.displayCache()

        elif choice == '6':
            print("Exiting.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

