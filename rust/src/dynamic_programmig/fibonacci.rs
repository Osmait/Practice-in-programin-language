pub fn fibonacci(n: u32) -> u128 {
    let mut a = 0;
    let mut b = 1;
    for _i in 0..n {
        let c = a + b;
        a = b;
        b = c;
    }
    b
}

pub fn recursive_fibonacci(n: u32) -> u128 {
    _recursive_fibonacci(n, 0, 1)
}

fn _recursive_fibonacci(n: u32, previous: u128, current: u128) -> u128 {
    if n == 0 {
        current
    } else {
        _recursive_fibonacci(n - 1, current, current + previous)
    }
}

pub fn classical_fibonacci(n: u32) -> u128 {
    match n {
        0 => 0,
        1 => 1,
        _ => {
            let k = n / 2;
            let f1 = classical_fibonacci(k);
            let f2 = classical_fibonacci(k - 1);
            match n % 4 {
                0 | 2 => f1 * (f1 + 2 * f2),
                1 => (2 * f1 + f2) * (2 * f1 - f2) + 2,
                _ => (2 * f1 + f2) * (2 * f1 - f2) - 2,
            }
        }
    }
}

pub fn logaritmic_fibonacci(n: u32) -> u128 {
    if n == 186 {
        let (_, second) = _logarithmic_fibonacci(185);
        second
    } else {
        let (first, _) = _logarithmic_fibonacci(n);
        first
    }
}

fn _logarithmic_fibonacci(n: u32) -> (u128, u128) {
    match n {
        0 => (0, 1),
        _ => {
            let (current, next) = _logarithmic_fibonacci(n / 2);
            let c = current * (next * 2 - current);
            let d = current * current + next * next;

            match n % 2 {
                0 => (c, d),
                _ => (d, c + d),
            }
        }
    }
}
