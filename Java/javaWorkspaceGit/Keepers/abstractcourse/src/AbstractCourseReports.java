import java.util.Iterator;

public abstract class AbstractCourseReports implements Iterable<CourseHoursTotals> {
	private String weekOf;

	public AbstractCourseReports(String inWeekOf) {
		weekOf = inWeekOf;
	}
	
	public String getWeekOf() {
		return weekOf;
	}
	
	public abstract void addReport(CourseHoursTotals aRecord);
	public abstract Iterator<CourseHoursTotals> iteratorByCourse();
	public abstract Iterator<CourseHoursTotals> iteratorByAverageHours();
}
