const arr = [1, 2, 3];
const doubled = arr.map((n) => n * 2);
console.log(doubled);

let n = 10;
let numbers = [];

for (let i = 1; i <= n; i++) {
  numbers.push(i);
}
console.log(numbers);

let fizbuzz = [];

function fizzbuzz(n) {
  for (let i = 1; i <= n; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      fizbuzz.push("fizbuzz");
    } else if (i % 3 === 0) {
      fizbuzz.push("fiz");
    } else if (i % 5 === 0) {
      fizbuzz.push("buzz");
    } else {
      fizbuzz.push(i);
    }
  }
}
fizzbuzz(15);
console.log(fizbuzz);

function fizzBuzz(n) {
  const result = [];
  for (let i = 1; i <= n; i++) {
    result.push(
      i % 15 === 0
        ? "FizzBuzz"
        : i % 3 === 0
        ? "Fizz"
        : i % 5 === 0
        ? "Buzz"
        : i
    );
  }
  return result;
}

console.log(fizzBuzz(15));

function isPalindrome(str) {
  const reverse = str.split("").reverse().join("");
  console.log(reverse);
  return string === reverse;
}
console.log(isPalindrome(string));

const myPromise = new Promise((resolve, reject) => {
  // asynchronous operation
  const success = true; // example condition

  if (success) {
    resolve("Operation succeeded!");
  } else {
    reject("Operation failed!");
  }
});

myPromise
  .then((result) => {
    console.log(result); // runs if resolved
  })
  .catch((error) => {
    console.error(error); // runs if rejected
  });

const array = [..."frontend"];
console.log(array);

const string = "Hello World SMita";
const split = string.split(" ");
console.log(split);
console.log(split.map((i) => i.split("").reverse().join("")).join(" "));

// reverse each word of string
function reverseStringWord(string) {
  const reversedString = string
    .split(" ")
    .map((i) => i.split("").reverse().join(""))
    .join(" ");
  return reversedString;
}

console.log(reverseStringWord(string));

console.log([1, 21] + [3, 4] + [3, 5]);

console.log(0.1 + 0.2 === 0.3);
// Proper debounce implementation
function debounce(func, delay) {
  let timer;
  return function (...args) {
    clearTimeout(timer); // stop previous call
    timer = setTimeout(() => {
      // wait for delay
      func(...args); // then call the function
    }, delay);
  };
}

var a = "1";
var b = 1;
console.log(a === b); //matches the type as awell as value of variable
console.log(a == b); // dont matches the type and amtches only value of variable

// const string = "hello world";
let vowels = 0;
let consonants = 0;

for (let char of string.toLowerCase()) {
  if ("aeiou".includes(char)) {
    vowels++;
  } else if (char >= "a" && char <= "z") {
    consonants++;
  }
}

console.log("Vowels:", vowels);
console.log("Consonants:", consonants);

// let string ="koko"
// let string1 ="koko"

// // let nonRepeating=[]

// function anagram(){
//     return string.split("").sort().join("") === string1.split("").sort().join("");
// }
// console.log(anagram())

// for (let i =0; i<string.length; i++){
//     char= string[i];
//     if(string.indexOf(char) === string.lastIndexOf(char)){
//         nonRepeating.push(char)
//     }
// }
// console.log(nonRepeating)

// if (string === string.split("").reverse().join("")){
//     console.log("palindrome")
// }
// else console.log("not palindorme")

// let reversedstring =""

// for (let i= string.length -1; i >= 0; i--){
//     reversedstring += string[i];
// }

// console.log(reversedstring,"reversedstring")
