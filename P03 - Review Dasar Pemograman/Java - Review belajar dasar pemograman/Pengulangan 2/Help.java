package P03g_Tugas_Pengulangan_Java_2272008_Elmosius_Suli;
// File : Help.java
// Nama : Elmosius Suli
// NRP  : 2272008
// Kelas : B
// Ket : 
import java.util.*;
public class Help {
    public void tampilkan_help() {
        Scanner sc = new Scanner(System.in);
        String str;
        int pil;
    
        do{
            System.out.println("Help Percabangan & Pengulanan\n");
            System.out.println("[1] if");
            System.out.println("[2] if else");
            System.out.println("[3] if else if");
            System.out.println("[4] switch");
            System.out.println("[5] for");
            System.out.println("[6] while");
            System.out.println("[7] do while");
            System.out.println("[8] Selesai\n");

            System.out.print("Pilihan anda : ");
            pil = sc.nextInt();
            System.out.println("\n");

            switch(pil){
                case 1:
                    System.out.println("if (kondisi)");
                    System.out.println("    statement_jika_kondisi_benar");
                break;
                case 2:
                    System.out.println("if (kondisi)");
                    System.out.println("    statement_jika_kondisi_benar");
                    System.out.println("else");
                    System.out.println("    statement_jika_kondisi_salah");
                    break;
                case 3:
                    System.out.println("if (kondisi1)");
                    System.out.println("    statement_jika_kondisi1_benar");
                    System.out.println("else if (kondisi2)");
                    System.out.println("    statement_jika_kondisi2_benar");
                    System.out.println("else");
                    System.out.println("    statement_jika_semua_kondisi_salah");
                    break;
                case 4:
                    System.out.println("switch (variabel)");
                    System.out.println("    case nilai1 : statement1");
                    System.out.println("                  break;");
                    System.out.println("    case nilai2 : statement2");
                    System.out.println("                  break;");
                    System.out.println("    default     : statement_default");
                    System.out.println("                  break;");
                    System.out.println("}");
                    break;
                case 5:
                    System.out.println("for (nilai_awal; kondisi; counter)");
                    System.out.println("    statement_yg_diulang;");
                    break;
                case 6:
                    System.out.println("pengisian_nilai_awal;");
                    System.out.println("while (kondisi) {");
                    System.out.println("    statement_yg_diulang;");
                    System.out.println("    counter;");
                    System.out.println("}");
                    break;
                case 7:
                    System.out.println("pengisian_nilai_awal;");
                    System.out.println("do {");
                    System.out.println("    statement_yg_diulang;");
                    System.out.println("    counter;");
                    System.out.println("} while(kondisi);");
                    break;
                case 8 :
                    System.out.println("Sampai jumpa...");
                    break;
                default :
                    System.out.println("Pilihnya yg bener dong !");
                    break;
            }
            System.out.println("tekan ENTER untuk melanjutkan...");
            str = sc.next();

        }while(pil != 8);
    }
    public static void main(String[] args) {
        Help hlp = new Help();
        hlp.tampilkan_help();
    }
}
