class Solution {
public:

    string encode(vector<string>& strs) {
        if (strs.empty()){
            return "";
        }
        
        string oneString;

        for (const string& s : strs) {
            oneString += to_string(s.size()) + '#' + s;
        }

        return oneString;
    }

    vector<string> decode(string s) {
        if (s.empty()){
            return {};
        } 

        vector<string> vecString;
        int i = 0;

        while (i < s.size()) {
            int j = i;
            while (s[j] != '#'){
                j++;
            }

            int length = stoi(s.substr(i, j - i));
            i= j + 1;
            j = i + length;
            vecString.push_back(s.substr(i, length));
            i = j;
        }
        return vecString;
    }
};
