(define (domain fetchworld)

(:requirements :strips :typing :action-costs :negative-preconditions)

(:types        location locatable - object
	       box - locatable
	       )

(:predicates   (hand-tucked)
	       (hand-empty)
	       (charged)
               (holding ?obj - box)
               (block-at ?obj - box ?pos - location)
	       (robot-at ?pos - location)
	       )

(:action move
	 :parameters	(?from ?to - location)
	 :precondition 	(and )
  	 :effect 	(and )
  	 )

(:action pickup
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and )
  	 :effect 	(and )
  	 )

(:action putdown
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and )
  	 :effect 	(and )
  	 )

(:action tuck
  	 :parameters	()
  	 :precondition 	(and )
  	 :effect 	(and )
  	 )

(:action charge
  	 :parameters	()
  	 :precondition 	(and )
  	 :effect 	(and )
  	 )

)