using System;


class Pessoa{
    //Atributos - Propriedades da Classe
    public string nome = ""; // Modelo --> acesso / proteção + tipo + nome + inicialização + ; 
    public int idade = 0;

    //Método da Classe

    public void Apresentar(){
        // Console.WriteLine("Olá, meu nome é " + nome + " e tenho " + idade + " anos."); // Alternativa 1
        Console.WriteLine($"Olá, meu nome é {nome} e tenho {idade} anos."); // Alternativa 2
    }
}


class Carro{
    //Atributos

    private string marca = "";

    private string modelo = "";

    private int anoDeFabricacao = 0;

    //Construtores

    public Carro(string marca, string modelo, int anoDeFabricacao){
        this.marca = marca; //this --> referencia à classe
        this.modelo = modelo;
        this.anoDeFabricacao = anoDeFabricacao;
    }

    //Métodos da Classe

    public void Ligar(){
        Console.WriteLine($"{marca} {modelo} de {anoDeFabricacao} está ligado!");
        Console.WriteLine($"{marca} {modelo} de {anoDeFabricacao} está ligado!");
    }

    //Getters / Setters


    public void SetModelo(string modelo){
        if(modelo != ""){
            this.modelo = modelo;
        }
    }


    public void SetMarca(string marca){
        if(marca != ""){
            this.marca = marca;
        }
    }

    public void SetAnoDeFabricacao(int anoDeFabricacao){
        if(anoDeFabricacao >= 1885){
            this.anoDeFabricacao = anoDeFabricacao;
        }
    }

    public string GetModelo(){
        return modelo;
    }

    public string GetMarca(){
        return marca;
    }

    public int GetAnoDeFabricacao(){
        return anoDeFabricacao;
    }
}

class Program{
    static void Main(string[] args){ //static = único | Main --> roda o programa |  //Funções precisam de ()
        /*Pessoa pessoa_1 = new Pessoa();
            pessoa_1.nome = "Victor";
            pessoa_1.idade = 21;

            pessoa_1.Apresentar();
        */

        Carro carro_1 = new Carro("Honda","Civic", 2015);
            carro_1.Ligar(); //Construtor
            carro_1.SetModelo("Corolla");
            carro_1.SetMarca("Toyota");
            carro_1.SetAnoDeFabricacao(2016);
            carro_1.Ligar(); //Setters
            
            Console.WriteLine($"Marca: {carro_1.GetMarca()} \n"); // Carro --> classe - ideia | carro_1 --> objeto - fisico
            Console.WriteLine($"Modelo: {carro_1.GetModelo()} \n");
            Console.WriteLine($"Ano de Fabricação: {carro_1.GetAnoDeFabricacao()} \n");
    }
}
