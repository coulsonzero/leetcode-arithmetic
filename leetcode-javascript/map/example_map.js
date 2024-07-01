function main() {
    let nums = [7, 3, 1, 2, 7, 9, 7, 2]
    let map = {}
    for (let num of nums) {
        map[num] = (map[num] || 0) + 1
    }

    console.log(map)
    // { '1': 1, '2': 2, '3': 1, '7': 3, '9': 1 }
}

// main()


hello = () => {
    console.log("hello, world")
}
hello()