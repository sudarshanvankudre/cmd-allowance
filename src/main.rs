use clap::clap_app;
extern crate clap;

fn main() {
    let matches = clap_app!(myapp => 
        (version: "1.0")
        (author: "Sudarshan Vankudre")
        (about: "Financial tracking through the command line")
        (@subcommand )
    )
}
