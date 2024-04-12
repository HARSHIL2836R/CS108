for file in {spl.py,split.py,style.py,subplot.py,sum_prod.py,trig.py,vect.py,where.py};
do
echo $'\n' >> $file
echo "''' $(python3 $file) '''" >> $file
done