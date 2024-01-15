/* Template union types*/

type HexadecimalColor = `#${string}`

const color: HexadecimalColor = '#0033ff' 

type HeroId = `${string}-${string}-${string}-${string}-${string}`

/* Union Types */ 
type HeroPowerScale = 'local' | 'planetary' | 'galactic' 
                      |'universal' | 'multiversal' 


/* Type Alias */
type HeroBasicInfo = {
    name : string
    age: number
}

type HeroProperties = {
    /* Optional properties */
    readonly id?: HeroId
    isActive?: boolean 
    powerScacle?: HeroPowerScale
}

/* Intersection Types */
type Hero = HeroBasicInfo & HeroProperties

let hero: Hero = {
    name: "Thor",
    age: 1500
};

function createHero (name: string, age: number): Hero {
    return {name, age}
};

const thor = createHero('Thor', 1500);

function createMoreHeros (basic: HeroBasicInfo): Hero {
    const {name, age} = basic
    return {
        id: crypto.randomUUID(),
        name,
        age,
        isActive: true}
}

/* Immutable */
const anotherThor = Object.freeze(createMoreHeros({name: 'Thor', age: 1500}))

anotherThor.id?.toString()


/* Type indexing */ 
type HeroAdreess = {
    isAcrive: boolean, 
    address: {
        planet: string,
        city: string
    }
}

const addressHero: HeroAdreess['address'] = {
    planet: 'Earth',
    city: 'Barcelona'
}

/* Type from value */ 
type Address = typeof addressHero
 
const addressMadrid: Address = {
    planet: 'Earth',
    city: 'Madrid'
}

/* Type from function return */ 
function createAddress() {
    return {
        planet: 'Earth',
        city: 'New York'
    }
}

type AnotherAddress = ReturnType<typeof createAddress>/* Type of value */ 


