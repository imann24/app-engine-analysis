# Author: Isaiah Mann
# Description: Runs the python program a specified number of times from a range of 1 to specified amount
# Description (cont.): on the preset App Engine URL and outputs to a specified file (CSV format)
# Usage: ./run.sh [upper bound on requests] [file to save results to]

echo "Request Count, Average Response Time (secs)" | cat >> $2
for ((i=1; i<=$1; i++))
do
     python main.py https://electric-nomad-165723.appspot.com/ $i | cat >> $2
done
