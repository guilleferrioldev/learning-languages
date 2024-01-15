/* Type Alias */
type Hero = {
    /* Optional properties */
    readonly id?: number,
    name : string, 
    age: number,
    isActive?: boolean 
}

let hero: Hero = {
    name: "Thor",
    age: 1500
};

function createHero (name: string, age: number): Hero {
    return {name, age}
};

const thor = createHero('Thor', 1500);

function createMoreHeros (hero: Hero): Hero {
    const {name, age} = hero
    return {name, age, isActive: true}
}

/* Immutable */
const anotherThor = Object.freeze(createMoreHeros({name: 'Thor', age: 1500}))

anotherThor.id?.toString()
