use std::env;
use std::process;
use thirty_one_limit_johnston::note_name;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide a ratio (e.g., 49/55) or two integers.");
        process::exit(1);
    }

    let (x, y) = if args.len() >= 3 {
        let x = args[1].parse::<i64>().unwrap_or_else(|_| {
            println!("Invalid numerator: {}", args[1]);
            process::exit(1);
        });
        let y = args[2].parse::<i64>().unwrap_or_else(|_| {
            println!("Invalid denominator: {}", args[2]);
            process::exit(1);
        });
        (x, y)
    } else {
        let arg = &args[1];
        if arg.contains('/') {
            let parts: Vec<&str> = arg.split('/').collect();
            if parts.len() != 2 {
                println!("Invalid ratio format. Use x/y.");
                process::exit(1);
            }
            let x = parts[0].parse::<i64>().unwrap_or_else(|_| {
                println!("Invalid numerator: {}", parts[0]);
                process::exit(1);
            });
            let y = parts[1].parse::<i64>().unwrap_or_else(|_| {
                println!("Invalid denominator: {}", parts[1]);
                process::exit(1);
            });
            (x, y)
        } else if arg.contains(' ') {
            let parts: Vec<&str> = arg.split_whitespace().collect();
            if parts.len() != 2 {
                println!("Invalid ratio format. Use 'x y'.");
                process::exit(1);
            }
            let x = parts[0].parse::<i64>().unwrap_or_else(|_| {
                println!("Invalid numerator: {}", parts[0]);
                process::exit(1);
            });
            let y = parts[1].parse::<i64>().unwrap_or_else(|_| {
                println!("Invalid denominator: {}", parts[1]);
                process::exit(1);
            });
            (x, y)
        } else {
            println!("Please provide a ratio (e.g., 49/55) or two integers.");
            process::exit(1);
        }
    };

    note_name(x, y, false);
}
