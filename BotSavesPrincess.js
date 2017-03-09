function processData(input) {
    var lines = input.split('\n');
    var dimension = parseInt(lines[0]);
    var grid = [];
    for(var i = 1; i <= dimension; ++i)
    {
        grid.push(lines[i]);
    }
    displayPathtoPrincess(dimension, grid);
}

function displayPathtoPrincess(dimension, grid)
{
    var moves = [];
    
    function _appendMoves(direction, amount){
        for(i = 0; i < amount; i++){
            moves.push(direction);
        }    
    }
        
    if(grid[0].indexOf('p') !== -1){
        
        if(grid[0].indexOf('p') == 0){
            _appendMoves('LEFT', ((dimension - 1) / 2));
        }else
        {
            _appendMoves('RIGHT', ((dimension - 1) / 2));
        }
        
        _appendMoves('UP', ((dimension - 1) / 2));

    }else{
        if(grid[dimension - 1].indexOf('p') == 0){
            _appendMoves('LEFT', ((dimension - 1) / 2));
        }else
        {
            _appendMoves('RIGHT', ((dimension - 1) / 2));
        }
        
        _appendMoves('DOWN', ((dimension - 1) / 2));
    }
    
    process.stdout.write(moves.join('\n'));
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
