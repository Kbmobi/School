import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class BottleTest {
	
	@Before
	public void setUp() throws Exception {
	}

	@Test
	public void testBottle() {
		Bottle myBottle = new Bottle(600 ,0 ,0);
		
		int maxCapacity = myBottle.getMaxCapacity();
		assertTrue(maxCapacity == 600);
		
		int minCapacity = myBottle.getMinCapacity();
		assertTrue(minCapacity == 0);
		
		int currentCapacity = myBottle.getCurrentCapacity();
		assertTrue(currentCapacity == 0);
	}
	
	@Test
	public void fillBottle() {
		Bottle myBottle = new Bottle(600 ,0 ,595);
		
		int currentCapacity = myBottle.getCurrentCapacity();
		assertTrue(currentCapacity == 595);
		
		myBottle.fill();
		myBottle.fill();
		myBottle.fill();
		myBottle.fill();
		myBottle.fill();
		
		currentCapacity = myBottle.getCurrentCapacity();
		assertTrue(currentCapacity == 595 + 5);
		
		myBottle.fill();
		
		currentCapacity = myBottle.getCurrentCapacity();
		assertTrue(currentCapacity == 595 + 5);
		
	}

	@Test
	public void dumpBottle() {
		Bottle myBottle = new Bottle(600 ,0 ,5);
		
		int currentCapacity = myBottle.getCurrentCapacity();
		assertTrue(currentCapacity == 5);
		
		myBottle.dump();
		myBottle.dump();
		myBottle.dump();
		myBottle.dump();
		myBottle.dump();
		
		currentCapacity = myBottle.getCurrentCapacity();
		assertTrue(currentCapacity == 5 - 5);
		
		myBottle.dump();
		
		currentCapacity = myBottle.getCurrentCapacity();
		assertTrue(currentCapacity == 5 - 5);
		
	}
	
	@Test
	public void nameCheck() {
		Bottle myBottle = new Bottle(600 ,0 ,5);
		
		String contents = myBottle.getBottleName();
		assertTrue(contents.equals("Water"));
	}
}
