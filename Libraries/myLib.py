# 二分探索
import bisect
listA = [1,2,5,2,4,6,7,8,6,56,3,56,76,34,32,2,6,0,32,6,0] 
listA = sorted(listA)
x = 10
zeroindex = bisect.bisect_right(listA, x) #ソートされたリスト内で x の場所を探し、右側Indexを返す
clearlistA = listA[zeroindex:]	#0以下が存在しないリストを得る

# ユークリッドの互除法
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def lcm(a, b):
	return a * b // gcd (a, b)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors