(define (problem cd-prob1)
	
  (:domain collective-decision)

  (:objects
    jeff - participant
  )

  (:init
    (got_recent_people)  	
  ) 

  (:goal (and 
  			(added_participant jeff)
  			(orchestrated_collective_ranking))

  )

)