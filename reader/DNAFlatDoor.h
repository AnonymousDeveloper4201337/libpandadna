#ifndef DNAFLATDOOR_H
#define DNAFLATDOOR_H

#include "pandabase.h"
#include "DNADoor.h"

class EXPCL_PANDASKEL DNAFlatDoor : public DNADoor
{
	PUBLISHED:
		DNAFlatDoor(string name);
		~DNAFlatDoor(void);
};

#endif
