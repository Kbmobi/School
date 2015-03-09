
public class Driver {
	
	public static void main(String[] args) {
		
		Bottle myBottle = new Bottle(600 ,0 ,0);
		
		System.out.println(myBottle.toString());
		
		myBottle.fill();
		myBottle.fill();
		
		System.out.println("Bottle has "+myBottle.getCurrentCapacity() + "ml out of "+ myBottle.getMaxCapacity() + "ml");
	}

}
