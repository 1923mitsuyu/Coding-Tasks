var romanToInt = function(s) {
    let ans = 0; 
    let m = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    };

    for (let i = 0; i < s.length; i++) { 
        if (i < s.length - 1 && m[s[i]] < m[s[i + 1]]) {
            ans += m[s[i + 1]] - m[s[i]]
            i = i + 1
        } else {
            ans += m[s[i]];
        }
    }

    return ans;
};

console.log(romanToInt("MCMXCIV"))