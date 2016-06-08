B1;2cmkdir temp
mv *.tgz temp
cd temp
for i in $(ls | grep tgz); do
    tar -xzf $i
done
rm *.tgz
for i in $(ls); do
    for j in $(ls $i); do
       echo "mv $i/$j/*.pdf ../$i/$j/"
    done
done
