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



{}

)
