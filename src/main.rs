use std::io;

fn main() {
    loop {
        match read_input() {
            Ok(_) => (),
            Err(_) => println!("error when reading command")
        }
    }
}

fn read_input() -> io::Result<Action> {
    let mut input = String::new();
    io::stdin().read_line(&mut input)?;
    println!("You typed: {:?}", input.trim().split(" "));
    let mut input_list = input.trim().split(" ");
    let cmd = input_list.next().unwrap();
    let vals = input_list.map(|x| x.to_string()).collect();
    let action = Action {
        command: cmd.to_string(),
        values: vals
    };
    Ok(action)
}

fn run_action(action: &Action) {
    match action.command {
        "new" => create_new_transaction(&action.values),
        _ => ()

    }
}

fn create_new_transaction(values: &Vec<String>) {
    let subject = values.get(0);
    
}

struct Action {
    command: String,
    values: Vec<String>
}
