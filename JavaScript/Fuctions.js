/// This is just a master file of fuctions that I have made to refrence / search on Github

// Write a function called swapFirstAndLast that takes in an array as a parameter.
// Swap the values of the first and last index without using array destructuring.
// Return the updated array

function swapFirstAndLast(inputArray) {
    //Fail Fast
    if (!Array.isArray(inputArray) || inputArray.length < 2) {
        return inputArray;
    }

    // Swap
    let firstElement = inputArray[0];
    let lastIndex = inputArray.length - 1;

    inputArray[0] = inputArray[lastIndex];
    inputArray[lastIndex] = firstElement;

    return inputArray;
}


