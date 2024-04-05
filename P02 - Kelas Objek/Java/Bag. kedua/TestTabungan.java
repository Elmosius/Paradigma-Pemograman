package Praktikum.P02;

import java.util.Scanner;

public class TestTabungan {
    public static void main(String[] args) {
        boolean loginBerhasil = false;

        while (!loginBerhasil) {
            if (Login.login()) {
                loginBerhasil = true;
            } else {
                System.out.println("Silakan coba lagi.");
            }
        }

        Tabungan t1 = new Tabungan("Bank ABC", "1234567890", 100000, 0 ,0);

        t1.cetakRek();

        System.out.println("Apa yang ingin dilakukan?");
        System.out.println("1. Menabung");
        System.out.println("2. Tarik Saldo");
        System.out.println("3. Tutup Rekening");
        System.out.println("0. Keluar\n");

        Scanner scanner = new Scanner(System.in);
        int pilih = scanner.nextInt();

        while (pilih != 0) {
            if (pilih == 1) {
                System.out.print("Jumlah yang ingin ditabung: ");
                int rpDitabung = scanner.nextInt();
                t1.menabung(rpDitabung);
            } else if (pilih == 2) {
                System.out.print("Jumlah yang ingin diambil: ");
                int rpDiambil = scanner.nextInt();
                t1.mengambil(rpDiambil);
            } else if (pilih == 3) {
                t1.tutupRek();
            }

            t1.cetakRek();

            System.out.println("Apa yang ingin dilakukan?");
            System.out.println("1. Menabung");
            System.out.println("2. Tarik Saldo");
            System.out.println("3. Tutup Rekening");
            System.out.println("0. Keluar \n");

            pilih = scanner.nextInt();
        }

    scanner.close();
    }
}

