def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links?
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    if newFrob.myName() >= atMe.myName():
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        elif newFrob.myName() < atMe.getAfter().myName():
            newFrob.setAfter(atMe.getAfter())
            newFrob.setBefore(atMe)
            atMe.getAfter().setBefore(newFrob)
            atMe.setAfter(newFrob)
        else:
            insert(atMe.getAfter(), newFrob)

    if newFrob.myName() < atMe.myName():
        if atMe.getBefore() == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        elif newFrob.myName() > atMe.getBefore().myName():
            newFrob.setBefore(atMe.getBefore())
            newFrob.setAfter(atMe)
            atMe.getBefore().setAfter(newFrob)
            atMe.setBefore(newFrob)
        else:
            insert(atMe.getBefore(), newFrob)