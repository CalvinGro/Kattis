use std::io;
use std::collections::HashMap;
// use std::thread::current;

// unfinished

fn main() {
    
    // get length of array
    let mut inp_length = String::new();
    let _ = io::stdin().read_line( &mut inp_length);
    let mut length: usize = inp_length.trim().parse().unwrap();

    // get array
    let mut nums = vec![0; length];
    let mut nums_inp = String::new();
    let _ = io::stdin().read_line(&mut nums_inp);
    nums_inp = nums_inp.trim().to_string();

    for (i, n) in nums_inp.split_whitespace().enumerate() {
        nums[i] = n.parse::<i32>().unwrap();
    }
    // end of user input section

    // because nums range from -50,000 to 50,000
    if length > 100_001 {
        length = 100_001;
    }

    let mut total: i64 = 0;
    // let mut prev_checked:HashMap<i32, i64>  = HashMap::with_capacity(length);
    let mut sums: HashMap<i32, i64> = HashMap::with_capacity(length);

    // loop through and add all values to sums
    for num in nums.iter() {
        *sums.entry(*num).or_insert(0) += 1;
    }

    // create vector of sums
    let mut sorted_nums = Vec::new();
    for (key, value) in &sums {
        sorted_nums.push((*key, *value));
    }

    // sort vector of nums by first value in the tuple
    sorted_nums.sort_by_key(|x| x.0);


    for (k, count) in &sorted_nums {
        // println!("k: {}, count: {}", k, count);
        // use double pointers to check all possible i and j ints.
        let mut j: usize = 0;
        let mut i: usize = sorted_nums.len() - 1;
        let mut current_total: i64 = 0;
        // start with j on the left and i on the right
        while i >= j {

            if i == j {
                // sum found, add to current_total and advance both pointers
                if sorted_nums[j].0 == 0 && *k == 0 && sorted_nums[i].0 == 0 {
                    let n = sorted_nums[i].1;
                    // println!("adding {} to current_total: {}", (n * (n-1) * (n-2)), current_total);
                    current_total += n * (n-1) * (n-2);
                }
                
                // if i and j point to the same number and it + itself = k
                else if i == j && (sorted_nums[j].0 + sorted_nums[i].0) == *k {
                    // find num of to add to current_total based of count
                    let n = sorted_nums[i].1;
                    current_total += n * (n-1) * *count;
                }
                break
            }

            else if (sorted_nums[j].0 + sorted_nums[i].0) == *k {
                // dont count the case where k and i are the same int if it exists
                let i_count = sorted_nums[i].1;
                let j_count = sorted_nums[j].1;
                let mut sub_i = 0;
                let mut sub_j = 0;
                if *k == sorted_nums[i].0 {
                    println!("i.0: {} matched k", sorted_nums[i].0);
                    sub_i += 1;
                }
                // dont count the case where k and j are the same int if it exists
                if *k == sorted_nums[j].0 {
                    println!("j.0: {} matched k", sorted_nums[j].0);
                    sub_j +=  1;
                }

                // println!("current_total += {} for k: {}", (2 * i_count * j_count) * *count, *k);
                current_total += (2 * i_count * j_count) * (*count - sub_i - sub_j);
                i -= 1;
                j += 1;
            }
            else if (sorted_nums[j].0 + sorted_nums[i].0) > *k {
                i -= 1
            }
            else if (sorted_nums[j].0 + sorted_nums[i].0) < *k {
                j += 1
            }            
        }
        // add (current_total * number of k occurances) to total
        total += current_total;
    }
    println!("{total}");


}






