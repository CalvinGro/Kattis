use std::io;

fn main() {

    // take input line and get size and k
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let mut it = line.split_whitespace();
    let _ = it.next().unwrap().parse::<u32>().unwrap();
    let mut size = it.next().unwrap().parse::<u32>().unwrap();

    // take input line and get nums
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let mut nums = Vec::<u32>::new();
    let mut it = line.split_whitespace();
    while let Some(num) = it.next() {
        nums.push(num.parse::<u32>().unwrap());
    }

    let mut zeros: u32 = 0;
    let mut great_1: u32 = 0;
    let mut great_2: u32 = 0;
    let mut great_3: u32 = 0;

    for n in nums {
        let remainder = n % 4;

        match remainder {
            0 => zeros += n,
            1 => if n > great_1 { great_1 = n },
            2 => if n > great_2 { great_2 = n },
            _ => if n > great_3 { great_3 = n },
        }
    }

    if (size % 4) == 1 {
        size += great_1;
    } else if (size % 4) == 3 {
        size += great_3;
    }

    if (size % 4) == 2 {
        size += great_2;
    }

    if (size % 4) == 0 {
        size += zeros;
    }
    print!("{size}");
}
