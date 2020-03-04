from collections import deque
urutan = deque(["aaa","bbb","ccc","ddd"])
urutan.append("bbb")
urutan.append("abc")
urutan
urutan.popleft()
urutan.popleft()
#popleft digunakan untuk memanggil data paling kiri dari array lalu menghapusnya
