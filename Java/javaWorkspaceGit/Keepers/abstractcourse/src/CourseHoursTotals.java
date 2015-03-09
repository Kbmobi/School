import java.util.Comparator;


public class CourseHoursTotals extends AbstractCourseHoursTotals {

	public CourseHoursTotals(String inCourseName, int inHoursSpent) {
		super(inCourseName, inHoursSpent);
	}
	
	@Override
	public float getAverageHours() {
		int total = getTotalHoursSpent();
		int samples = getReportCount();
		
		float average = total / (float) samples;
		return average;
	}

	@Override
	public void addTime(int moreHours) {
		addToTotalHoursSpent(moreHours);
	}
	
	public static Comparator<AbstractCourseHoursTotals> getByCourseName() {
		return new Comparator<AbstractCourseHoursTotals>(){

			@Override
			public int compare(AbstractCourseHoursTotals a,
					AbstractCourseHoursTotals b) {
				String aName = a.getCourseName();
				String bName = b.getCourseName();
				return aName.compareTo(bName);
			}
			
		};
	}
	
	public static Comparator<AbstractCourseHoursTotals> getByAverageHours() {
		return new Comparator<AbstractCourseHoursTotals>()  {

			@Override
			public int compare(AbstractCourseHoursTotals a,
					AbstractCourseHoursTotals b) {
				
				Float aAverage = a.getAverageHours();
				Float bAverage = b.getAverageHours();
				
				return aAverage.compareTo(bAverage);
			}
			
		};
	}

}
