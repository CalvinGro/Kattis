use std::io;
// to slow
fn main() {
    let base: f64 = 2.0;
    let exp1 = -5.0/4.0;
    let exp2 = -3.0/4.0;
    let starting_width = base.powf(exp1);
    let starting_height = base.powf(exp2);

    let mut paper_count = 0;
    let mut total_tape: f64 = starting_height;
    let mut papers = create_arr();
    for paper in papers {
        paper_count += paper;
    }

    // dbg!(papers);
    let not_enough_paper_l = recursive_next_paper(0, starting_height, starting_width, &mut total_tape, &mut papers, &mut paper_count);
    let not_enough_paper_r = recursive_next_paper(0, starting_height, starting_width, &mut total_tape, &mut papers, &mut paper_count);
    
    if not_enough_paper_l || not_enough_paper_r {
        println!("impossible");
    } else {
        println!("{}", total_tape);
    }


}

fn recursive_next_paper(i:usize, height: f64, width: f64, total_tape: &mut f64, papers: &mut [i32], paper_count: &mut i32) -> bool {
    let not_enough_paper_l;
    let not_enough_paper_r;
    if i > 29 || (*paper_count == 0) {
        return true;
        
    } else if papers[i] > 0 {
        papers[i] -= 1;
        *paper_count -= 1;
        return false
    } else {
        *total_tape += width;
        not_enough_paper_l = recursive_next_paper(i+1, width, height/2.0, total_tape, papers, paper_count);
        not_enough_paper_r = recursive_next_paper(i+1, width, height/2.0, total_tape, papers, paper_count);
    }
    not_enough_paper_l || not_enough_paper_r
}


// create array of every paper size (i) and store the count for each, starting at A0
fn create_arr() -> [i32; 30] {
        let mut paper_sizes = [0; 30];

    let mut s_starting_size = String::new();

    let _ = io::stdin().read_line(&mut s_starting_size);
    // let starting_size = s_starting_size.trim().to_string().parse::<usize>().unwrap();

    let mut s_papers = String::new();
    let _ = io::stdin().read_line(&mut s_papers);
    s_papers = s_papers.trim().to_string();

    for (i, s) in s_papers.split_whitespace().enumerate() {
        paper_sizes[i] = s.parse::<i32>().unwrap();
    }

    paper_sizes
}
