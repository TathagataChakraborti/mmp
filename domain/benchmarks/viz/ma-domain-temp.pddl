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
%OPERATORS%
)
