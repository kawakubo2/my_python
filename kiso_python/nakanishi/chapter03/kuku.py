for i in range(1, 10):
    for j in range(1, 10):
        if i * j > 30:
            break
        print(f"{i * j:3}", end="")
    else:
        print()
        continue
    break

