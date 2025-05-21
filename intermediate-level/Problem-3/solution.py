### Problem-3: Implement an LRU Cache (Least Recently Used)

from collections import OrderedDict


class LruCache:
	def __init__(self, max_cap):
		self.cache = OrderedDict()
		self.max_cap = max_cap

	def get(self, key):
		if key not in self.cache:
			return "Key is not in cache"
		
		self.cache.move_to_end(key)
		return self.cache.get(key)
	
	def put(self, key, val):
		if key in self.cache:
			self.cache.pop(key)
		elif len(self.cache) >= self.max_cap:
			self.cache.popitem(last=False)
		
		self.cache[key] = val

lru = LruCache(2)
lru.put(1, 1)
print(lru.get(1))
lru.put(2, 2)
lru.put(3, 3)
print(lru.get(1))
print(lru.get(2))  
lru.put(4, 4)
print(lru.get(1))  
print(lru.get(3))
print(lru.get(4))
