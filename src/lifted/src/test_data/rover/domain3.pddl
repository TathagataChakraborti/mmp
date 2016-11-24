(define (domain Rover)
(:requirements :typing)
(:types rover waypoint store camera mode lander objective)

(:predicates (at ?x - rover ?y - waypoint)
             (at_lander ?x - lander ?y - waypoint)
             (can_traverse ?r - rover ?x - waypoint ?y - waypoint)
         (equipped_for_soil_analysis ?r - rover)
             (equipped_for_rock_analysis ?r - rover)
             (equipped_for_imaging ?r - rover)
             (empty ?s - store)
             (have_rock_analysis ?r - rover ?w - waypoint)
             (have_soil_analysis ?r - rover ?w - waypoint)
             (full ?s - store)
         (calibrated ?c - camera ?r - rover)
         (supports ?c - camera ?m - mode)
             (available ?r - rover)
             (visible ?w - waypoint ?p - waypoint)
             (have_image ?r - rover ?o - objective ?m - mode)
             (communicated_soil_data ?w - waypoint)
             (communicated_rock_data ?w - waypoint)
             (communicated_image_data ?o - objective ?m - mode)
         (at_soil_sample ?w - waypoint)
         (at_rock_sample ?w - waypoint)
             (visible_from ?o - objective ?w - waypoint)
         (store_of ?s - store ?r - rover)
         (calibration_target ?i - camera ?o - objective)
         (on_board ?i - camera ?r - rover)
         (channel_free ?l - lander)

)



(:action take_image
:parameters (?r - rover ?p - waypoint ?o - objective ?i - camera ?m - mode)
:precondition
(and
( supports ?i ?m )
( on_board ?i ?r )
( visible_from ?o ?p )
( equipped_for_imaging ?r )
( calibrated ?i ?r )
( at ?r ?p )
)
:effect
(and

(not ( calibrated ?i ?r ))
)
)

(:action communicate_image_data
:parameters (?r - rover ?l - lander ?o - objective ?m - mode ?x - waypoint ?y - waypoint)
:precondition
(and
( at_lander ?l ?y )
( visible ?x ?y )
( channel_free ?l )
( available ?r )
)
:effect
(and
( channel_free ?l )
( communicated_image_data ?o ?m )
( available ?r )

)
)

(:action sample_rock
:parameters (?x - rover ?s - store ?p - waypoint)
:precondition
(and
( at_rock_sample ?p )
( store_of ?s ?x )
( at ?x ?p )
( equipped_for_rock_analysis ?x )
( empty ?s )
)
:effect
(and
( have_rock_analysis ?x ?p )
( full ?s )
(not ( at_rock_sample ?p ))
(not ( empty ?s ))
)
)

(:action communicate_rock_data
:parameters (?r - rover ?l - lander ?p - waypoint ?x - waypoint ?y - waypoint)
:precondition
(and
( at_lander ?l ?y )
( visible ?x ?y )
( have_rock_analysis ?r ?p )
( channel_free ?l )
( available ?r )
)
:effect
(and
( channel_free ?l )
( available ?r )
( communicated_rock_data ?p )

)
)

(:action sample_soil
:parameters (?x - rover ?s - store ?p - waypoint)
:precondition
(and
( at_soil_sample ?p )
( store_of ?s ?x )
( equipped_for_soil_analysis ?x )
( at ?x ?p )
( empty ?s )
)
:effect
(and
( have_soil_analysis ?x ?p )
( full ?s )
(not ( at_soil_sample ?p ))
(not ( empty ?s ))
)
)

(:action navigate
:parameters (?x - rover ?y - waypoint ?z - waypoint)
:precondition
(and
( visible ?y ?z )
( at ?x ?y )
( available ?x )
( can_traverse ?x ?y ?z )
)
:effect
(and
( at ?x ?z )
(not ( at ?x ?y ))
)
)

(:action drop
:parameters (?x - rover ?y - store)
:precondition
(and
( store_of ?y ?x )
( full ?y )
)
:effect
(and
( empty ?y )
(not ( full ?y ))
)
)

(:action calibrate
:parameters (?r - rover ?i - camera ?t - objective ?w - waypoint)
:precondition
(and
( at ?r ?w )
( calibration_target ?i ?t )
( on_board ?i ?r )
)
:effect
(and
( calibrated ?i ?r )

)
)

(:action communicate_soil_data
:parameters (?r - rover ?l - lander ?p - waypoint ?x - waypoint ?y - waypoint)
:precondition
(and
( at_lander ?l ?y )
( available ?r )
( at ?r ?x )
)
:effect
(and
( channel_free ?l )
( communicated_soil_data ?p )

)
)


)
