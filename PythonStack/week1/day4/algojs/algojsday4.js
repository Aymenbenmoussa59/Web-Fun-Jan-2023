// var str="aaaabbcddd";
// var NewSrt="";
// function encodeStr(str) {
//     let encodedStr = "";
//     for (let i = 0; i < str.length; i++) {
//       encodedStr +=NewSrt(i);
//     }
//     return encodedStr;
//   }
//   console.log(eeeeeeeeeeeeeeeeeeee);


function encodeStr(str) {
    let encoded = '';
    let count = 1;

    for (var i = 0; i < str.length; i++) {
      if (str[i] === str[i + 1]) {
        count++;
      } else {
        if (count > 1) {
          encoded += str[i] + count;
        } else {
          encoded += str[i];
        }
        count = 1; // Reset the count to 1 for the next character
      }
    }

    return encoded;
  }

  console.log(encodeStr("aaaabbddds"));



// function encodeStr(str) {
//     let encoded = '';
//     let count = 1;

//     for ( var i = 0; i < str.length; i++) {
//       if (str[i] === str[i + 1]) {
//         count++;
//       } else {
//         encoded += str[i] + count;
//         count = 0;
//       }
//     }

//     return encoded;
//   }
//   console.log(encodeStr("aaaabbddds"));