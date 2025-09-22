using System;
using System.Dynamic;
using System.Runtime.Versioning;

//classe Super

abstract class Animal{
    
    //Atributos + Acesso
        //Getters and Setters --> Método 1
    public string Nome //ATT --> public
        {get;set;} = "";
    
    //Metodos

    public abstract void EmitirSom();

    //Virtual
    public virtual void Comer(){
        Console.WriteLine($"{Nome} está comendo.");
    }
}

//Subclasse

class Cachorro : Animal{ 
    //Atributos + Acesso

    private string raca = "";

        //Getters and Setters --> Método 2
    public string Raca{
        get{return raca;}
        set{raca = value;}
    }
    //Construtor

    //Métodos
    public override void EmitirSom(){
        Console.WriteLine("Woof woof");
    }

    public override void Comer(){
        base.Comer();
        Console.WriteLine($"{Nome} está satisfeito.");
    }

}

//Main

class Program{
    public static void Main(string[] args){
        //Instanciação de um novo Cachorro
        Cachorro cachorro_1 = new Cachorro();
            
            //Setters
            cachorro_1.Nome = "Max";
            cachorro_1.Raca = "German Shepherd";
            
            //Métodos
            cachorro_1.EmitirSom();
            cachorro_1.Comer();

        Console.WriteLine($"{cachorro_1.Nome} é da raça {cachorro_1.Raca}");
    }
}