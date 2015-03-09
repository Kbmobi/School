import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;


public class Emcee implements EmceeInterface   {
	private List<Instructor> allInstructors;
	private ThrowerInterface currentThrower;
	private InstructorInterface currentVictim;
	private int gotsMoneys;
	private int position;
	
	public Emcee() {
		allInstructors = new ArrayList<Instructor>();
		currentThrower = new Thrower(0);
		currentVictim = new Instructor("");
		gotsMoneys = 0;
	}
	
	@Override
	public Iterator<Instructor> iterator() {
		Collections.sort(allInstructors);
		Collections.reverse(allInstructors);
		return allInstructors.iterator();
	}

	@Override
	public ThrowerInterface getCurrentThrower() {
		return currentThrower;
	}

	@Override
	public InstructorInterface getCurrentVictim() {
		return currentVictim;
	}

	@Override
	public void throwerStepsUp(ThrowerInterface nextThrower) {
		currentThrower = nextThrower;
	}

	@Override
	public void throwerChoosesVictim(Instructor victim) {
		int victimPosition = allInstructors.indexOf(victim);
		if (!(victimPosition >= 0)){
			allInstructors.add(victim);
			position = allInstructors.indexOf(victim);
			currentVictim = allInstructors.get(position);		
		}

		Instructor realInstructorFromList = allInstructors.get(position);
		int amountToAdd = victim.getMoneyRaised();
		realInstructorFromList.addToMoneyRaised(amountToAdd);
		position = allInstructors.indexOf(victim);
		
	}

	@Override
	public boolean throwAnother(int fundsPayed) {
		if(currentThrower.hasNext()){
			currentVictim.addToMoneyRaised(fundsPayed);
			gotsMoneys += fundsPayed;
			
			currentThrower.next();
			return true;
		}
		return false;
	}

	@Override
	public void dunked() {
		Instructor dunkedVictim = allInstructors.get(position);
		dunkedVictim.wasDunked();
	}

	@Override
	public int getTotalFundsRaised() {
		return gotsMoneys;
		
	}
}
