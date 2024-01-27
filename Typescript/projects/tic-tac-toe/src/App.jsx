import { useState } from "react"
import { Square } from './components/Square.jsx'
import { WinnerModal } from './components/WinnerModal.jsx'
import { ShowBoard } from "./components/ShowBoard.jsx"

import { checkWinner } from "./logic/CheckWInner.jsx"
import { checkEndGame } from "./logic/CheckEndGame.jsx"

const TURNS = {
    X: '❌',
    O: '⚪'
}

function App() {
    const [board, setBoard] = useState(() => {
        const boardFromStorage = window.localStorage.getItem('board')
        if (boardFromStorage) return JSON.parse(boardFromStorage)
        return Array(9).fill(null)
      })
    

    const [turn , setTurn] = useState(() => {
        const turnFromStorage = window.localStorage.getItem('turn')
        return turnFromStorage ?? TURNS.X
    })

    const [winner, setWinner] = useState(null)
    
    const updateBoard = (index) => {
        if (board[index] || winner)  return

        const newBoard = [...board]
        newBoard[index] = turn
        setBoard(newBoard)
        
        const newTurn = turn === TURNS.X ? TURNS.O : TURNS.X
        setTurn(newTurn)

        window.localStorage.setItem('board', JSON.stringify(newBoard))
        window.localStorage.setItem('turn', newTurn)

        const newWInner = checkWinner(newBoard)
        if (newWInner) {
            setWinner(newWInner)
        } else if (checkEndGame(newBoard)){
            setWinner(false)
        }

    }

    const resetGame = () => {
        setBoard(Array(9).fill(null))
        setTurn(TURNS.X)
        setWinner(null)

        window.localStorage.removeItem('board')
        window.localStorage.removeItem('turn')
    }

    return (
        <main className='board'>
            <h1>Tic tac toe</h1>
            
            <ShowBoard board={board} updateBoard={updateBoard}/>
            
            <section className="turn">
                <Square isSelected={turn === TURNS.X}>
                    {TURNS.X}
                </Square>
                <Square isSelected={turn === TURNS.O}>
                    {TURNS.O}
                </Square>
            </section>

            <button onClick={resetGame}>Reset Game</button>

            <WinnerModal resetGame={resetGame} winner={winner} />
        </main>
    )
}

export default App
