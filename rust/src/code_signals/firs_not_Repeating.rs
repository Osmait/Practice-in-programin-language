use std::collections::HashMap;

fn solution(s: String) -> char {
    s.chars()
        .enumerate()
        .fold(
            HashMap::new(),
            |mut letters: HashMap<char, (i32, usize)>, (k, v)| {
                letters
                    .entry(v)
                    .and_modify(|e| (*e).0 += 1)
                    .or_insert((1, k));
                letters
            },
        )
        .into_iter()
        .filter(|(k, v)| v.0 < 2)
        .min_by(|a, b| (a.1).1.cmp(&(b.1).1))
        .unwrap_or(('_', (0, 0)))
        .0
}
