use std::io;

fn main () {
        let mut user_input = String::new();

    loop {
        user_input.clear();
        let _ = io::stdin().read_line(&mut user_input);
        user_input = user_input.trim().to_string();
        if user_input == "0 0 0 0 0" {
            break;
        }

        // Clean User Input
        let (mut s, mut x, mut y, mut dx, mut dy) = (0, 0, 0, 0, 0);
        for (i, val) in user_input.split_whitespace().take(5).enumerate() {
            match i {
                0 => {s = val.parse::<i32>().unwrap()},
                1 => {x = val.parse::<i32>().unwrap()},
                2 => {y = val.parse::<i32>().unwrap()},
                3 => {dx = val.parse::<i32>().unwrap()},
                4 => {dy = val.parse::<i32>().unwrap()},
                _ => {unreachable!()},
            }
        }
    

        let modifier = s*2;
        let mut modx = x.rem_euclid(modifier);
        let mut mody = y.rem_euclid(modifier);
        let moddx = dx.rem_euclid(modifier);
        let moddy = dy.rem_euclid(modifier);
        let mut jmp = 0;

        // checks if flea can not escape
        if (modx == mody) && (moddx == moddy) || ((modx == 0) && ((moddx == s) || (moddx == 0))) || ((mody == 0) && ((moddy == s) || (moddy == 0))){
            println!("The flea cannot escape from black squares.");
        } else {
            // while on black squares
            while (modx == 0 || mody == 0 || (modx >= s) && (mody >= s)) || ((modx <= s) && (mody <= s)) {
                modx = (modx + moddx).rem_euclid(modifier);
                mody = (mody + moddy).rem_euclid(modifier);
                x += dx;
                y += dy;
                jmp += 1;
            }
            println!("After {} jumps the flea lands at ({}, {}).", jmp, x, y);
        }
    }
}
