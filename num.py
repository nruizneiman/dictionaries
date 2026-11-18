with open("num.txt", "w", encoding="ascii", newline="\n") as f:
    for inicio in range(0, 10**8, 1_000_000):
        f.write("".join(f"{i:08d}\n" for i in range(inicio, inicio + 1_000_000)))