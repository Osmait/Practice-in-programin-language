
import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicInteger;

import leetCode.Fetch;
import sort.Sorting;

public class Main {
  public static void main(String[] args) {

    List<Integer> listInt = new ArrayList<>();
    listInt.add(10);
    listInt.add(5);
    listInt.add(3);
    listInt.add(1);

    System.out.println(Sorting.mergeSort(listInt));

    // Fetch fetch = new Fetch();

    // File file = new File("Java/leetcode/src/product2.json");
    // // File file2 = new File("Java/leetcode/src/product2.json");

    // try {
    // Scanner sc = new Scanner(file);
    // // StringBuilder info = new StringBuilder();
    // while (sc.hasNextLine()) {
    // System.out.println(sc.nextLine());
    // }
    // // FileWriter fs = new FileWriter(file2);
    // // fs.write(fetch.get());
    // // fs.close();
    // sc.close();
    // } catch (Exception e) {
    // e.printStackTrace();
    // }

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

}
