package Praktikum.P02;
public class Kelas02 {
    // Method main() di Java ditulis di dalam teks
    // atau di kelas terpisah

    public static void main(String[] args){
        Kelas02 k;

        k = new Kelas02();
        System.out.println("Objek k         : " + k); 
        System.out.println("Hashcode k      : " + k.hashCode());
        System.out.println("Objek k         : " + k.getClass());
    
    }

}
