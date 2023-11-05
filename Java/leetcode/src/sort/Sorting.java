package sort;

import java.util.ArrayList;

import java.util.Collections;
import java.util.List;

public class Sorting {


    public static List<Integer> mergeSort(List<Integer> array) {
        if(array.size() <= 1)return array;

        int mid = 0 + (array.size())/ 2;
       

       List<Integer> letfHalf = array.subList(0, mid);
    
       List<Integer> rightHalf = array.subList(mid,array.size());
     


       return merge(mergeSort(letfHalf),mergeSort(rightHalf));
        

    }

    private static List<Integer> merge(List<Integer> letfHalf, List<Integer> rightHalf) {
        List<Integer> listSort = new ArrayList<>(Collections.nCopies(letfHalf.size() + rightHalf.size(), 0));
       int pointer1 = 0;

       int pointer2 = 0;

       int index = 0;

       while(pointer1 < letfHalf.size() && pointer2 < rightHalf.size() ){
        if(letfHalf.get(pointer1) < rightHalf.get(pointer2)){
            listSort.set(index, letfHalf.get(pointer1));
            pointer1 ++;
            index ++;

        }else{
            listSort.set(index, rightHalf.get(pointer2));
            pointer2++;
            index++;
        }
       }
        while(pointer1 < letfHalf.size()){
            listSort.set(index, letfHalf.get(pointer1));
            pointer1 ++;
            index ++;

       }

       while(pointer2 < rightHalf.size()){
        listSort.set(index, rightHalf.get(pointer2));
            pointer2 ++;
            index ++;

       }
       return listSort;

    }
    
    
}
