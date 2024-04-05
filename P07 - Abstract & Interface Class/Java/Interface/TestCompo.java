// file : TestCompo.java
// note : kelas test latihan interface 2
public class TestCompo {
    public static void main(String[] args) {
        Compo compoku = new Compo();

        compoku.setGelombang(92.5);
        System.out.println(compoku.getSiaran());
        System.out.println("gelombang: " + compoku.getGelombang() + " MHz\n");

        compoku.setPuterKaset("Jazzy Bass");
        System.out.println(compoku.getDengerKaset());
        System.out.println("kaset: " + compoku.getKaset() + "\n");
    }
}
