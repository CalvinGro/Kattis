use std::io;

fn main() {
    let mut in_n_m = String::new();
    let _ = io::stdin().read_line(&mut in_n_m);

    let nums: Vec<i32> = in_n_m.trim().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
    // n = num of teams
    // m = num of games 
    let (n,m) = (nums[0],nums[1]);
    
    let mut teams: Vec<String> = (1..=n).map(|i| format!("T{}", i)).collect();

    // loop through every game
    for _ in 0..(m as usize) {
        // input game results
        let mut new_teams = teams.clone();
        let mut took_losers = false;
        let mut line = String::new();
        let _ = io::stdin().read_line(&mut line);
        let game: Vec<String> = line.trim().split_whitespace().map(|x| x.to_string()).collect();
        //println!("game{:?}", game);

        let (winners, losers) = (game[0].clone(),game[1].clone());

        // create new array new_teams
        for (i, team) in teams.iter().enumerate() {
            if team == &losers {took_losers = true;}

            else if team == &winners {
                if !took_losers {break;}
                // set losers in their new place
                new_teams[i] = losers.clone();
                // set winners in their new place
                new_teams[i-1] = winners.clone();
                break;
            } else if took_losers {new_teams[i-1] = teams[i].clone();}
            
        }
        teams = new_teams;

    }
    for team in teams {
        print!("{team} ");
    }

}
