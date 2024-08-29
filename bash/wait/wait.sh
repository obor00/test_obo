#!/bin/bash

cat << EOF > child1.sh
#!/bin/bash
sleep 3
echo "child complete"
exit 0
EOF

cat << EOF > child2.sh
#!/bin/bash
sleep 3
echo "child2 complete"
exit 1
EOF

echo "forking child1"
bash child1.sh &

pid=$!
echo "waiting child1"
wait $pid

echo "returned value child1= $?" 

echo "forking child2"
bash child2.sh &

pid=$!
echo "waiting child2"
wait $pid

echo "returned value child2 = $?" 


echo "missing end of child"
bash child2.sh &
pid=$!
sleep 8
echo "waiting child2"
wait $pid
echo "returned value child2 = $?" 
