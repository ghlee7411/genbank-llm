curl -s https://ftp.ncbi.nih.gov/genbank/ | awk -F'"' '/href/ {print $2}' > file_list.txt
cat file_list.txt | grep "^gb.*\.seq\.gz$" | xargs -I{} -n 1 -P 4 wget -c -nv https://ftp.ncbi.nih.gov/genbank/{}
