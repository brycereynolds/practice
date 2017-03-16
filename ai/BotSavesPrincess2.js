function processData(input) {
        
    var lines = input.split('\n');
    var dimension = parseInt(lines[0]);
    var mario = lines[1].split(' ');
    var marioRow = mario[0];
    var marioCol = mario[1];
    
    var nextMove = 'UNKNOWN';
    
    for(var i = 2; i <= dimension + 1; ++i){
        var gridRow = i - 2;
        var princess = lines[i].indexOf('p');
        
        if(princess !== -1){
            if(gridRow < marioRow){
                nextMove = 'UP';
            }else if(gridRow == marioRow){
                nextMove = princess < marioCol ? 'LEFT' : 'RIGHT';
            }else if(gridRow > marioRow){
                nextMove = 'DOWN';
            }
        }
    }

    process.stdout.write(nextMove);
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
