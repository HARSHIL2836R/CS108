for file in *.py;
do
echo $'\n' >> $file
echo "''' $(python3 $file) '''" >> $file
done