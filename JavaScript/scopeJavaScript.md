# Understanding Scope in JavaScript

Scope in JavaScript refers to the accessibility and visibility of variables, functions, and objects in different parts of your code. It determines where these entities can be used and accessed. This guide focuses on function scope and block scope in JavaScript.

## Function Scope

Function scope is one of the fundamental concepts in JavaScript. It refers to the visibility and accessibility of variables within a function.

## Block Scope

let lightsAreOn = true;
if {lightsAreOn} {
    let blockSccoppedVar = "I am block scoped between brackets with let.";
    const blockSccoppedConst = "I am block scoped between brackets with Const.";
    console.log(blockSccoppedVar);
    console.log(blockSccoppedConst);
}

## Notes

- Pay attention to your linter as the hints can be super helpful.
- Scope can be tricky as you are working through it, so remember to test the scope in different ways to understand its full process.