public class Solution
{
    public bool ContainsDuplicate(int[] nums)
    {
        HashSet<int> set = new HashSet<int>();


        foreach (int x in nums)
        {
            if (set.Contains(x)) return true;
            set.Add(x);
        }
        return false;
    }

    public bool IsAnagram(string s, string t)
    {
        if (s.Length != t.Length) return false;
        if (s == t) return true;

        Dictionary<char, int> sCounts = new Dictionary<char, int>();
        Dictionary<char, int> tCounts = new Dictionary<char, int>();

        for (int i = 0; i < s.Length; i++)
        {
            sCounts[s[i]] = 1 + (sCounts.ContainsKey(s[i]) ? sCounts[s[i]] : 0);
            tCounts[t[i]] = 1 + (tCounts.ContainsKey(t[i]) ? tCounts[t[i]] : 0);
        }

        foreach (char c in sCounts.Keys)
        {
            int tCount = tCounts.ContainsKey(c) ? tCounts[c] : 0;
            if (sCounts[c] != tCount) return false;
        }
        return true;
    }

    public int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> dict = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int complement = target - nums[i];
            if (dict.ContainsKey(complement)) return new int[] { dict[complement], i };
            dict[nums[i]] = i;
        }
        return new int[] { };
    }

}









