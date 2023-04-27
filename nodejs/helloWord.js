class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    describe () {
        return `${this.name}, ${this.age} years old`;
    }
}

class Programmer extends Person {
    constructor(name, age, ...languages) {
        super(name, age);
        this.languages = languages;
    }

    describe () {
        return `${super.describe()}, ${this.languages.length} languages`;
    }

    code () {
        return `${this.name} is coding in ${this.languages.join(', ')}`;
    }
}

const person = new Person('John', 25);
console.log(person.describe());

const programmer = new Programmer('Jane', 22, 'JavaScript', 'Python', 'Java');
console.log(programmer.describe());
console.log(programmer.code());