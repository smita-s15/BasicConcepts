const string = "hellow there";

let vowel = 0;
let consonants = 0;

function findcount(str) {
  const lower = str.toLowerCase();
  for (const char of lower) {
    if ("aeiou".includes(char)) {
      vowel++;
    } else if (char >= "a" && char <= "z") {
      consonants++;
    }
  }
}

findcount(string);

console.log(vowel, consonants);
