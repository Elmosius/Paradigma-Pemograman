package Praktikum.P02;
// File : CekJam
class Jam {
    private int jam;
    private int menit;
    private int detik;

    public Jam() { this(0,0,0);}

    public Jam(int j) { this(j,0,0);}

    public Jam(int j, int m){this(j,m,0);}

    public Jam(int j, int m, int d){ setJam(j,m,d);}

    public void setJam(int a, int b, int c){
        this.jam = a;
        this.menit = b;
        this.detik = c;
    }

    public String getJam(){
        String waktu = "";
        waktu = this.jam + ":" + this.menit + ":" + this.detik;
        return waktu;
    }
}

public class Cekjam {
    public static void main(String[] args){
        String infoWaktu;
        Jam jamKu = new Jam(10,15,40);

        infoWaktu = jamKu.getJam();
        System.out.print("Informasi Waktu : " + infoWaktu);
        System.exit(0);
    }
}
