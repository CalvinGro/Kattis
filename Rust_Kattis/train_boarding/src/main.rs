use std::io;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let mut it = line.split_whitespace();
    let car_count = it.next().unwrap().parse::<u32>().unwrap();
    let length = it.next().unwrap().parse::<u32>().unwrap();
    let passengers = it.next().unwrap().parse::<u32>().unwrap();

    let half_car = length / 2;
    let train_end = (length*car_count) - half_car;
    let mut greatest_dist = 0;
    let mut cars: Vec<u32> = vec![0; car_count as usize];

    for _ in 0..passengers {

        let mut line = String::new();
        io::stdin().read_line(&mut line).unwrap();
        let pass_dist = line.trim().parse::<u32>().unwrap();

        if pass_dist > train_end {
            cars[(car_count-1) as usize] += 1;
            if (pass_dist-train_end) > greatest_dist {
                greatest_dist = pass_dist-train_end;
            }
        } else {
            cars[(pass_dist/length) as usize] += 1;
            let dist_from_car = (((pass_dist/length) * length + half_car) as i32 - pass_dist as i32).abs();
            if dist_from_car > greatest_dist as i32 {
                greatest_dist = dist_from_car as u32;
            }
        }
    }
    let mut greatest_car: u32 = 0;
    for car in &cars {
        if *car > greatest_car {
            greatest_car = *car;
        }
    }
    println!("{}\n{}", greatest_dist, greatest_car);
}