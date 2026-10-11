
import csv
import random
import time


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root

        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left

            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

            else:
                return

    def search(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node


class HashTable:
    def __init__(self, capacity=1024):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def insert(self, key):
        bucket = self.buckets[self._index(key)]

        if key not in bucket:
            bucket.append(key)

    def search(self, key):
        bucket = self.buckets[self._index(key)]
        return key in bucket

    def delete(self, key):
        bucket = self.buckets[self._index(key)]

        if key in bucket:
            bucket.remove(key)


def measure(function):
    start = time.perf_counter()
    function()
    return time.perf_counter() - start


def benchmark(structure_name, size, keys, targets, repeats=3):
    results = []

    for operation in ("insert", "search", "delete"):
        timings = []

        for _ in range(repeats):
            if structure_name == "BST":
                structure = BST()
            else:
                structure = HashTable(capacity=max(1, size * 2))

            if operation == "insert":
                elapsed = measure(
                    lambda: [structure.insert(k) for k in keys]
                )

            else:
                for key in keys:
                    structure.insert(key)

                if operation == "search":
                    elapsed = measure(
                        lambda: [structure.search(k) for k in targets]
                    )
                else:
                    elapsed = measure(
                        lambda: [structure.delete(k) for k in targets]
                    )

            timings.append(elapsed)

        results.append({
            "structure": structure_name,
            "elements": size,
            "operation": operation,
            "average_seconds": sum(timings) / repeats
        })

    return results


def main():
    all_results = []
    random.seed(42)

    for size in (100, 1000, 10000):
        keys = random.sample(range(size * 10), size)
        targets = random.sample(keys, size)

        print(f"\nTesting {size} elements")

        for name in ("BST", "Hash Table"):
            results = benchmark(name, size, keys, targets)
            all_results.extend(results)

            for result in results:
                print(
                    f"{name:10} | "
                    f"{result['operation']:6} | "
                    f"{result['average_seconds']:.6f} seconds"
                )

    with open("results.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "structure",
                "elements",
                "operation",
                "average_seconds"
            ]
        )
        writer.writeheader()
        writer.writerows(all_results)

    print("\nResults saved to results.csv")


if __name__ == "__main__":
    main()
