
import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;

public class Main {
  public static void main(String[] args) {

    int[] input = { 1, 2, 3, 0, 0, 0 };
    int[] nums2 = { 2, 5, 6 };
    mergeSortedArray(input, 3, nums2, 3);
    System.out.println(Arrays.toString(input));
  }

  public static int removeElement(int[] nums, int value) {
    int K = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != value) {
        nums[k] = nums[i];
        k += 1;
      }
      return k;
    }
  }

  public static void mergeSortedArray(int[] numbs1, int m, int[] numbs2, int n) {
    int p1 = m - 1;
    int p2 = m - 1;
    int p = m + n - 1;
    while (p1 >= 0 && p2 >= 0) {
      if (numbs1[p1] >= numbs2[p2]) {
        numbs1[p] = numbs1[p1];
        p1 -= 1;
      } else {

        numbs1[p] = numbs2[p2];
        p2 -= 1;

      }
      p -= 1;

    }
    System.arraycopy(numbs2, 0, numbs1, 0, p2 + 1);

  }

  public static int maxProfit(int[] prices) {
    int res = 0;
    int lowest = prices[0];
    for (int price : prices) {

      if (price < lowest) {
        lowest = price;

      }
      res = Math.max(res, price - lowest);

    }
    return res;
  }

  public static int[] topkFrequent(int[] nums, int k) {
    int[] arr = new int[k];
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int num : nums)
      map.put(num, map.getOrDefault(num, 0) + 1);
    PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
        (a, b) -> a.getValue() - b.getValue());
    for (Map.Entry<Integer, Integer> it : map.entrySet()) {
      pq.add(it);
      if (pq.size() > k)
        pq.poll();
    }
    int i = k;
    while (!pq.isEmpty()) {
      arr[--i] = pq.poll().getKey();
    }
    return arr;
  }

  public static int[] RunningSum(int[] nums) {
    AtomicInteger sum = new AtomicInteger();
    return Arrays.stream(nums).map(sum::addAndGet).toArray();
  }

  public static int pivotIndex(int[] nums) {
    int Total = Arrays.stream(nums).sum();
    int lefNum = 0;
    for (int i = 0; i < nums.length; i++) {

      if (lefNum == Total - nums[i] - lefNum) {
        return i;
      }
      lefNum += nums[i];
    }
    return -1;
  }

  public static int[] twoSum(int[] nums, int targuet) {
    Map<Integer, Integer> mapNums = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
      int complement = targuet - nums[i];
      if (mapNums.containsKey(complement)) {
        return new int[] { mapNums.get(complement), i };
      }
      mapNums.put(nums[i], i);

    }
    return null;
  }

  public static boolean isIsomorphic(String s, String t) {
    if (s.length() != t.length())
      return false;
    Map<Character, Character> sMap = new HashMap<>();
    Map<Character, Character> tMap = new HashMap<>();

    for (int i = 0; i < s.length(); i++) {
      char c1 = s.charAt(i);
      char c2 = t.charAt(i);
      if ((tMap.containsKey(c2) && tMap.get(c2) != c1) || (sMap.containsKey(c1) && sMap.get(c1) != c2)) {
        return false;
      }
      sMap.put(c1, c2);
      tMap.put(c2, c1);

    }

    return true;

  }

  public List<List<String>> groupAnagrams(String[] strs) {
    List<List<String>> res = new ArrayList<>();
    if (strs.length == 0)
      return res;
    HashMap<String, List<String>> map = new HashMap<>();
    for (String s : strs) {
      int[] hash = new int[26];
      for (char c : s.toCharArray()) {
        hash[c - 'a']++;
      }
      String key = new String(Arrays.toString(hash));
      map.computeIfAbsent(key, k -> new ArrayList<>());
      map.get(key).add(s);
    }
    res.addAll(map.values());
    return res;
  }

  public static void arrayRotare(int[] nums, int k) {
    int n = nums.length;
    k = k % n;
    reverse(nums, 0, n - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, n - 1);

  }

  public static void reverse(int[] nums, int start, int end) {
    while (start < end) {
      int temp = nums[start];
      nums[start] = nums[end];
      nums[end] = temp;
      start++;
      end--;
    }
  }

}
