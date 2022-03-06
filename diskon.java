import java.util.*;
public class diskon {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        //deklarasi
        int jumlahbarang,hargasatuan,hargabarang;
        double diskon1,diskon2;

        //input user
        System.out.print("masukan jumlah barang = ");
        jumlahbarang = input.nextInt();
        System.out.print("masukan harga satuan barang = ");
        hargasatuan = input.nextInt();

        //proses
        hargabarang =  jumlahbarang * hargasatuan;
        System.out.println("harga barang anda sebesar = Rp " + hargabarang);

        //percabangan
        if (hargabarang > 1500000) {
            diskon1 = hargabarang-(0.35*hargabarang);
            diskon2 = diskon1 - (0.15*diskon1);
        } else if (hargabarang >=750000 && hargabarang == 1500000) {
            diskon1 = hargabarang-(0.15*hargabarang);
            diskon2 = diskon1 - (0.10*diskon1);
        } else {
            diskon2 = 0;
        }
        System.out.println("harga yang harus anda bayar = Rp "+diskon2);

        input.close();
    }
}
