fn merger<T: Ord + Copy>(arr: &mut [T], mid: usize) {
    let left_half = arr[..mid].to_vec();

    let right_halt = arr[mid..].to_vec();

    let mut l = 0;
    let mut r = 0;

    for v in arr {
        if r == right_halt.len() || (l < left_half.len() && left_half[l] < right_halt[r]) {
            *v = left_half[l];
            l += 1;
        } else {
            *v = right_halt[r];
            r += 1;
        }
    }
}

pub fn top_down_merge_sort<T: Ord + Copy>(arr: &mut [T]) {
    if arr.len() > 1 {
        let mid = arr.len() / 2;
        // Sort the left half recursively.
        top_down_merge_sort(&mut arr[..mid]);
        // Sort the right half recursively.
        top_down_merge_sort(&mut arr[mid..]);
        // Combine the two halves.
        merger(arr, mid);
    }
}
