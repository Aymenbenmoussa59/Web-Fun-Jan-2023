function encodestr(str) {
    let encoded = '';
    let count = 1;
  
    for (let i = 1; i < str.length; i++) {
      if (str[i] === str[i - 1]) {
        count++;
      } else {
        encoded += str[i - 1] + count;
        count = 1;
      }
    }
  
    encoded += str[str.length - 1] + count;
    return encoded;
  }
  
  const str1 = 'aaaabbcddd';
  const expected1 = 'a4b2cd3';
  
  const result1 = encodestr(str1);
  console.log(result1);  
  