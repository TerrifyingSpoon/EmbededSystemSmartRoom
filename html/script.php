<?php

system("gpio -g mode 24 out");

if($_POST['executer'] == 'Allumer')
{
	system("gpio -g write 24 1");
}
if($_POST['executer'] == 'Eteindre')
{
	system("gpio -g write 24 0");
}

header('Location: index.php');
?>
