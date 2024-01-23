interface IAvenger {
    name: string;
    powerScore: number;
}

class Avenger implements IAvenger{
    readonly name: string;
    powerScore: number;
    private age: number
    protected readonly superpower: string

    constructor(name: string, powerScore: number, age: number, superpower: string){
        this.name = name 
        this.powerScore = powerScore
        this.age = age
        this.superpower = superpower
    }

    get fullName(): string{
        return `${this.name}, power ${this.powerScore}`
    }

    set power(newPower: number){
        if (newPower <= 100) {
            this.powerScore = newPower
        } else {
            throw new Error('Power Score cannot be more then 100')
        }
    } 
}

const spidey = new Avenger('Spiderman', 89, 26, "spider webs")
