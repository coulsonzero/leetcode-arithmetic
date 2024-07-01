var isUnique = function(astr) {
    let map = {}
    for (let c of astr) {
        map[c] = (map[c] || 0) + 1
    }

    for (let key in map) {
        if (map[key] > 1) {
            return false
        }
    }
    return true
};

