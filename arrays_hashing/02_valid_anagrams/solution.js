// SOLUTION 1
// class Solution {
//     /**
//      * @param {string} s
//      * @param {string} t
//      * @return {boolean}
//      */
//     isAnagram(s, t) {
//         if (s.length !== t.length) return false;
//         let sorted_s = s.split("").sort().join("")
//         let sorted_t = t.split("").sort().join("")
//         for (let i = 0; i < sorted_s.length; i++) {
//             if (sorted_s[i] !== sorted_t[i]) return false
//         }
//         return true;
//     }
// }

// value = new Solution()
// result = value.isAnagram("racecar", "carrace")
// console.log(result)

// SOLUTION 2
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        let hash_values = {}
        for (let i = 0; i < s.length; i++) {
            if (!(s[i] in hash_values)) hash_values[s[i]] = 0;
            hash_values[s[i]] += 1
            if (!(t[i] in hash_values)) hash_values[t[i]] = 0;
            hash_values[t[i]] -= 1
        }
        for (let value of Object.values(hash_values)) {
            if (value !== 0 ) return false
        }
        return true;
    }
}

value = new Solution()
result = value.isAnagram("racecar", "carrace")
console.log(result)
