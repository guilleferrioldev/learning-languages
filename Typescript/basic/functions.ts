function myAge(age: number): string { 
    return `I'am ${age} years old`
}

let age = myAge(5)

function greet ({name, age}: {name: string, age: number}): string {
    return `${name} is ${age} years old`
}

let username: string
username = greet({name: 'Pepe', age: 20})


// Arrow function
const sayHiFromFunction = (fn: (name: string) => string): string => {
    return fn('Miguel')
}

const sayHi = (name: string): string => {
    return `Hi ${name}`
}

sayHiFromFunction(sayHi)

// Typing arrow functions
const sum = (a: number, b: number): number => {
    return a + b
}

const minus: (a: number, b: number) => number = (a, b) => {
    return a - b
}

// never 
function throwError(message: string): never {
    throw new Error(message)
}


//
const avengers = ['Spidey', 'Hulk', 'Ironman']

avengers.forEach(avenger => {
    console.log(avenger.toUpperCase())
})




