export function checkEndGame(board) {
    return board.every(square => square !== null)
}