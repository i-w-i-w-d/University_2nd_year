import time

class JohnsonTrotter:
    def __init__(self, n):
        self.n = n
        self.current = list(range(1, n + 1)) #поточна перестановка
        self.dirs = [-1] * n #напрямок рухів елементів
        self.first = True

    def get_mobile(self):
        mobile = -1
        mobile_index = -1
        for i in range(self.n):

            if (self.dirs[i] == -1 and i > 0 and self.current[i] > self.current[i - 1]) or \
               (self.dirs[i] == 1 and i < self.n - 1 and self.current[i] > self.current[i + 1]):

                if mobile == -1 or self.current[i] > mobile:
                    mobile = self.current[i]
                    mobile_index = i

        return mobile, mobile_index

    def next_permutation(self): #повертає наступну перестановку, або none, якщо вже нема

        if self.first:
            self.first = False
            return self.current[:]

        mobile, mobile_index = self.get_mobile()

        if mobile == -1:
            return None

        swap_with = mobile_index + self.dirs[mobile_index]
        self.current[mobile_index], self.current[swap_with] = self.current[swap_with], self.current[mobile_index]
        self.dirs[mobile_index], self.dirs[swap_with] = self.dirs[swap_with], self.dirs[mobile_index]
        mobile_index = swap_with

        for i in range(self.n):

            if self.current[i] > mobile:
                self.dirs[i] *= -1

        return self.current[:]

    def generate_all(self): #ітерування всіх перестановок
        self.current = list(range(1, self.n + 1))
        self.dirs = [-1] * self.n
        self.first = True

        while True:
            p = self.next_permutation()
            if p is None:
                break

            yield p

if __name__ == "__main__":

    print("1-ші 50 перестановок на множині {1,2,3,4,5,6}:")
    jt = JohnsonTrotter(6)

    for i, p in enumerate(jt.generate_all()):

        if i >= 50:
            break
        print(f"{i+1}: {p}")

    print("\nЧас генерування перестановок")

    for n in range(5, 11):
        jt = JohnsonTrotter(n)
        start = time.time()
        count = 0
        for _ in jt.generate_all():
            count += 1
        elapsed = time.time() - start
        print(f"n={n}: {count} перестановок, час = {elapsed:.4f} c")
