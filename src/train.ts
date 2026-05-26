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

function getSquareNumbers(arr: number[]) {
  const result = [];

  for (const num of arr) {
    result.push({
      number: num,
      square: num * num,
    });
  }

  return result;
}

console.log(getSquareNumbers([1, 2, 3]));
