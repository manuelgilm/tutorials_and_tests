use std::io;

fn main() {
    println!("Input first number");
    let mut num1 = String::new();
    io::stdin().read_line(&mut num1).expect("Failed reading number 1");
    //Validate first number
    let num1: i32 = num1.trim().parse().expect("Input a number");

    println!("Input Second Number");
    let mut num2 = String::new();
    io::stdin().read_line(&mut num2).expect("Failed reading number 1");
    let num2: i32 = num2.trim().parse().expect("Input a number");

    println!("Input operation + - * /");
    let mut op = String::new();
    io::stdin().read_line(&mut op).expect("Failed reading operation");
    let result: i32;
    println!("Operation: {op}");
    if op.trim() == "+" {
        result = num1 + num2;

    } else if op.trim() == "-" {
        result = num1 - num2;
    } else if op.trim() == "*" {
        result = num1 * num2;
    } else {
        if num2 == 0 {
            println!("Operation not valid");
            result = 0;
        } else {
            result = num1 / num2;
        }
    }
    println!("Result is: {result}");
    
}

