// file : MusikTiup.java
// note : latihan abstract class 3
interface  Pesan {
    // method interface untuk menulis pesan
    void setPesan(String pesannya);

    // method interface untuk melihat pesan
    String getPesan();

    // method interface untuk mengisi pengirim
    void setPengirim(String pengirimnya);

    // method interface untuk melihat pengirim
    String getPengirim();

    // method interface untuk mengisi tujuan
    void setTujuan(String tujuannya);

    // method interface untuk melihat tujuan
    String getTujuan();
}
