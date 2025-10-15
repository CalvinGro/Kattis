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
        let modx = x.rem_euclid(modifier);
        let mody = y.rem_euclid(modifier);
        let moddx = dx.rem_euclid(modifier);
        let moddy = dy.rem_euclid(modifier);

        let change_x = dx.rem_euclid(s);
        let change_y = dy.rem_euclid(s);
        let mut x_dist = s - x.rem_euclid(s);
        let mut y_dist = s - y.rem_euclid(s);
        let mut jmp = 0;
        let mut num_of_jmps_x = i32::MAX -1;
        let mut num_of_jmps_y = i32::MAX -1;
        let mut cant_escape = false;

        // checks if flea can not escape
        if (modx == mody) && (moddx == moddy) || ((modx == 0) && ((moddx == s) || (moddx == 0))) || ((mody == 0) && ((moddy == s) || (moddy == 0))){
            println!("The flea cannot escape from black squares.");

        // elif first value not on black square
        } else if !(((x.rem_euclid(s)) == 0) || (y.rem_euclid(s) == 0) || ((modx >= s) && (mody >= s)) || ((modx <= s) && (mody <= s))) {
            println!("After 0 jumps the flea lands at ({}, {}).", x, y);

        // elif second value not on black square
        } else if !(((x+dx).rem_euclid(s) == 0) || ((y+dy).rem_euclid(s) == 0) || (((modx + moddx) >= s) && ((mody + moddy) >= s)) || (((modx + moddx) <= s) && ((mody + moddy) <= s))) {
            x += dx;
            y += dy;
            println!("After 1 jumps the flea lands at ({}, {}).", x, y);

        // else neither the first nor second squares are white
        } else {
            loop {
                if change_x != 0 {
                    num_of_jmps_x = x_dist / change_x + 1;
                }
                if change_y != 0 {
                    num_of_jmps_y = y_dist / change_y + 1;
                } else if change_x != 0 {
                    println!("The flea cannot escape from black squares.");
                    cant_escape = true;
                    break;
                }

                // break out and jmps 
                if num_of_jmps_x != num_of_jmps_y {
                    if num_of_jmps_x < num_of_jmps_y {
                        jmp = num_of_jmps_x;
                    } else {
                        jmp = num_of_jmps_y;
                    }
                    break;
                } else {
                    jmp += num_of_jmps_x;
                    x_dist = (num_of_jmps_x * change_x + x_dist) - s;
                    y_dist = (num_of_jmps_y * change_y + y_dist) - s;
                }
            }
            if !cant_escape {
                x += jmp * dx;
                y += jmp * dy;
                println!("After {} jumps the flea lands at ({}, {}).", jmp, x, y);
            }
        } 
        
    }
}

