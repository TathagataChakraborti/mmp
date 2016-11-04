(define (problem tuck)

(:domain fetchworld)

(:objects b1 - box
	  loc1 loc2 - location)

(:init
	(block-at b1 loc1)
	(robot-at loc2)
	(hand-empty)
	(charged)
    (dummy1)
)


(:goal
(and
	(robot-at loc1)
)
)

)
