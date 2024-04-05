package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : ParameterMain.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
public class ParameterMain {
    public static void main(String[] args) {
        // Proses setiap paramater
        for(int i=0; i<args.length; i++){
            System.out.println("Parameter ke-" + i + " : " + args[i]);
        }
        System.out.println("Hellow World!");
    }
}
