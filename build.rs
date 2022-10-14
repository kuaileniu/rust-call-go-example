use std::process::Command;
use std::env;

fn main() {
    let out_dir = env::var("OUT_DIR").unwrap();

    Command::new("go").args(&["build", "-o", &format!("{}/libawesome.a", out_dir), "-buildmode=c-archive"])
        // .arg("src/awesome.go")
        .arg("awesome.go")
        .status().unwrap();

    println!("cargo:rustc-link-search=native={}", out_dir);
}

