function solution(str) {
    return str.split('').reverse().join('');
}

function splitString(varstr) {
    var splitted = varstr.split('#', 2);
    return splitted
}

function duplicateEncode(word) {
    wordcopy = word
    for (i = 0; i < word.length; i++) {
        console.log(`${word.indexOf(word[i])}  ${word.lastIndexOf(word[i])}  `);

        if (word.indexOf(word[i] === word.lastIndexOf(word[i]))) {
            console.log(word[i])
            wordcopy = wordcopy.replace(word[i], "(")
            console.log(wordcopy)
        }
        else {
            wordcopy = wordcopy.replace(word[i], ")")
        }
        // count = (word.match(new RegExp(word[i], 'gi')) || []).length;
        // console.log(`count:   ${word[i]} :  ${count}`)
        // if (count > 1) {
        //     wordcopy = wordcopy.replace(new RegExp(word[i], 'gi'), ")")
        // }
        // else{
        //     wordcopy = wordcopy.replace(word[i], "(")
        // }    
    }
    return wordcopy
}

function duplicateEncode_1(str) {
    //create a var to hold string value that IGNORES case
    var word = str.toLowerCase();
    //create a var to hold the finished string to return after it's looped through 
    var unique = '';
    //loop through all letters in string
    for (var i = 0; i < word.length; i++) {
        //check for any characters that repeat
        if (word.lastIndexOf(word[i]) === word.indexOf(word[i])) {
            //for each character that never dupes, place (
            unique += '(';
        } else
            //for each character that IS a dupe, place )
            unique += ')';
    }
    //return the full string value where '(' are non duped and all')' are duped
    return unique;

}


function lcs(x, y) {
    var shortstr = "", longstr = "";
    var newstr = "";
    // find the shorter string
    if (x.length > y.length) {
        shortstr = y;
        longstr = x;
    }
    else {
        shortstr = x;
        longstr = y;
    }
    //check if the short string is present in the bigger string
    var ch;
    for (i = 0; i < shortstr.length; i++) {
        ch = shortstr[i];
        console.log(ch);

        if (longstr.search(ch) >= 0) {
            newstr = newstr + ch
        }
        console.log(newstr)

    }


    return newstr;
}

console.log(`lcs:   ${lcs("anothertest", "notatest")}`)

// console.log(solution("Javascript Coding"))

// console.log(splitString("apple#orange#banana#pear"))

// // myString = "(( $@ ))"
// // ch = '/('
// // var reg = new RegExp(ch, "gi");
// // myString.replace(reg, "");
// // console.log(myString.replace(reg, "0"));


// console.log(duplicateEncode_1("(( @))((@@"))


// console.log(duplicateEncode("((@  )"))

