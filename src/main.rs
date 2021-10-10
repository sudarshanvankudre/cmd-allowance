use std::io;

fn main() {
    loop {
        match read_input() {
            Ok(_) => (),
            Err(_) => println!("error when reading command")
        }
    }
}

fn read_input() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_line(&mut input)?;
    println!("You typed: {}", input.trim());
    Ok(())
}
