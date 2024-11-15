var countPrimes = function(n) {
    let ans = 0;
    for (let i = 2; i < n; i++) {
        ans += isPrime(i)
    }
    return ans
};

function isPrime(x) {
    for (let i = 2; i < x; i++) {
        if (x % i == 0) {
            return false
        }
    }
    return true
}