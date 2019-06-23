cat result.txt | sed -e '1,4d' > temp.csv
cat temp.csv | cut -d , -f 1 > result.txt
sort result.txt | uniq -d | wc -l
