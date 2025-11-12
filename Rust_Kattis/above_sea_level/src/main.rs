use std::io;

fn main() {
    let mut in_str = String::new();
    io::stdin().read_line(&mut in_str).unwrap();
    let mut fl: f64 = in_str.trim().parse::<f64>().unwrap();
    fl -= 0.3;
    println!("{fl}");

}
