function showLength (object: string | number) {
    if (typeof object === 'string'){
        return object.length
    }   
    return object.toString().length
}

showLength('1');


//
interface Character {
    company: string,
    name: string,
};

interface Mario extends Character{    
    jump: () => void
};

interface Sonic extends Character{
    run: () => void
};

type Cartoon = Mario | Sonic; 

// Type Guard
function checkIsSonic(character: Cartoon): character is Sonic {
    return (character as Sonic).run != undefined
}

function play(character: Cartoon): void {
    if (checkIsSonic(character)) {
        character.run()
    } else {
        character.jump()
    }
}

//
function anotherPlay(character: Cartoon): void {
    if ('run' in character) {
        character.run()
    } else {
        character.jump()
    }
}
