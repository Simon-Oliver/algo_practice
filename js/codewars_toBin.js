function binaryToString(binary) {
  let str = "";
  for (let index = 0; index < binary.length; index = index + 8) {
    const chunck = binary.substring(index, index + 8);
    str += String.fromCharCode(parseInt(chunck, 2));
  }
  return str;
}

console.log(
  binaryToString("01001011010101000100100001011000010000100101100101000101") // 'KTHXBYE'
);
console.log(binaryToString("01100001"));
