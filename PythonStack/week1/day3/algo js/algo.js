/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

// create a new string str = ""
// loop over the array
//      for....
// str += arr[i]
// as we are looping

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

function join(arr, separator) {

  // joined for the result
  var joined = ""
  if (arr.length == 0) {
    return joined
  }
  // less than arr.length to stop before last
  for (var i = 0; i < arr.length - 1; i++) {
    joined += arr[i] + separator
  }

  return joined + arr[arr.length - 1]




}



// var arr = [1, 2, 3];
// var separator= ",";
// function join(arr, separator) {
//     for ( i< arr.length; i++ ) {

//     }

// }