
declare -A v[A]="a"
v[B]="b"

echo "v=${v[@]}"

declare -A z
z=${v[@]}

echo "z=${z[@]}"
