class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false; }

        unordered_map<char, int> seenC;
        unordered_map<char, int> seenT;

        for (int i = 0; i < s.length(); i++) {
            seenC[s[i]]++;
            seenT[t[i]]++;
        }
        return seenC == seenT;
    }
};
