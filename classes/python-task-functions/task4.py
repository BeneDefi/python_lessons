# Task 4: Party Invite List
def invite_guests(invite_list, *guests, **special_notes):
    """
    Add guests to a party invite list, with optional special notes for VIPs.
    
    Parameters:
    invite_list: The existing list of invited guests.
    guests: Any number of guest names (strings).
    special_notes: Key-value pairs where the key is the guest name and 
                     the value is their special request or note.
    
    Example:
        invites = []
        invite_guests(invites, "John", "Mary", Peter="Needs wheelchair access")
    """
    
    invite_list = guests
    print(f"Invite list: {invite_list}")
    print(f"Number of guest(s): {len(guests)}")
    print(f"Special guest: {special_notes}")

invites = []
invite_guests(invites, "John", "Mary", Peter="Needs wheelchair access")
