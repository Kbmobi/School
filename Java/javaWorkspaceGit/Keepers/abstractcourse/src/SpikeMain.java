import java.util.Iterator;


public class SpikeMain {

	public static void main(String[] args) {
		AbstractCourseReports thisWeek = new CourseReports("110220");
		
		thisWeek.addReport(new CourseHoursTotals("Comp101", 3));
		thisWeek.addReport(new CourseHoursTotals("Comp101", 6));
		thisWeek.addReport(new CourseHoursTotals("Bus111", 10));
		thisWeek.addReport(new CourseHoursTotals("Eng201", 5));
		thisWeek.addReport(new CourseHoursTotals("Bus111", 5));
		thisWeek.addReport(new CourseHoursTotals("Eng201", 8));
		thisWeek.addReport(new CourseHoursTotals("Comp101", 3));
		
		System.out.println("Courses by Total Hours");
		System.out.println("Course Hours Reports Average");
		
		for(AbstractCourseHoursTotals aReport : thisWeek) {
			System.out.println(aReport.getCourseName() + " " +
							aReport.getTotalHoursSpent() + " " +
							aReport.getReportCount() + " " +
							aReport.getAverageHours());			
		}
		
		System.out.println();

		System.out.println("Courses by Name");
		System.out.println("Course Hours Reports Average");
		
		Iterator<CourseHoursTotals> iter = thisWeek.iteratorByCourse();
		while(iter.hasNext()) {
			AbstractCourseHoursTotals aReport = iter.next();
			System.out.println(aReport.getCourseName() + " " +
					aReport.getTotalHoursSpent() + " " +
					aReport.getReportCount() + " " +
					aReport.getAverageHours());						
		}
		
		System.out.println();

		System.out.println("Courses by Average Hours");
		System.out.println("Course Hours Reports Average");
		
		Iterator<CourseHoursTotals> iterAverage = thisWeek.iteratorByAverageHours();
		while(iterAverage.hasNext()) {
			AbstractCourseHoursTotals aReport = iterAverage.next();
			System.out.println(aReport.getCourseName() + " " +
					aReport.getTotalHoursSpent() + " " +
					aReport.getReportCount() + " " +
					aReport.getAverageHours());						
		}
	}

}
