// file : AnekaFlora.java
// note : kelas test latihan interface
public class AnekaFlora {
    public static void main(String[] args) {
        Kaktus kaktusku = new Kaktus();
        Melati melatiku = new Melati();

        kaktusku.keterangan();
        System.out.println("ciri:");
        System.out.println("\t" + kaktusku.getFotosintesis());
        System.out.println("\t" + kaktusku.getBerduri());

        
        melatiku.keterangan();
        System.out.println("ciri:");
        System.out.println("\t" + melatiku.getFotosintesis());
        System.out.println("\t" + melatiku.getBerbunga());
    }
}
