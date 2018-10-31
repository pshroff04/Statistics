N = int(input())
X = [int(x) for x in input().split()]
W = [int(w) for w in input().split()]

print('%.1f' % (sum([x*w for x,w in zip(X,W)])/sum(W)) )
