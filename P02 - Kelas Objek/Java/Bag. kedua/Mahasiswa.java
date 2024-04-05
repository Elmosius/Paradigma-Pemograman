package Praktikum.P02;

public class Mahasiswa {
    private String noInduk;  // Field noInduk
    private int totalSks;    // Field totalSks
    private double ipk;      // field ipk

    // constuctor 1
    public Mahasiswa(){
        this.noInduk = "???";
        this.totalSks = 0;
        this.ipk = 0.0;
    }

     // constuctor 2
    public Mahasiswa(String noInduknya, int totalSksnya){
        this.noInduk = noInduknya;
        this.totalSks = totalSksnya;
        this.ipk = 0.0;
    }

     // constuctor 3
    public Mahasiswa(String noInduknya, int totalSksnya, double ipknya){
        this.noInduk = noInduknya;
        this.totalSks = totalSksnya;
        this.ipk = ipknya;
    }

    // method meminta noInduk Mahasiswa
    public String getNoInduk(){
        return this.noInduk;
    }

    // method meminta totalSks Mahasiswa
    public int getTotalSks(){
        return this.totalSks;
    }

    // method meminta ipk Mahasiswa
    public double getIpk(){
        return this.ipk;
    }
    
    // method mengisi totalSks Mahasiswa
    public void setTotalSks(int totalSksnya){
        this.totalSks = totalSksnya;
    }

    // method mengisi ipk Mahasiswa
    public void setIpk(int ipknya){
        this.ipk = ipknya;
    }

    //  methos memproses prestasi Mahasiwa
    public void prestasi(){
        if(this.ipk > 3.5){
            System.out.print("Sangat baik");
        }
        else if(this.ipk > 3.0) {
            System.out.print("Baik");
        }
        else if(this.ipk > 2.0){
            System.out.print("Cukup");
        }
        else {
            System.out.print("Masih perlu banyak belajar");
        }
    }
}
