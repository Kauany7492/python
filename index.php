<!DOCTYPE html>
<html>
<body>

<h1>My first PHP page</h1>

<?php
class carro{
  public $cor;
  public $modelo/
  public function __construct($cor, $modelo){
    $this -> cor = $cor;
    $this -> modelo = $modelo;
  }
  public function mensage(){
    return "Meu carro é ". $this -> modelo. " ". $this -> cor."!";
  }
}

$meucarro = new carro("azul", "stilo");
var_dump($meucarro);
?>

</body>
</html>
