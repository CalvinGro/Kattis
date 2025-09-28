use std::io;

fn main () {
    let mut user_input = String::new();
    let _ = io::stdin().read_line(&mut user_input);
    user_input = user_input.trim().to_string(); 

    let mut num = 0;
    let mut broke = false;

    while !user_input.is_empty() {
        num += 1;
        let current = num.to_string();
        let length = current.len();
        let first_n: String = user_input.chars().take(length).collect();
        let rest: String = user_input.chars().skip(length).collect();
        user_input = rest;
        if first_n != current {
            println!("-1"); 
            broke = true;
            break;
        };
    };
    if !broke {
        println!("{}", num);
    };

}
