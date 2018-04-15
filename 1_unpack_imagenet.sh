mkdir train
mkdir val
tar xvf ILSVRC2012_img_train.tar -C train
tar xvf ILSVRC2012_img_val.tar -C val

cd train
for tarball in `ls *.tar`
do
    filename=`basename $tarball .tar`
    mkdir $filename
    tar -xvf $tarball -C ./$filename
done

rm *.tar

