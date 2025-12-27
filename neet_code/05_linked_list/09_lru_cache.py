"""
LRU Cache

class LRUCache:

    def __init__(self, capacity: int):

    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:

Implement the Least Recently Used (LRU) cache class LRUCache.
The class should support the following operations

LRUCache(int capacity) Initialize the LRU cache of size capacity.
int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
Output:
[null, null, 10, null, null, 20, -1]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 10);  // cache: {1=10}
lRUCache.get(1);      // return 10
lRUCache.put(2, 20);  // cache: {1=10, 2=20}
lRUCache.put(3, 30);  // cache: {2=20, 3=30}, key=1 was evicted
lRUCache.get(2);      // returns 20
lRUCache.get(1);      // return -1 (not found)

Constraints:
1 <= capacity <= 100
0 <= key <= 1000
0 <= value <= 1000

"""
from typing import Union


class CacheNode:
    def __init__(self, key: Union[int, str] = None, val: Union[int, str] = None,
                 prev_node: "CacheNode" = None, next_node: "CacheNode" = None):
        self.key = key
        self.val = val
        self.prev = prev_node
        self.next = next_node

    def __repr__(self) -> str:
        return str(self.val)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: dict[Union[int, str], CacheNode] = dict()
        self.head = CacheNode(val=-1)
        self.tail = CacheNode(val=-2)
        self.head.next, self.tail.prev = self.tail, self.head

    def __repr__(self) -> str:
        return str(self.data)

    def _move_node_to_front(self, cache_node: CacheNode):

        # move node to front of linked list
        if cache_node.next:
            cache_node.next.prev = cache_node.prev
        if cache_node.prev:
            cache_node.prev.next = cache_node.next

        # insert right after head
        cache_node.prev = self.head
        cache_node.next = self.head.next
        self.head.next.prev = cache_node
        self.head.next = cache_node

    def get(self, key: int) -> int:

        # if the value is in the cache
        val = -1
        if key in self.data:

            # get data
            cache_node = self.data[key]

            # move node to front of linked list
            self._move_node_to_front(cache_node=cache_node)

            # get value
            val = cache_node.val

        return val

    def put(self, key: int, value: int) -> None:
        # if the value is in the cache
        if key in self.data:
            cache_node = self.data[key]
            cache_node.val = value
            self._move_node_to_front(cache_node=cache_node)

        # if the value is not in the cache
        else:
            cache_node = CacheNode(key=key, val=value)
            self._move_node_to_front(cache_node=cache_node)
            self.data[key] = cache_node
            if len(self.data) > self.capacity:
                key = self.tail.prev.key
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
                del self.data[key]


def main():
    lru_cache = LRUCache(2)
    lru_cache.put(1, 10)
    print(lru_cache.get(1))
    lru_cache.put(2, 20)
    lru_cache.put(3, 30)
    print((lru_cache.get(2)))
    print((lru_cache.get(1)))


if __name__ == '__main__':
    main()
