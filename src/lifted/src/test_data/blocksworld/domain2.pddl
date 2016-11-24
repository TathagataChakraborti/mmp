(define (domain BLOCKS)
  (:requirements :strips :typing)
  (:types block)
  (:predicates (on ?x - block ?y - block)
           (ontable ?x - block)
           (clear ?x - block)
           (handempty)
           (holding ?x - block)
           )

(:action unstack
:parameters (?x - block ?y - block)
:precondition
(and
( on ?x ?y )
( clear ?x )
( handempty )
)
:effect
(and
( holding ?x )

)
)

(:action pickup
:parameters (?x - block)
:precondition
(and
( clear ?x )
( ontable ?x )
( handempty )
)
:effect
(and

(not ( ontable ?x ))
(not ( clear ?x ))
)
)

(:action putdown
:parameters (?x - block)
:precondition
(and

)
:effect
(and
( handempty )
(not ( holding ?x ))
)
)

(:action stack
:parameters (?x - block ?y - block)
:precondition
(and
( holding ?x )
( clear ?y )
)
:effect
(and
( clear ?x )
(not ( holding ?x ))
(not ( clear ?y ))
)
)


)
