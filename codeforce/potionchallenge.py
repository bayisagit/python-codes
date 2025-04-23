def can_buy_potion(l, r, x, y, k):
    for a in range(l, r + 1):
        b = a / k
        if b.is_integer() and x <= b <= y:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    l, r, x, y, k = map(int, input().split())
    can_buy_potion(l, r, x, y, k)
