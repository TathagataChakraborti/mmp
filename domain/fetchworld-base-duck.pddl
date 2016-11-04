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
               (crouched)
               (dummy1)
	       )

(:action move
	 :parameters	(?from ?to - location)
	 :precondition 	(and (robot-at ?from) (hand-tucked) (crouched))
  	 :effect 	(and (robot-at ?to) (not (robot-at ?from)))
  	 )

(:action pickup
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and (hand-empty) (block-at ?obj ?loc) (robot-at ?loc) (hand-tucked))
  	 :effect 	(and (holding ?obj) (not (hand-tucked)) (not (hand-empty)) (not (block-at ?obj ?loc)))
  	 )

(:action putdown
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and (holding ?obj) (robot-at ?loc))
  	 :effect 	(and (not (holding ?obj)) (not (hand-tucked)) (hand-empty) (block-at ?obj ?loc))
  	 )

(:action tuck
  	 :parameters	()
  	 :precondition 	(and (dummy1))
  	 :effect 	(and (hand-tucked) (crouched))
  	 )

(:action charge
  	 :parameters	()
  	 :precondition 	(and (dummy1))
  	 :effect 	(and (charged))
  	 )

(:action crouch
     :parameters    ()
     :precondition  (and (dummy1))
     :effect    (and (crouched))
)

)
