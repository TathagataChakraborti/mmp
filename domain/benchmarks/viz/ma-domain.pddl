(define (domain collective-decision)

;; 1. Comment - Underscores are predicates, dashes are actions
;; 2. Another comment -- Should we unset the preconditions of an action once the action executes? This 
;; will force CELia to check for preconds every single time when an action needs to be run - ASK JEFF
;; 3. ASK JEFF -- Is there some ordering to the setup actions? That should reflect in preconds.

  (:requirements 
    :typing
  )

  (:types
    person - object
    participant - person
  )

  (:predicates
    (orchestrated_collective_ranking)
    (determined_participants)
    (elicited_all_individual_preferences)
    (got_recent_people)
    (got_Celio_context)
    (displayed_participants)
    (displayed_alternatives)
    (got_full_context)
    (set_Celio_context)
    (added_participant ?p - participant)
    (removed_participant ?p - participant)

  ) 

  (:action orchestrate_collective_ranking
    :parameters ()
    :precondition (and 
    				(determined_participants)
    				(elicited_all_individual_preferences))
    :effect (and 
    				(orchestrated_collective_ranking)))

  (:action determine_participants
    :parameters ()
    :precondition (and 
    				(got_recent_people)
    				(got_Celio_context)
    				(displayed_participants))
    :effect (and 
    				(determined_participants)))

  (:action elicit_all_individual_preferences
    :parameters ()
    :precondition (and 
    				(got_Celio_context)
    				(displayed_alternatives))
    :effect (and 
    				(elicited_all_individual_preferences)))

;; Add participants, remove participants 

;; got_recent_people, got_Celio_context, displayed_participants, got_full_context, set_Celio_context, displayed_alternatives

  (:action get_recent_people
    :parameters ()
    :precondition (and )
    :effect (and (got_recent_people)))

  (:action get_Celio_context
    :parameters ()
    :precondition (and )
    :effect (and (got_Celio_context)))

  (:action display_participants
    :parameters ()
    :precondition (and )
    :effect (and (displayed_participants)))

  (:action get_full_context
    :parameters ()
    :precondition (and )
    :effect (and (got_full_context)))

  (:action set_Celio_context
    :parameters ()
    :precondition (and )
    :effect (and (set_Celio_context)))

  (:action display_alternatives
    :parameters ()
    :precondition (and )
    :effect (and (displayed_alternatives)))

	
  (:action add_participant
    :parameters (?p - participant)
    :precondition (and 
    				(got_full_context)
    				(set_Celio_context))
    :effect (and 
    				(displayed_participants)
    				(added_participant ?p)))

  (:action remove_participant
    :parameters (?p - participant)
    :precondition (and 
    				(got_full_context)
    				(set_Celio_context))
    :effect (and 
    				(displayed_participants)
    				(removed_participant ?p)))

)
