use std::io;

fn main() {
    let mut input = String::new();
    let _ = io::stdin().read_line(&mut input);
    input = input.trim().to_string();
    let num: i32 = input.parse().unwrap();

    if num < 149 {
        println!("99");
    } else {
        let last_two = num % 100; // mod by 100
        let rest = num / 100; // floor divisition
        if last_two >= 49 {
            println!("{rest}99");
        } else {
            println!("{}99", rest - 1)
        };
    };
}
