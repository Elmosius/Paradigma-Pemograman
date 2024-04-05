package P03b_Latihan_Tipe_Data_Java_2272008_Elmosius_Suli;

    // File : Boolean2.java
    // Nama : Elmosius Suli
    // NRP  : 2272008
    // Kelas : B
    // Ket : 

public class Boolean2 {
    public static void main(String[] args) {
        boolean a,b,c;

        a = true;
        b = false;

        System.out.println("Latihan Operasi Logika\n");
        System.out.println("operasi and (&&) : ");
        System.out.println("true && true = " + (a && a));
        System.out.println("true && false = " + (a && b));
        System.out.println("false && true = " + (b && a));
        System.out.println("false && false = " + (a && a));

        System.out.println("\noperasi or (||) : ");
        System.out.println("true && true = " + (a || a));
        System.out.println("true || false = " + (a || b));
        System.out.println("false || true = " + (b || a));
        System.out.println("false || false = " + (a || a));

        System.out.println("\noperasi xor (^) : ");
        System.out.println("true ^ true = " + (a ^ a));
        System.out.println("true ^ false = " + (a ^ b));
        System.out.println("false ^ true = " + (b ^ a));
        System.out.println("false ^ false = " + (a ^ a));

        System.out.println("\noperasi not (^) : ");
        System.out.println("!true = " + ((!a)));
        System.out.println("!false = " + (!b));
    }
}
