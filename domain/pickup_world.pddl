(define (domain fetchworld)

(:requirements :strips :typing :action-costs :negative-preconditions)

(:types        location locatable - object
	       box - locatable
	       )

(:predicates   (hand-empty)
               (lighter-than-80-kg ?obj - box)
               (holding ?obj - box)
               (trolley-at ?loc - location)
               (trolley-prepared)
               (forklift-prepared)
               (forklift-at ?loc - location)
               (block-at ?obj - box ?pos - location)
	       (robot-at ?pos - location)
	       )

(:action move
	 :parameters	(?from ?to - location)
	 :precondition 	(and (robot-at ?from))
  	 :effect 	(and (robot-at ?to) (not (robot-at ?from)))
  	 )

(:action pickup
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and (hand-empty) (block-at ?obj ?loc) (robot-at ?loc) (lighter-than-80-kg ?obj))
  	 :effect 	(and (holding ?obj) (not (hand-empty)) (not (block-at ?obj ?loc)))
  	 )

(:action pickup_forklift
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and (hand-empty) (block-at ?obj ?loc) (robot-at ?loc) (forklift-at ?loc))
  	 :effect 	(and (holding ?obj) (not (hand-empty)) (not (block-at ?obj ?loc)))
  	 )

(:action prepare_trolley
         :parameters    (?loc - location)
         :precondition  (and (hand-empty) (robot-at ?loc) (trolley-at ?loc))
         :effect        (and (trolley-prepared))
         )

(:action move_trolley
	 :parameters	(?from ?to - location)
	 :precondition 	(and (robot-at ?from) (trolley-at ?from) (trolley-prepared))
  	 :effect 	(and (robot-at ?to) (trolley-at ?to) (not (robot-at ?from)) (not (trolley-at ?from)))
  	 )

(:action move_forklift
	 :parameters	(?from ?to - location)
	 :precondition 	(and (robot-at ?from)  (forklift-at ?from))
  	 :effect 	(and (robot-at ?to) (forklift-at ?to) (not (forklift-at ?from)) (not (robot-at ?from)))
  	 )

(:action pickup_trolley
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and (hand-empty) (block-at ?obj ?loc) (robot-at ?loc) (trolley-at ?loc))
  	 :effect 	(and (holding ?obj) (not (hand-empty)) (not (block-at ?obj ?loc)))
  	 )

(:action putdown
  	 :parameters	(?obj - box ?loc - location)
  	 :precondition 	(and (holding ?obj) (robot-at ?loc))
  	 :effect 	(and (not (holding ?obj)) (hand-empty) (block-at ?obj ?loc))
  	 )


)
