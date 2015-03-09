import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;


public class CourseReports extends AbstractCourseReports {
	private List<CourseHoursTotals> allCourses;
	
	public CourseReports(String inWeekOf) {
		super(inWeekOf);
		
		allCourses = new ArrayList<>();
	}

	@Override
	public Iterator<CourseHoursTotals> iterator() {
		Collections.sort(allCourses);
		Collections.reverse(allCourses);
		return allCourses.iterator();
	}

	@Override
	public void addReport(CourseHoursTotals aRecord) {
		int position = allCourses.indexOf(aRecord);
		if(position == -1) {
			allCourses.add(aRecord);
			return;
		}
		
		CourseHoursTotals mergeInto = allCourses.get(position);
		int moreHours = aRecord.getTotalHoursSpent();
		mergeInto.addToTotalHoursSpent(moreHours);

	}

	@Override
	public Iterator<CourseHoursTotals> iteratorByCourse() {
		Collections.sort(allCourses, CourseHoursTotals.getByCourseName());
		return allCourses.iterator();
	}

	@Override
	public Iterator<CourseHoursTotals> iteratorByAverageHours() {
		Collections.sort(allCourses, CourseHoursTotals.getByAverageHours());
		return allCourses.iterator();
	}

}
