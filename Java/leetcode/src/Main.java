

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;


public class Main {
    public static void main(String[] args) {
        int[] result = twoSum(new int[]{2, 7, 11, 15},9);
        System.out.printf(Arrays.toString(result));
    }

    public static int[] RunningSum(int[] nums){
        AtomicInteger sum= new AtomicInteger();
        return  Arrays.stream(nums).map(sum::addAndGet).toArray();
    }

    public static int pivotIndex(int[] nums){
       int Total  = Arrays.stream(nums).sum();
       int lefNum = 0;
        for (int i = 0; i < nums.length; i++) {

            if (lefNum == Total -  nums[i]  - lefNum){
                return i;
            }
            lefNum += nums[i];
        }
        return  -1;
    }

    public static int[] twoSum(int[] nums,int targuet){
        Map<Integer, Integer> mapNums = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int complement = targuet - nums[i];
            if (mapNums.containsKey(complement)){
                return  new int[]{mapNums.get(complement),i};
            }
            mapNums.put(nums[i],i);

        }
        return null;
    }
    public static  boolean isIsomorphic(String s, String t){
        if (s.length() != t.length())return false;
        Map<Character, Character> sMap = new HashMap<>();
        Map<Character, Character> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++){
           char c1 = s.charAt(i);
           char c2 = t.charAt(i);
            if ((tMap.containsKey(c2) && tMap.get(c2) != c1) || (sMap.containsKey(c1) && sMap.get(c1) != c2)) {
                return false;
            }
        sMap.put(c1,c2);
        tMap.put(c2,c1);

        }

        return true;


    }
   
    }




   






    
