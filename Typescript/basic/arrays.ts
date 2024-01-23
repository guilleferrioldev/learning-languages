// Arrays 
const languages: string[] = []

languages.push('Typescript')
languages.push('Python')

const numbers: Array<number> = []

numbers.push(1)
numbers.push(2)

const array: (string | number)[] = []
array.push(1)
languages.push('Typescript')

// 
type CellValue = 'X' | 'O' | ''

// Tuple
type GameBoard = [
    [CellValue, CellValue, CellValue],
    [CellValue, CellValue, CellValue],
    [CellValue, CellValue, CellValue]
]

const gameBoard: GameBoard = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'], 
    ['O', '', 'O']
]

gameBoard[2][1] = 'O'