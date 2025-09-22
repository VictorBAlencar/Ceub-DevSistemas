using System;

//classe Super

class Animal{
    
    //Atributos
    public string nome = "";
    
    //Metodos

    public virtual void EmitirSom(){
        Console.WriteLine($"Animal: {nome}");
    }

    public virtual void Comer(){
        Console.WriteLine($"Animal: {nome} está comendo.");
    }

    //Polimorfismo Estático
    public virtual void EmitirSom(string msg){
        Console.WriteLine($"Animal está dizendo: {msg}");
    }
}

//Subclasse

class Cachorro : Animal{ //: --> extends
    //Atributos
    public string raca = "";
    
    //Override --> polimorfismo dinâmico
    public override void EmitirSom(){
        base.EmitirSom();
        Console.WriteLine("Woof woof");
    }

    public override void Comer(){
        base.Comer(); //base --> degrau da hierarquia super.
        Console.WriteLine($"{nome} está comendo ração.");
    }

}

//Main

class Program{
    public static void Main(string[] args){
        Animal animal_1 = new Animal();
            animal_1.nome = "Animal 1";
            animal_1.EmitirSom();
            animal_1.Comer();
            animal_1.EmitirSom("Olá"); //Estático

        Cachorro cachorro_1 = new Cachorro();
            cachorro_1.nome = "Max";
            cachorro_1.raca = "German Shepherd";
            cachorro_1.EmitirSom();
            cachorro_1.Comer();
    }
}