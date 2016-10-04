(define (problem tuck)

(:domain fetchworld)

(:objects b1 - box
	  loc1 loc2 loc3 loc4 - location)

(:init
(forklift-at loc4)
(trolley-at loc3)
	(block-at b1 loc1)
	(robot-at loc2)
	(hand-empty)
)


(:goal
(and
	(block-at b1 loc2)
)
)

)
