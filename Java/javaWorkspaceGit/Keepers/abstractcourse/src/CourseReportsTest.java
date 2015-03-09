
import static org.junit.Assert.*;

import java.util.Iterator;

import org.junit.Before;
import org.junit.Test;


public class CourseReportsTest {

	AbstractCourseReports thisWeek;
	
	@Before
	public void setUp() throws Exception {
		thisWeek = new CourseReports("110220");
		
		thisWeek.addReport(new CourseHoursTotals("Comp101", 3));
		thisWeek.addReport(new CourseHoursTotals("Comp101", 6));
		thisWeek.addReport(new CourseHoursTotals("Bus111", 10));
		thisWeek.addReport(new CourseHoursTotals("Eng201", 5));
		thisWeek.addReport(new CourseHoursTotals("Bus111", 5));
		thisWeek.addReport(new CourseHoursTotals("Eng201", 8));
		thisWeek.addReport(new CourseHoursTotals("Comp101", 3));
	}
	
	@Test
	public void constructor() {
		AbstractCourseReports thisWeek = new CourseReports("110220");
		assertTrue(thisWeek.getWeekOf().equals("110220"));
		
		Iterator<CourseHoursTotals> iter = thisWeek.iterator();
		assertTrue(iter.hasNext() == false);
	}
	
	@Test
	public void iterable() {
		assertTrue(thisWeek instanceof Iterable<?>);
	}
	
	@Test
	public void iterator() {
		Iterator<CourseHoursTotals> iter = thisWeek.iterator();
		
		AbstractCourseHoursTotals current;
		
		current = iter.next();
		String courseName = current.getCourseName();
		assertTrue(current.getCourseName().equals("Bus111"));

		current = iter.next();
		assertTrue(current.getCourseName().equals("Eng201"));

		current = iter.next();
		assertTrue(current.getCourseName().equals("Comp101"));
		
		assertTrue(iter.hasNext() == false);
	}
	
	@Test
	public void iteratorCourseOrder() {
		Iterator<CourseHoursTotals> iter = thisWeek.iteratorByCourse();
		
		AbstractCourseHoursTotals current;
		
		current = iter.next();
		assertTrue(current.getCourseName().equals("Bus111"));

		current = iter.next();
		assertTrue(current.getCourseName().equals("Comp101"));

		current = iter.next();
		assertTrue(current.getCourseName().equals("Eng201"));
		
		assertTrue(iter.hasNext() == false);
	}
	
	@Test
	public void iteratorAverageHoursOrder() {
		Iterator<CourseHoursTotals> iter = thisWeek.iteratorByAverageHours();
		
		AbstractCourseHoursTotals current;
		
		current = iter.next();
		assertTrue(current.getCourseName().equals("Bus111"));
		assertTrue(current.getTotalHoursSpent() == 10 + 5);

		current = iter.next();
		assertTrue(current.getCourseName().equals("Eng201"));
		assertTrue(current.getTotalHoursSpent() == 5 + 8);
		
		current = iter.next();
		assertTrue(current.getCourseName().equals("Comp101"));
		assertTrue(current.getTotalHoursSpent() == 3 + 6 + 3);

		assertTrue(iter.hasNext() == false);
	}
}
