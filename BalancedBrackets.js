process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = "";
var input_stdin_array = "";
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split("\n");
    main();    
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////
function checkString(str){
    let bracketStack = [];
    let bracketDict = {
        '{':'}',
        '[':']',
        '(':')',
    }
    
    function closesLastBracket(current){
        if(bracketStack.length === 0) return false;

        let expectedLast = bracketDict[bracketStack[bracketStack.length - 1]];
        return expectedLast === current;
    }
    
    let valid = true;
    for(let i = 0; i < str.length; i++){
        switch(str[i]){
            case '{':
            case '[':
            case '(':
                bracketStack.push(str[i]);
                break;
            case '}':
            case ']':
            case ')':
                if(!closesLastBracket(str[i]))
                    valid = false;
                else
                    bracketStack.pop();
                break;
        }
    }
    
    if(bracketStack.length > 0) valid = false;

    return valid;
}

function main() {
    var t = parseInt(readLine());
    for(var a0 = 0; a0 < t; a0++){
        var expression = readLine();
        console.log(checkString(expression) ? 'YES' : 'NO')
    }
}
