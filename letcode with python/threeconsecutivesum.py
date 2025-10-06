from typing import List

def sumofthree(num: int) -> List[int]:
	if num % 3 != 0:
		return []
	mid = num // 3
	return [mid - 1, mid, mid + 1]

num = int(input("Enter the number to check if it has a consecutive three sum: "))
resu = sumofthree(num)
print(resu)
    