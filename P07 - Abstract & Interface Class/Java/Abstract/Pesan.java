// file : MusikTiup.java
// note : latihan abstract class 3
abstract class Pesan {
    // method abstract untuk menulis pesan
    abstract public void setPesan(String pesannya);

    // method abstract untuk melihat pesan
    abstract public String getPesan();

    // method abstract untuk mengisi pengirim
    abstract public void setPengirim(String pengirimnya);

    // method abstract untuk melihat pengirim
    abstract public String getPengirim();

    // method abstract untuk mengisi tujuan
    abstract public void setTujuan(String tujuannya);

    // method abstract untuk melihat tujuan
    abstract public String getTujuan();
}
