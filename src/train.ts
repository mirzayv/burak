// console.log("Hello World");

// TASK-M

// Masalani izohi
// Array ichidagi har bir raqam uchun
// raqamning o'zi va uning kvadratidan
// tashkil topgan object hosil qilib qaytarsin.

// Masalan:
// getSquareNumbers([1, 2, 3])
// return [
//   { number: 1, square: 1 }, ...]

/* function getSquareNumbers(arr: number[]) {
  const result = [];

  for (const num of arr) {
    result.push({
      number: num,
      square: num * num,
    });
  }

  return result;
}

console.log(getSquareNumbers([1, 2, 3])); */

// TASK-N

// Masalani izohi
// Stringni palindrom ekanligini aniqlab
// true yoki false qaytarsin.

// Masalan:
// palindromCheck("dad")
// return true

/* function palindromCheck(text: string): boolean {
  return text === text.split("").reverse().join("");
}

console.log(palindromCheck("dad")); */

/* Project Standards:
   - Logging standards
   - Naming standards:
        function, method, variable => CAMEL
        class => PASCAL
        folder, file => KEBAB
        css => SNAKE
   - Error handling

*/

/*
  Traditional Api
  Rest Api
  GraphQL Api
  ...
*/

/*
  Traditional FD => SSR => EJS
  Modern FD => SPA => REACT
*/

// TASK-O

// Masalani izohi
// Array ichidagi har xil qiymatlardan faqat sonlar yig'indisini hisoblab qaytarsin.

// Masalan:
// calculateSumOfNumbers([10, "10", {son: 10}, true, 35]) return 45
/* 
function calculateSumOfNumbers(arr: any[]): number {
  let total = 0;

  for (let item of arr) {
    if (typeof item === "number") {
      total += item;
    }
  }

  return total;
}

console.log(calculateSumOfNumbers([10, "10", { son: 10 }, true, 35]));
 */

// TASK-P

// Masalani izohi
// Objectni nested array sifatida convert qilib qaytarsin.

// Masalan:
// objectToArray({a: 10, b: 20})
// return [["a", 10], ["b", 20]]

/* function objectToArray(obj: any): any[] {
  let result = [];

  for (let key in obj) {
    result.push([key, obj[key]]);
  }

  return result;
}

console.log(objectToArray({ a: 10, b: 20 })); */

// TASK-Q

// Masalani izohi
// Objectda berilgan string propertysi borligini tekshirsin.

// Masalan:
// hasProperty({name: "BMW"}, "name") return true
// hasProperty({name: "BMW"}, "color") return false

/* function hasProperty(obj: Record<string, unknown>, prop: string): boolean {
  return prop in obj;
}

console.log(hasProperty({ name: "BMW" }, "name")); // true
console.log(hasProperty({ name: "BMW" }, "color")); // false
console.log(hasProperty({}, "name")); // false
 */

/* 
request join
self destroy
*/
