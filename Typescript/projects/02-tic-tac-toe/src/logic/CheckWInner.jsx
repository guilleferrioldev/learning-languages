export function checkWinner(board) {
    // Check rows
    for (let i = 0; i < 9; i += 3) {
        if (board[i] === board[i + 1] && board[i + 1] === board[i + 2] && board[i] !== ' ') {
            return board[i]; 
        }
    }

    // Check columns
    for (let i = 0; i < 3; i++) {
        if (board[i] === board[i + 3] && board[i + 3] === board[i + 6] && board[i] !== ' ') {
            return board[i]; 
        }
    }

    // Check diagonals
    if ((board[0] === board[4] && board[4] === board[8]) || 
        (board[2] === board[4] && board[4] === board[6]) && 
         board[4] !== ' ') {
        return board[4];  
    }

    return null;
}