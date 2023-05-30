package leetCode

fun ContainDuplicate(nums:IntArray):Boolean{
    val hs = HashSet<Int>()
    for ( e in nums){
        if (!hs.contains(e)){
            return true
        }
        hs.add(e)
    }
    return false

}