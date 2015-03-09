
import static org.junit.Assert.*;

import java.util.Comparator;

import org.junit.Before;
import org.junit.Test;

public class CourseHoursTotalsTest {
	
	AbstractCourseHoursTotals aCourse;

	@Before
	public void setUp() throws Exception {
		aCourse = new CourseHoursTotals("totals", 10);
	}
	
	@Test
	public void testConstructor() {
		assertTrue(aCourse.getCourseName().equals("totals"));
		assertTrue(aCourse.getTotalHoursSpent() == 10);
		assertTrue(aCourse.getReportCount() == 1);
	}
	
	@Test
	public void addHoursWorks() {
		aCourse.addTime(19);
		assertTrue(aCourse.getTotalHoursSpent() == 29);
		assertTrue(aCourse.getReportCount() == 2);
		assertTrue(aCourse.getAverageHours() == 29.0 / 2);
	}
	
	@Test
	public void comparable() {
		assertTrue(aCourse instanceof Comparable<?>);
	}
	
	@Test
	public void equalsWorks() {
		AbstractCourseHoursTotals original = new CourseHoursTotals("original", 20);
		AbstractCourseHoursTotals looksLikeOriginal = new CourseHoursTotals("original", 10);
		
		assertTrue(original.equals(looksLikeOriginal));
	}
	
	@Test
	public void compareToWorks() {
		AbstractCourseHoursTotals bigger = new CourseHoursTotals("aaa", 20);
		AbstractCourseHoursTotals smaller = new CourseHoursTotals("zzz", 10);
	
		assertTrue(bigger.compareTo(smaller) > 0);
		assertTrue(smaller.compareTo(bigger) < 0);
	}
	
	@Test
	public void courseByName() {
		Comparator<AbstractCourseHoursTotals> comp = CourseHoursTotals.getByCourseName();
		
		AbstractCourseHoursTotals bigger = new CourseHoursTotals("zzz", 10);
		AbstractCourseHoursTotals smaller = new CourseHoursTotals("aaa", 500);
		
		assertTrue(comp.compare(bigger, smaller) > 0);
		assertTrue(comp.compare(smaller, bigger) < 0);
	}
	
	@Test
	public void courseByAverage() {
		Comparator<AbstractCourseHoursTotals> comp = CourseHoursTotals.getByAverageHours();
		
		AbstractCourseHoursTotals bigger = new CourseHoursTotals("aaa", 10);
		bigger.addTime(10);
		bigger.addTime(10);
		
		AbstractCourseHoursTotals smaller = new CourseHoursTotals("zzz", 5);
		smaller.addTime(5);
		smaller.addTime(5);
		
		assertTrue(comp.compare(bigger, smaller) > 0);
		assertTrue(comp.compare(smaller, bigger) < 0);
		
		bigger = new CourseHoursTotals("zzz", 10);
		bigger.addTime(10);
		bigger.addTime(10);
		
		smaller = new CourseHoursTotals("aaa", 5);
		smaller.addTime(5);
		smaller.addTime(5);
		
		assertTrue(comp.compare(bigger, smaller) > 0);
		assertTrue(comp.compare(smaller, bigger) < 0);
		
		bigger = new CourseHoursTotals("zzz", 10);
		bigger.addTime(10);
		
		smaller = new CourseHoursTotals("aaa", 10);
		smaller.addTime(5);
		smaller.addTime(5);
		
		assertTrue(comp.compare(bigger, smaller) > 0);  // 20/2 > 20/3
		assertTrue(comp.compare(smaller, bigger) < 0);
	}

}
