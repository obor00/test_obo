# example 1
 timeout 10s bash << FIN
ff()
{
echo "hello obo"
}

ff
sleep 5 
echo "fini"

FIN


# example 2
ff() { echo $a1; sleep 5; echo "fin" ; }
timeout 3 cat <( ff )

