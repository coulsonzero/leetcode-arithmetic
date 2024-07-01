'''
@title: 求1000以内的所有质数
@time: 2024.7.1
'''

def prime(n):
    nums = []
    for i in range(2, n):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            nums.append(i)
    print(nums)

if __name__ == '__main__':
    prime(1000)

