use std::io;
fn main() {
    let mut in_num = String::new();
    let _ = io::stdin().read_line(&mut in_num);
    let num: usize = in_num.trim().parse().unwrap();

    let mut min_temps = Vec::new();
    let mut max_temps = Vec::new();
    for _ in 0..num {

        let mut line = String::new();
        let _ = io::stdin().read_line(&mut line);
        let nums: Vec<i32> = line.trim().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
        min_temps.push(nums[0]);
        max_temps.push(nums[1]);
    }
    let highest_min = min_temps.iter().max().unwrap();
    let lowest_max = max_temps.iter().min().unwrap();
    let count: i32 =  lowest_max - highest_min + 1;
    if count > 0 {
        println!("{count} {highest_min}");
    } else {
        println!("bad news")
    }
}
