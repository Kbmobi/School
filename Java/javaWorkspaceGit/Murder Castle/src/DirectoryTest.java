import static org.junit.Assert.*;

import java.util.Comparator;

import org.junit.Before;
import org.junit.Test;


public class DirectoryTest {

	Directory who;
	
	@Before
	public void setUp() throws Exception {
		who = new Directory("Jack", "Smith", 0);
	}

	@Test
	public void comparatorByLastName() {
		Directory aSmith = new Directory("Able", "Smith", 0);
		Directory bSmith = new Directory("Baker", "Smith", 0);
		Directory cSmith = new Directory("Charlie", "Smith", 0);
		
		Comparator<Directory> comp = Directory.byLastName();
		
		assertTrue(comp.compare(aSmith, bSmith) < 0);
		assertTrue(comp.compare(bSmith, aSmith) > 0);
		
		assertTrue(comp.compare(bSmith, cSmith) < 0);
		assertTrue(comp.compare(cSmith, bSmith) > 0);
		
		assertTrue(comp.compare(aSmith, cSmith) < 0);
		assertTrue(comp.compare(cSmith, aSmith) > 0);
	}

}
