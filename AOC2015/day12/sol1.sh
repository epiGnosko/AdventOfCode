cat input.txt | grep -o -E "[0-9]+" | awk '{sum += $1} END {print sum}'
