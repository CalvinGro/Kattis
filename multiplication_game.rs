use std::io;

fn main() {

    let mut new_input = String::new();
    loop {
        new_input.clear();
        let _ = io::stdin().read_line(&mut new_input);
        new_input = new_input.trim().to_string();
        if new_input == "" {
            break;
        }
        let mut num = new_input.parse::<i64>().unwrap();

        // just wanted to practice using tuples
        let divs = [9, 2];
        let mut i: usize = 1;
        while num > 1 {
            if i == 0 {
                i = 1;
            } else {
                i = 0;
            }
            num = div_ceil(num, divs[i]);
        }
        if divs[i] == 9 {
            println!("Stan wins.");
        } else {
            println!("Ollie wins.")
        }

    }
}

fn div_ceil(a: i64, b:i64) -> i64 {
    (a + b - 1) / b
}