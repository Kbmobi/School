import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;


public class AuctionItem implements AuctionItemInterface {
	private String itemName;
	private int firstBid;
	private List<Bid> allBids;
	
	public AuctionItem (String inName, int inBid) {
		itemName = inName;
		allBids = new ArrayList<Bid>();
		firstBid = inBid;
	}

	@Override
	public Iterator<Bid> iterator() {
		Collections.sort(allBids);
		return allBids.iterator();
	}

	@Override
	public String getDescription() {
		return itemName;
	}

	@Override
	public void makeBid(Bid newBid) {
		if(newBid.getAmount() <= firstBid ) {
			return;
		}
		
		int position = allBids.indexOf(newBid);
		if (position == -1) {
			allBids.add(newBid);
			firstBid = newBid.getAmount();
			return;
		}
		
	}

	@Override
	public Bid getHighestBid() {
		Bid i = Collections.max(allBids);
		return i;
	}

	@Override
	public Iterator<Bid> byName() {
		Collections.sort(allBids, Bid.getByName());
		return allBids.iterator();

	}
	

}
