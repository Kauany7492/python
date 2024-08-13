<!DOCTYPE html>
<html>
<body>

<h1>My first PHP page</h1>

<?php
class Carro{
    public $cor;
    public $modelo;
    public function __construct($cor, $modelo){
        $this -> cor = $cor;
        $this -> modelo = $modelo;
    }
    public function mensage(){
        return "Meu carro é " . $this -> modelo . " " . $this -> cor . "!"; 
    }
}

$meucarro = new Carro("vermeho", "Volvo");
var_dump($meucarro);
?>

</body>
</html>