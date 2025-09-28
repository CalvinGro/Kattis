use std::io;

fn main () {
    let mut num_of_cases = String::
    let _ = io::stdin().read_line(&mut num_of_cases);
    num_of_cases = num_of_cases.trim().to_string(); 
    num_of_cases = num_of_cases as i32;

    let mut num_of_people = String::
    let _ = io::stdin().read_line(&mut num_of_people);
    num_of_people = num_of_people.trim().to_string(); 
    num_of_people = num_of_people as i32;

    for case in 0..num_of_cases {
        for person_num in 0..num_of_people {
            let mut person = String::
            let _ = io::stdin().read_line(&mut person);
            person = person.trim().to_string(); 
            

        }
        println!("==============================");
    }
}