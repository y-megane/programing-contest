S = list(input())

ans = 'Good'
for i in range(3):
    if S[i] == S[i+1]:
        ans = 'Bad'
print(ans)