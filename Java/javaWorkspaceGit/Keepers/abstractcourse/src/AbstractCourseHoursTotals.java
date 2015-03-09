
public abstract class AbstractCourseHoursTotals implements Comparable<AbstractCourseHoursTotals>{
	private String courseName;
	private int totalHoursSpent;
	private int reportCount;
	
	public AbstractCourseHoursTotals(String inCourseName, int inHoursSpent) {
		courseName = inCourseName;
		totalHoursSpent = inHoursSpent;
		reportCount = 1;
	}
	
	public String getCourseName() {
		return courseName;
	}
	
	public int getTotalHoursSpent() {
		return totalHoursSpent;
	}
	
	public int getReportCount() {
		return reportCount;
	}
	
	public void addToTotalHoursSpent(int moreHours) {
		totalHoursSpent += moreHours;
		reportCount++;
	}
	
	public boolean equals(Object what) {
		AbstractCourseHoursTotals other = (AbstractCourseHoursTotals) what;
		return courseName.equals(other.courseName);
	}
	
	public int compareTo(AbstractCourseHoursTotals other) {
		return totalHoursSpent - other.totalHoursSpent;
	}
	
	public abstract float getAverageHours();
	public abstract void addTime(int moreHours);
}
