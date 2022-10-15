use std::process::Command;
use std::env;

fn main() {
    let out_dir = env::var("OUT_DIR").unwrap();
    // 当用go.mod中引用外部库时， 可考虑通过build.rs调用外部python脚本进行打包
    // python中接收 静态文件生成的完整路径
    Command::new("go").args(&["build", "-o", &format!("{}/libawesome.a", out_dir), "-buildmode=c-archive"])
        // .arg("src/awesome.go")
        .arg("awesome.go")
        .status().unwrap();

    println!("cargo:rustc-link-search=native={}", out_dir);
}

