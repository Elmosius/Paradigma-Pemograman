// Menyisipkan dokumentasi langsung di dalam program & di generate dg Javadoc

/**
 * Ini adalah bentuk komentar di Java yg dapat di generate
 * langsung menjadi dokumentasi dengan menggunakan program javadoc.
 * Formatnya /** .... * /
 */

 /** 
  * <b> Kelas03 </b> adalah kelas untuk menunjukkan javadoc <br>
  * Dapat menggunakan tag2 html <br>
  * Ada annotasi2 khusus (tanda @) yg memiliki arti tertentu <br>
  * Dari cmd eksekusi dengan: javadoc Kelas03.java <br>
  * Dari IntelliJ menu: Tools | Generate Javadoc... <br>
  *
  * @author Elmo  
  * @version 1.0
  * @since 27/09/2023 
 */
package Praktikum.P02;

public class Kelas03 {
    /**
     * Ini adalah method main() <br>
     * @param args Nothing 
     */
    public static void main(String[] args){
        System.out.println("Hallo Dunia... mari belajar Java!");
    }
}
