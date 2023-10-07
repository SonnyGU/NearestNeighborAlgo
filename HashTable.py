class HashTable:
    def __init__(self, cap=50):
        self.table = [None] * cap  # initializes all field to None
        self.deleted = "Deleted"  # Marker for a deleted item

    #  Reset the hash table, clearing all stored items.
    def clear_table(self):
        self.table = [None] * len(self.table)

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
            self.table[idx] = self.deleted  # Remove an entry from the hash table based on its key.

    def keys(self):
        return sorted([entry[0] for entry in self.table if entry is not None and entry != self.deleted])  # Return a list of
        # all active keys in the hash table
