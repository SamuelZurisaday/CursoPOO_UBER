class Main {

    public static void main(String[] args) {
        System.out.println("Hola mundo");
        uberX Uberx = new Uberx("AMQ123", new Account("Andre Herrera", "AND123"), "Chevrolet", "Sonic");
        uberX.setPassenger(4);
        uberX.printDataCar();

        /*Car car2 = new Car("AKL784", new Account("Joaquín Rivera", "ANDA878"));
        car2.passenger = 3;
        car2.printDataCar();*/
    }

}