class HashTable:
    def __init__(self, cap=400):
        self.table = [None] * cap  # initializes all field to None
        self.deleted = "Deleted"  # Marker for a deleted item

    def clear_table(self):
        self.table = [None] * len(self.table)

    def display(self):
        for idx, entry in enumerate(self.table):
            if entry is not None and entry != self.deleted:
                print(f"Index: {idx}, Key: {entry[0]}, Value: {entry[1]}")

    def _hash(self, key):
        return sum(ord(char) for char in str(key))  # hashing the key

    def _probe(self, key):
        idx = self._hash(key) % len(self.table)
        original_idx = idx

        while self.table[idx] is not None and (self.table[idx] == self.deleted or self.table[idx][0] != key):
            idx = (idx + 1) % len(self.table)  # checking the next spot
            if idx == original_idx:  # in case all spots are filled
                raise Exception("Hash table is full!")

        return idx

    def insert(self, key, package):
        idx = self._probe(key)

        if self.table[idx] is not None and self.table[idx][0] == key:
            self.table[idx] = (key, package)  # updates existing package
        else:
            self.table[idx] = (key, package)  # inserts a new package

    def search(self, key):
        idx = self._probe(key)

        if self.table[idx] is not None and self.table[idx][0] == key:
            return self.table[idx][1]  # returns package
        return None

    def remove(self, key):
        idx = self._probe(key)

        if self.table[idx] is not None and self.table[idx][0] == key:
            self.table[idx] = self.deleted
